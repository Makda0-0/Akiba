def analyze_password(password, min_length=8):
    passed = {
        "length":    len(password) >= min_length,
        "uppercase": any(c.isupper() for c in password),
        "lowercase": any(c.islower() for c in password),
        "digit":     any(c.isdigit() for c in password),
        "special":   any(not c.isalnum() for c in password),
    }
    missing = [k for k, v in passed.items() if not v]
    return {"passed": passed, "missing": missing}


count = 0
while count < 5:
    password = input("Enter password: ")
    result = analyze_password(password)
    print("Passed:", result["passed"])
    print("Missing:", result["missing"])
    print("")
    count = count + 1