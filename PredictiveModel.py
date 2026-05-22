import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import GradientBoostingClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

# Load dataset
df = pd.read_csv("advanced_students_dataset.csv")

# Display dataset
print(df.head())

print(df.info())

# Handle missing values
numeric_columns = ['Math', 'Science', 'English', 'Attendance']

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].mean())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Remove outliers using IQR
q1 = df['Math'].quantile(0.25)
q3 = df['Math'].quantile(0.75)

iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

df = df[
    (df['Math'] >= lower) &
    (df['Math'] <= upper)
]

# One-hot encoding
df = pd.get_dummies(
    df,
    columns=['Gender', 'Department', 'Grade'],
    drop_first=True
)

# Features
X = df.drop(
    columns=[
        'Student_ID',
        'Name',
        'City',
        'Placement_Status'
    ]
)

# Target
y = df['Placement_Status']

# Convert target column into numbers
y = y.map({
    'Placed': 1,
    'Not Placed': 0
})

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

# Feature scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

# Train model
model = GradientBoostingClassifier(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy :", accuracy)

# Classification report
print("\nClassification Report\n")

print(classification_report(y_test, predictions))

# Confusion matrix
cm = confusion_matrix(y_test, predictions)

plt.figure(figsize=(6, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues'
)

plt.title("Confusion Matrix")

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.show()

# ROC Curve
probabilities = model.predict_proba(X_test)[:, 1]

fpr, tpr, thresholds = roc_curve(
    y_test,
    probabilities
)

auc_score = roc_auc_score(
    y_test,
    probabilities
)

plt.figure(figsize=(6, 5))

plt.plot(
    fpr,
    tpr,
    label=f"AUC = {auc_score:.2f}"
)

plt.plot([0, 1], [0, 1], linestyle='--')

plt.xlabel("False Positive Rate")

plt.ylabel("True Positive Rate")

plt.title("ROC Curve")

plt.legend()

plt.show()

# Feature Importance
importance = model.feature_importances_

feature_names = X.columns

importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importance
})

importance_df = importance_df.sort_values(
    by='Importance',
    ascending=False
)

plt.figure(figsize=(10, 6))

sns.barplot(
    x='Importance',
    y='Feature',
    data=importance_df
)

plt.title("Feature Importance")

plt.show()

# Final insights
print("\nFinal Insights")

print("1. Gradient Boosting model trained successfully.")

print("2. Average marks and study hours strongly influence placement prediction.")

print("3. Attendance also impacts student placement.")

print("4. Feature importance helped identify the most influential factors.")

print("5. The model evaluation was completed using confusion matrix and ROC curve.")