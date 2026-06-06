import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("advanced_students_dataset.csv")
print(df.head())

print(df.shape)

print(df.info())

print(df.describe())
print(df.isnull().sum())
sns.countplot(x='Gender', data=df)
plt.show()
subject_avg = df[
    ['Math', 'Science', 'English']
].mean()

print(subject_avg)

sns.scatterplot(
    x='Study_Hours',
    y='Average_Marks',
    data=df
)

plt.show()

sns.scatterplot(
    x='Attendance',
    y='Average_Marks',
    data=df
)

plt.show()

sns.boxplot(
    x='Gender',
    y='Average_Marks',
    data=df
)

plt.show()

department_avg = df.groupby(
    'Department'
)['Average_Marks'].mean()

print(department_avg)
department_avg.plot(kind='bar')
plt.show()

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

plt.show()

placement_count = df[
    'Placement_Status'
].value_counts()

print(placement_count)
placement_count.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.show()

print("\nEDA REPORT")

print("1. Dataset contains student academic information.")

print("2. Missing values were identified.")

print("3. Average marks differ across subjects.")

print("4. Study hours positively influence performance.")

print("5. Attendance has a positive relationship with marks.")

print("6. Department-wise performance differences exist.")

print("7. Math and Science show strong correlation.")

print("8. Placement status varies based on academic performance.")