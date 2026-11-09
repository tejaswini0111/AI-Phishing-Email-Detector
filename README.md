## Security Disclaimer

This project is an educational phishing email detection system developed using machine learning and rule-based analysis.

The application identifies potentially suspicious email characteristics using:

- TF-IDF and Logistic Regression classification
- Suspicious URL pattern detection
- Suspicious keyword identification

**Important limitations:**

- Model predictions are not definitive security verdicts.
- Legitimate emails may be incorrectly flagged.
- Phishing emails may evade detection.
- URL indicators do not confirm that a domain is malicious.
- The application does not visit or verify extracted URLs.
- No email attachments are executed or opened.
