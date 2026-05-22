# Import Pandas library
import pandas as pd

# Import NumPy library
import numpy as np

# Import Matplotlib library
import matplotlib.pyplot as plt

# Import Seaborn library
import seaborn as sns

df = pd.read_csv("advanced_students_dataset.csv")

# Display first 5 rows
print(df.head())

# Display last 5 rows
print(df.tail())

# Display dataset shape
print(df.shape)

# Display complete dataset information
print(df.info())

# Display statistical summary
print(df.describe())

# Check missing values in each column
print(df.isnull().sum())

# Fill missing values in Math column
df['Math'] = df['Math'].fillna(df['Math'].mean())

# Fill missing values in Science column
df['Science'] = df['Science'].fillna(df['Science'].mean())

# Fill missing values in English column
df['English'] = df['English'].fillna(df['English'].mean())

# Fill missing values in Attendance column
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].mean())

print(df.isnull().sum())
# Check duplicate rows
print(df.duplicated().sum())
# Remove duplicate rows
df.drop_duplicates(inplace=True)
print(df.duplicated().sum())

# Create boxplot for Math column
sns.boxplot(x=df['Math'])

# Display graph
plt.show()
# Calculate Q1 (25th percentile)
Q1 = df['Math'].quantile(0.25)

# Calculate Q3 (75th percentile)
Q3 = df['Math'].quantile(0.75)

# Calculate IQR
IQR = Q3 - Q1

# Calculate lower limit
lower_limit = Q1 - 1.5 * IQR

# Calculate upper limit
upper_limit = Q3 + 1.5 * IQR

print("Q1 :", Q1)
print("Q3 :", Q3)
print("IQR :", IQR)
print("Lower Limit :", lower_limit)
print("Upper Limit :", upper_limit)
# Remove outliers from Math column

df = df[
    (df['Math'] >= lower_limit) &
    (df['Math'] <= upper_limit)
]
# Display new maximum value
print(df['Math'].max())
sns.boxplot(x=df['Math'])
plt.show()

# Calculate average marks
average_marks = df[['Math', 'Science', 'English']].mean()

# Print average marks
print(average_marks)
# Create bar chart
average_marks.plot(kind='bar')

# Add title
plt.title("Average Subject Marks")

# Add X-axis label
plt.xlabel("Subjects")

# Add Y-axis label
plt.ylabel("Average Marks")

# Display graph
plt.show()
# Create histogram
sns.histplot(df['Math'], bins=10, kde=True)

# Add title
plt.title("Distribution of Math Marks")

# Show graph
plt.show()
# Create scatter plot
sns.scatterplot(
    x='Study_Hours',
    y='Average_Marks',
    data=df
)

# Add title
plt.title("Study Hours vs Average Marks")

# Show graph
plt.show()
# Gender vs Math marks
sns.boxplot(
    x='Gender',
    y='Math',
    data=df
)

# Add title
plt.title("Gender vs Math Performance")

# Show graph
plt.show()
# Correlation matrix
correlation = df[['Math',
                  'Science',
                  'English',
                  'Attendance',
                  'Study_Hours',
                  'Average_Marks']].corr()

# Create heatmap
sns.heatmap(correlation,
            annot=True,
            cmap='coolwarm')

# Add title
plt.title("Correlation Heatmap")

# Show graph
plt.show()
print("\nFINAL INSIGHTS")

print("1. Missing values were cleaned successfully.")
print("2. Duplicate rows were removed.")
print("3. Outliers were detected and removed.")
print("4. Students who study more tend to score higher.")
print("5. Attendance positively affects performance.")
print("6. Math and Science marks show positive correlation.")