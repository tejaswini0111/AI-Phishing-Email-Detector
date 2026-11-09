
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

# Load the same cleaned dataset
df = pd.read_csv(
    "dataset/cleaned_phishing_emails.csv"
)

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

df = df.dropna(subset=["label"])
df["label"] = df["label"].astype(int)

X = df["email"].astype(str)
y = df["label"]

# Recreate the same test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Load trained model
model = joblib.load("phishing_model.joblib")

# Predict
predictions = model.predict(X_test)

# Confusion matrix
cm = confusion_matrix(
    y_test,
    predictions,
    labels=[0, 1]
)

# Plot
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Legitimate", "Phishing"],
    yticklabels=["Legitimate", "Phishing"]
)

plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")
plt.title("Phishing Detection Confusion Matrix")

plt.tight_layout()

plt.savefig("confusion_matrix.png")

plt.show()

print("Confusion matrix saved!")
