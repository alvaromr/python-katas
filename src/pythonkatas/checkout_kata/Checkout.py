from pydantic import BaseModel


class PriceRule(BaseModel):
    code: str
    base_price: int
    discount_amount: int
    discount_per: int

    def apply(self, codes) -> int:
        scan_count = codes.count(self.code)
        total_base = self.base_price * scan_count
        discount = self.discount_amount * (scan_count // self.discount_per)
        return total_base - discount


class Checkout:
    def __init__(self, price_rules):
        self.price_rules = price_rules
        self.codes = list()

    def scan(self, code):
        self.codes.append(code)

    @property
    def total(self):
        return sum(rule.apply(self.codes) for rule in self.price_rules)


def build_price_rules(text: str) -> list[PriceRule]:
    if not text:
        return []
    import os

    try:
        from dotenv import load_dotenv
        load_dotenv(os.path.join(os.path.expanduser("~"), ".env"))
    except Exception:
        pass

    try:
        from google import genai
        from google.genai import types
    except Exception as exc:
        raise RuntimeError("'google-generativeai' no disponible") from exc

    api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY o GEMINI_API_KEY no disponibles.")

    client = genai.Client(api_key=api_key)

    system_instructions = (
        "You are a parser that converts price rules written in natural language "
        "into a JSON list of objects with the following strict schema: "
        '[{"code": str, "base_price": int, "discount_amount": int, "discount_per": int}]. '
        "Do not include comments or additional fields. "
        "Use positive integers. "
        "Respond ONLY with the JSON array, no additional text."
        "'code' is the product identifier (e.g. 'A', 'B', ...). "
        "'base_price' is the unit price without discount. "
        "'discount_amount' is the total discount applied for each group of 'discount_per' units, "
        "and it is never greater than 'base_price'. "
        "'discount_per' is the size of the group of units to which that discount applies. "
        "If any rule does not specify a discount, return discount_amount=0 and discount_per=1 for that code."
    )

    user_prompt = (
        "Convert the following rules text to strict JSON with the indicated schema. "
        f"Rules text:\n{text}"
    )

    try:
        response= client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                response_mime_type= "application/json",
                response_schema= list[PriceRule],
                system_instruction=system_instructions,
            ),
            contents=types.Part.from_text(text=user_prompt),
        )
    except Exception as exc:
        raise RuntimeError("Error al invocar Gemini: " + str(exc)) from exc

    return response.parsed
