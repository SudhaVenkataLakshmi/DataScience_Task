import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("advanced_students_dataset.csv")

# Dataset preview
print(df.head())
print(df.tail())

# Dataset details
print(df.shape)
print(df.info())
print(df.describe())

# Missing values
print(df.isnull().sum())

# Fill missing values
df['Math'] = df['Math'].fillna(df['Math'].mean())
df['Science'] = df['Science'].fillna(df['Science'].mean())
df['English'] = df['English'].fillna(df['English'].mean())
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].mean())

print(df.isnull().sum())

# Duplicate rows
print("Duplicate Rows :", df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("Duplicate Rows After Cleaning :", df.duplicated().sum())

# Boxplot before removing outliers
sns.boxplot(x=df['Math'])
plt.title("Math Marks Before Outlier Removal")
plt.show()

# IQR Method
q1 = df['Math'].quantile(0.25)
q3 = df['Math'].quantile(0.75)

iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

print("Q1 :", q1)
print("Q3 :", q3)
print("IQR :", iqr)

# Remove outliers
df = df[
    (df['Math'] >= lower) &
    (df['Math'] <= upper)
]

# Boxplot after removing outliers
sns.boxplot(x=df['Math'])
plt.title("Math Marks After Outlier Removal")
plt.show()

# Average subject marks
avg_marks = df[['Math', 'Science', 'English']].mean()

print(avg_marks)

avg_marks.plot(kind='bar')

plt.title("Average Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.show()

# Histogram
sns.histplot(df['Math'], bins=10, kde=True)

plt.title("Math Marks Distribution")

plt.show()

# Scatter plot
sns.scatterplot(
    x='Study_Hours',
    y='Average_Marks',
    data=df
)

plt.title("Study Hours vs Average Marks")

plt.show()

# Gender analysis
sns.boxplot(
    x='Gender',
    y='Math',
    data=df
)

plt.title("Gender vs Math Marks")

plt.show()

# Correlation heatmap
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

sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

plt.show()

# Insights
print("\nFinal Insights")

print("1. Missing values cleaned successfully.")
print("2. Duplicate rows removed.")
print("3. Outliers handled using IQR method.")
print("4. Students with more study hours scored better.")
print("5. Attendance affects academic performance.")
print("6. Math and Science marks are positively correlated.")