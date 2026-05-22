import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title="Student Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Advanced Student Performance Dashboard")
st.markdown("### Data Cleaning & Visualization Project")

st.markdown("---")

@st.cache_data

def load_data():
    df = pd.read_csv("advanced_students_dataset.csv")
    return df
df = load_data()

st.subheader("📁 Raw Dataset")
st.dataframe(df.head(10))

st.subheader("🧹 Data Cleaning Process")

st.write("### Missing Values Before Cleaning")
st.write(df.isnull().sum())


for col in ['Math', 'Science', 'English', 'Attendance']:
    df[col] = df[col].fillna(df[col].mean())
before_duplicates = df.shape[0]
df.drop_duplicates(inplace=True)
after_duplicates = df.shape[0]

Q1 = df['Math'].quantile(0.25)
Q3 = df['Math'].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR


df = df[(df['Math'] >= lower_limit) &
        (df['Math'] <= upper_limit)]
st.write("### Missing Values After Cleaning")
st.write(df.isnull().sum())

st.success("✅ Missing values handled successfully")
st.success("✅ Duplicate rows removed successfully")
st.success("✅ Outliers removed successfully")

st.markdown("---")
st.subheader("📌 Dashboard KPIs")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Students", df.shape[0])

with col2:
    st.metric("Average Math Marks", round(df['Math'].mean(), 2))

with col3:
    st.metric("Average Attendance", round(df['Attendance'].mean(), 2))

with col4:
    st.metric("Average Study Hours", round(df['Study_Hours'].mean(), 2))

st.markdown("---")
st.subheader("📊 Subject-wise Average Marks")

average_marks = df[['Math', 'Science', 'English']].mean().reset_index()
average_marks.columns = ['Subject', 'Average Marks']

fig1 = px.bar(
    average_marks,
    x='Subject',
    y='Average Marks',
    color='Subject',
    text='Average Marks',
    title='Average Subject Marks'
)

st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")
st.subheader("📈 Distribution of Math Marks")

fig2 = px.histogram(
    df,
    x='Math',
    nbins=20,
    color_discrete_sequence=['skyblue'],
    title='Math Marks Distribution'
)

st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.subheader("⏳ Study Hours vs Average Marks")

fig3 = px.scatter(
    df,
    x='Study_Hours',
    y='Average_Marks',
    color='Gender',
    size='Attendance',
    hover_data=['Name', 'Department'],
    title='Study Hours vs Average Marks'
)

st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.subheader("👨‍🎓 Gender-wise Performance")

fig4 = px.box(
    df,
    x='Gender',
    y='Math',
    color='Gender',
    title='Gender vs Math Marks'
)

st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")
st.subheader("🏫 Department-wise Average Performance")

department_avg = df.groupby('Department')['Average_Marks'].mean().reset_index()

fig5 = px.bar(
    department_avg,
    x='Department',
    y='Average_Marks',
    color='Department',
    text='Average_Marks',
    title='Department Performance'
)

st.plotly_chart(fig5, use_container_width=True)

st.markdown("---")
st.subheader("🔥 Correlation Heatmap")

correlation = df[[
    'Math',
    'Science',
    'English',
    'Attendance',
    'Study_Hours',
    'Average_Marks'
]].corr()
fig, ax = plt.subplots(figsize=(10, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm',
    ax=ax
)

st.pyplot(fig)

st.markdown("---")
st.subheader("💼 Placement Status Analysis")

placement_count = df['Placement_Status'].value_counts().reset_index()
placement_count.columns = ['Placement Status', 'Count']

fig6 = px.pie(
    placement_count,
    names='Placement Status',
    values='Count',
    title='Placement Distribution'
)

st.plotly_chart(fig6, use_container_width=True)

st.markdown("---")
st.subheader("🧠 Data Storytelling Insights")

st.info("Students with higher study hours tend to score better average marks.")
st.info("Attendance positively influences student performance.")
st.info("Outliers were successfully identified and removed.")
st.info("Department-wise performance differences are clearly visible.")
st.info("Math and Science scores show strong positive correlation.")

st.markdown("---")
st.success("🎉 Data Cleaning & Visualization Project Completed Successfully")
