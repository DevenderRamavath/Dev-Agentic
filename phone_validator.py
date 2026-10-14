import re


def is_valid_phone_number(phone: str) -> bool:
    """Validate common international phone number formats.

    Accepted examples:
    - +1 (555) 123-4567
    - 555-123-4567
    - 5551234567
    - +44 20 7946 0958

    Rules:
    - Optional leading '+'
    - Accepts spaces, hyphens, and parentheses as separators
    - Requires 10 to 15 digits total
    """
    if not isinstance(phone, str):
        return False

    cleaned = phone.strip()
    if not cleaned:
        return False

    # Allow optional +, digits, spaces, hyphens, and parentheses
    pattern = r"^\+?[0-9()\-\s]{10,20}$"
    if not re.fullmatch(pattern, cleaned):
        return False

    digits_only = re.sub(r"\D", "", cleaned)
    return 10 <= len(digits_only) <= 15


if __name__ == "__main__":
    samples = [
        "+1 (555) 123-4567",
        "555-123-4567",
        "5551234567",
        "+44 20 7946 0958",
        "123",
        "abc",
    ]

    for sample in samples:
        print(f"{sample!r}: {is_valid_phone_number(sample)}")
