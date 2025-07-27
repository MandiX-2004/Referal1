def validate_code(code, existing_codes):
    if not (len(code) == 5 and code[:2].isalpha() and code[2:].isdigit()):
        return False
    if code in existing_codes:
        return False
    return True
