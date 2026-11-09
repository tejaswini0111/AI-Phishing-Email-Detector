from keyword_detector import detect_suspicious_keywords

email = """
URGENT! Your account has been suspended.

Click here to verify your account
and reset password immediately.
"""

results = detect_suspicious_keywords(email)

print("Suspicious keywords detected:")

for word in results:
    print("-", word)