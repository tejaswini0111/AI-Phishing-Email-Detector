
import re
import ipaddress
from urllib.parse import urlparse

# Common URL shorteners
SHORTENERS = [
    "bit.ly",
    "tinyurl.com",
    "t.co",
    "is.gd",
    "cutt.ly",
    "rb.gy"
]

def extract_urls(email_text):

    pattern = r'https?://[^\s<>"\']+'

    urls = re.findall(
        pattern,
        email_text,
        flags=re.IGNORECASE
    )

    # Remove common trailing punctuation
    return [
        url.rstrip(".,!?;:)")
        for url in urls
    ]


def analyze_url(url):

    indicators = []

    parsed = urlparse(url)

    hostname = parsed.hostname or ""
    hostname = hostname.lower()

    # Check HTTP
    if parsed.scheme.lower() == "http":
        indicators.append(
            "Uses HTTP instead of HTTPS"
        )

    # Check IP address
    try:
        ipaddress.ip_address(hostname)
        indicators.append(
            "Uses an IP address instead of a domain"
        )
    except ValueError:
        pass

    # Check URL shorteners
    if hostname in SHORTENERS:
        indicators.append(
            "Uses a known URL shortening service"
        )

    # Check @ symbol
    if "@" in parsed.netloc:
        indicators.append(
            "Contains an @ symbol in the URL authority"
        )

    # Check punycode
    if "xn--" in hostname:
        indicators.append(
            "Contains a Punycode domain label"
        )

    # Check URL length
    if len(url) > 100:
        indicators.append(
            "Unusually long URL"
        )

    return indicators


def detect_suspicious_urls(email_text):

    urls = extract_urls(email_text)

    results = []

    for url in urls:

        indicators = analyze_url(url)

        results.append({
            "url": url,
            "indicators": indicators
        })

    return results
