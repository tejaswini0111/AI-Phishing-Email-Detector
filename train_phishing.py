
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# 1. Load cleaned dataset
df = pd.read_csv(
    "dataset/cleaned_phishing_emails.csv"
)

# 2. Normalize labels
# Adjust these values to match your actual dataset.
label_mapping = {
    "phishing": 1,
    "1": 1,
    "legitimate": 0,
    "legit": 0,
    "safe": 0,
    "0": 0
}

df["label"] = (
    df["label"]
    .astype(str)
    .str.strip()
    .str.lower()
    .map(label_mapping)
)

# Remove labels that could not be mapped
df = df.dropna(subset=["label"])

df["label"] = df["label"].astype(int)

# 3. Prepare features and labels
X = df["email"].astype(str)
y = df["label"]

# Verify that both classes exist
if y.nunique() != 2:
    raise ValueError(
        "Dataset must contain both phishing and legitimate emails."
    )

# 4. Split training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

# 5. Build machine learning pipeline
pipeline = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            ngram_range=(1, 2),
            max_features=10000,
            stop_words="english"
        )
    ),
    (
        "clf",
        LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            random_state=42
        )
    )
])

# 6. Train model
print("\nTraining model...")

pipeline.fit(X_train, y_train)

print("Training completed!")

# 7. Predict test data
predictions = pipeline.predict(X_test)

# 8. Evaluate model
accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nAccuracy:", round(accuracy, 4))

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        predictions,
        labels=[0, 1],
        target_names=["Legitimate", "Phishing"],
        zero_division=0
    )
)

print("\nConfusion Matrix:")

print(
    confusion_matrix(
        y_test,
        predictions,
        labels=[0, 1]
    )
)

# 9. Save model
joblib.dump(
    pipeline,
    "phishing_model.joblib"
)

print("\nModel saved successfully!")