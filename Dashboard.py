import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Student Performance Dashboard",
    layout="wide"
)

st.title("Student Performance Dashboard")
st.write("Analysis of student academic performance and attendance data")


@st.cache_data
def load_data():
    return pd.read_csv("advanced_students_dataset.csv")


df = load_data()

# Dataset Preview

st.subheader("Dataset Preview")
st.dataframe(df.head())


# Data Cleaning

st.subheader("Data Cleaning")

missing_before = df.isnull().sum()

numeric_columns = ['Math', 'Science', 'English', 'Attendance']

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].mean())

df.drop_duplicates(inplace=True)

q1 = df['Math'].quantile(0.25)
q3 = df['Math'].quantile(0.75)

iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

df = df[(df['Math'] >= lower) & (df['Math'] <= upper)]

missing_after = df.isnull().sum()

col1, col2 = st.columns(2)

with col1:
    st.write("Missing Values Before Cleaning")
    st.write(missing_before)

with col2:
    st.write("Missing Values After Cleaning")
    st.write(missing_after)

st.success("Data cleaning completed")


# Overview

st.subheader("Overview")

k1, k2, k3, k4 = st.columns(4)

k1.metric("Total Students", len(df))
k2.metric("Average Math Score", round(df['Math'].mean(), 2))
k3.metric("Average Attendance", round(df['Attendance'].mean(), 2))
k4.metric("Average Study Hours", round(df['Study_Hours'].mean(), 2))


# Filter Data

st.subheader("Filter Data")

department = st.selectbox(
    "Select Department",
    ["All"] + list(df['Department'].unique())
)

if department != "All":
    filtered_df = df[df['Department'] == department]
else:
    filtered_df = df


# Subject Average Scores

st.subheader("Subject Average Scores")

subject_avg = filtered_df[
    ['Math', 'Science', 'English']
].mean().reset_index()

subject_avg.columns = ['Subject', 'Average Score']

bar_chart = px.bar(
    subject_avg,
    x='Subject',
    y='Average Score',
    color='Subject',
    text='Average Score'
)

st.plotly_chart(bar_chart, use_container_width=True)


# Math Score Distribution

st.subheader("Math Score Distribution")

hist_chart = px.histogram(
    filtered_df,
    x='Math',
    nbins=15
)

st.plotly_chart(hist_chart, use_container_width=True)


# Study Hours vs Performance

st.subheader("Study Hours vs Performance")

scatter_chart = px.scatter(
    filtered_df,
    x='Study_Hours',
    y='Average_Marks',
    color='Department',
    hover_data=['Name']
)

st.plotly_chart(scatter_chart, use_container_width=True)


# Gender-wise Math Performance

st.subheader("Gender-wise Math Performance")

gender_chart = px.box(
    filtered_df,
    x='Gender',
    y='Math',
    color='Gender'
)

st.plotly_chart(gender_chart, use_container_width=True)


# Department Performance

st.subheader("Department Performance")

dept_avg = filtered_df.groupby(
    'Department'
)['Average_Marks'].mean().reset_index()

dept_chart = px.bar(
    dept_avg,
    x='Department',
    y='Average_Marks',
    color='Department',
    text='Average_Marks'
)

st.plotly_chart(dept_chart, use_container_width=True)


# Correlation Heatmap

st.subheader("Correlation Heatmap")

corr_data = filtered_df[
    [
        'Math',
        'Science',
        'English',
        'Attendance',
        'Study_Hours',
        'Average_Marks'
    ]
].corr()

fig, ax = plt.subplots(figsize=(8, 5))

sns.heatmap(
    corr_data,
    annot=True,
    cmap='Blues',
    ax=ax
)

st.pyplot(fig)


# Placement Status

st.subheader("Placement Status")

placement_data = filtered_df[
    'Placement_Status'
].value_counts().reset_index()

placement_data.columns = ['Status', 'Count']

pie_chart = px.pie(
    placement_data,
    names='Status',
    values='Count'
)

st.plotly_chart(pie_chart, use_container_width=True)


# Top Performer

st.subheader("Top Performer")

top_student = filtered_df.loc[
    filtered_df['Average_Marks'].idxmax()
]

st.write("Name:", top_student['Name'])
st.write("Department:", top_student['Department'])
st.write("Average Marks:", round(top_student['Average_Marks'], 2))


# Insights

st.subheader("Insights")

st.write("- Students with better attendance generally score higher.")
st.write("- Study hours have a positive impact on performance.")
st.write("- Some departments perform better on average.")
st.write("- Math and Science marks show strong correlation.")

st.success("Dashboard updated successfully")