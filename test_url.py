from url_detector import detect_suspicious_urls

email = """
Your account is suspended.
Please visit http://192.168.1.100/login
"""

results = detect_suspicious_urls(email)

for result in results:

    print("\nURL:", result["url"])

    if result["indicators"]:
        print("Indicators:")

        for indicator in result["indicators"]:
            print("-", indicator)

    else:
        print("No configured URL indicators detected.")