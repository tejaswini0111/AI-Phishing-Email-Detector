
import re

SUSPICIOUS_KEYWORDS = [
    "urgent",
    "verify your account",
    "account suspended",
    "password expired",
    "click here",
    "free reward",
    "reset password",
    "limited time",
    "immediate action",
    "confirm your identity",
    "update your payment",
    "unusual activity",
    "account compromised",
    "claim your prize"
]


def detect_suspicious_keywords(email_text):

    text = email_text.lower()

    found_keywords = []

    for keyword in SUSPICIOUS_KEYWORDS:

        pattern = (
            r"(?<!\w)"
            + re.escape(keyword)
            + r"(?!\w)"
        )

        if re.search(pattern, text):

            found_keywords.append(keyword)

    return found_keywords
