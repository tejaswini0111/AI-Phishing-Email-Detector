
import streamlit as st
import joblib

from url_detector import detect_suspicious_urls
from keyword_detector import detect_suspicious_keywords


# Page configuration
st.set_page_config(
    page_title="AI Phishing Email Detector",
    page_icon="🛡️",
    layout="wide"
)


# Load trained model
@st.cache_resource
def load_model():

    return joblib.load("phishing_model.joblib")


model = load_model()


# Dashboard title
st.title("🛡️ AI-Powered Phishing Email Detector")

st.write(
    "Analyze email content using machine learning "
    "and rule-based security indicators."
)

st.divider()


# Email input
st.subheader("Email Analysis")

email_text = st.text_area(
    "Paste email content here:",
    height=220,
    placeholder="Paste the email you want to analyze..."
)


# Analyze button
if st.button("Analyze Email", type="primary"):

    if not email_text.strip():

        st.warning("Please enter email content.")

    else:

        # Machine learning prediction
        prediction = model.predict([email_text])[0]

        probabilities = model.predict_proba(
            [email_text]
        )[0]

        classes = model.classes_

        # URL detection
        urls = detect_suspicious_urls(email_text)

        # Keyword detection
        keywords = detect_suspicious_keywords(
            email_text
        )

        st.divider()

        st.subheader("Analysis Results")

        # Prediction result
        if prediction == 1:

            st.error(
                "Potential Phishing Email Detected"
            )

        else:

            st.success(
                "Model Classified This Email as Legitimate"
            )

        # Model scores
        st.subheader("Model Class Scores")

        score_columns = st.columns(len(classes))

        for column, label, score in zip(
            score_columns,
            classes,
            probabilities
        ):

            class_name = (
                "Phishing" if label == 1
                else "Legitimate"
            )

            column.metric(
                class_name,
                f"{score * 100:.2f}%"
            )

        st.caption(
            "These are model scores, not guaranteed "
            "probabilities that an email is malicious."
        )

        st.divider()

        # URL results
        st.subheader("🔗 URL Analysis")

        if urls:

            for result in urls:

                st.write("URL:", result["url"])

                if result["indicators"]:

                    for indicator in result["indicators"]:

                        st.warning(indicator)

                else:

                    st.info(
                        "No configured suspicious URL "
                        "indicators were detected."
                    )

        else:

            st.info("No HTTP/HTTPS URLs found.")

        st.divider()

        # Keyword results
        st.subheader("🔍 Keyword Analysis")

        if keywords:

            st.warning(
                "Potentially suspicious phrases detected:"
            )

            for word in keywords:

                st.write("- ", word)

        else:

            st.success(
                "No configured suspicious keywords detected."
            )

        st.divider()

        # Final disclaimer
        st.info(
            "Security Notice: This tool is an educational "
            "phishing detection system. A legitimate "
            "classification does not guarantee that an "
            "email is safe. A phishing classification "
            "does not independently prove maliciousness. "
            "Verify senders, links and attachments using "
            "trusted security procedures."
        )


# Sidebar
st.sidebar.title("About This Project")

st.sidebar.write(
    """
    **Technologies**

    - Python
    - Scikit-learn
    - TF-IDF
    - Logistic Regression
    - Streamlit
    - Pandas

    **Detection Methods**

    - Machine learning classification
    - Suspicious URL indicators
    - Suspicious keyword analysis
    """
)

st.sidebar.divider()

st.sidebar.caption(
    "Cybersecurity Educational Project"
)
