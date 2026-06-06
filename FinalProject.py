
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_curve,
    roc_auc_score
)


# PROJECT TITLE


print("Educational Analytics and Placement Prediction System")
print("Real-World Data Science Project")

# LOAD DATASET

df = pd.read_csv("advanced_students_dataset.csv")

# DATA CLEANING

# Handle missing values
for col in ['Math', 'Science', 'English', 'Attendance']:
    df[col] = df[col].fillna(df[col].mean())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove outliers using IQR (Math column)
q1 = df['Math'].quantile(0.25)
q3 = df['Math'].quantile(0.75)

iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

df = df[
    (df['Math'] >= lower) &
    (df['Math'] <= upper)
]

# DATASET OVERVIEW

print("\nDataset Shape")
print(df.shape)

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

# SUBJECT PERFORMANCE ANALYSIS

subject_avg = df[
    ['Math', 'Science', 'English']
].mean()

print("\nAverage Subject Marks")
print(subject_avg)

subject_avg.plot(kind='bar')

plt.title("Average Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.show()

# DEPARTMENT ANALYSIS

department_avg = df.groupby(
    'Department'
)['Average_Marks'].mean()

print("\nDepartment Wise Average Marks")
print(department_avg)

department_avg.plot(
    kind='bar'
)

plt.title("Department Wise Performance")
plt.xlabel("Department")
plt.ylabel("Average Marks")

plt.show()

# PLACEMENT ANALYSIS

placement = df[
    'Placement_Status'
].value_counts()

print("\nPlacement Status Distribution")
print(placement)

placement.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Placement Distribution")
plt.ylabel("")

plt.show()

# STUDY HOURS ANALYSIS

sns.scatterplot(
    x='Study_Hours',
    y='Average_Marks',
    data=df
)

plt.title("Study Hours vs Average Marks")

plt.show()

# ATTENDANCE ANALYSIS

sns.scatterplot(
    x='Attendance',
    y='Average_Marks',
    data=df
)

plt.title("Attendance vs Average Marks")

plt.show()

# CORRELATION ANALYSIS

corr = df[
    [
        'Math',
        'Science',
        'English',
        'Attendance',
        'Study_Hours',
        'Average_Marks'
    ]
].corr()

plt.figure(figsize=(8, 5))

sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

plt.show()

# MACHINE LEARNING SECTION

df_ml = pd.get_dummies(
    df,
    columns=[
        'Gender',
        'Department',
        'Grade'
    ],
    drop_first=True
)

X = df_ml.drop(
    columns=[
        'Student_ID',
        'Name',
        'City',
        'Placement_Status'
    ]
)

y = df_ml['Placement_Status'].map({
    'Placed': 1,
    'Not Placed': 0
})

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = GradientBoostingClassifier(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nPLACEMENT PREDICTION RESULTS")
print("Accuracy :", accuracy)

print("\nClassification Report\n")
print(
    classification_report(
        y_test,
        predictions
    )
)

# CONFUSION MATRIX

cm = confusion_matrix(
    y_test,
    predictions
)

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

# ROC CURVE


probabilities = model.predict_proba(X_test)[:, 1]

fpr, tpr, _ = roc_curve(
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

plt.plot(
    [0, 1],
    [0, 1],
    linestyle='--'
)

plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()

plt.show()

# FEATURE IMPORTANCE

importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
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


print("\nFINAL PROJECT CONCLUSIONS")

print("1. Students with higher study hours tend to achieve better academic performance.")

print("2. Attendance positively influences student success.")

print("3. Average Marks is one of the strongest indicators of placement outcomes.")

print("4. Department-wise differences exist in academic performance.")

print("5. Machine Learning successfully predicts placement status.")

print("6. Educational institutions can use analytics to improve student performance and placement rates.")