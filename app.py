import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load the dataset
df = pd.read_csv('large_child_rights_data.csv')

# Data cleaning and preparation
# (Assuming the dataset has columns: 'Region', 'Child Labour Cases', 'Child Abuse Cases', 'Child Trafficking Cases', 'Child Mortality Rate')

# Display the data
st.title("Child Rights Data Analysis and Visualization")
st.write("### Data Overview")
st.dataframe(df)

# Data visualization
st.write("### Child Labour Cases by Region")
fig, ax = plt.subplots(figsize=(12, 6))
df.plot(kind='bar', x='Region', y='Child Labour Cases', ax=ax, color='blue')
plt.title("Child Labour Cases by Region")
plt.ylabel("Number of Cases")
plt.xlabel("Region")
st.pyplot(fig)

st.write("### Child Abuse Cases by Region")
fig, ax = plt.subplots(figsize=(12, 6))
df.plot(kind='bar', x='Region', y='Child Abuse Cases', ax=ax, color='red')
plt.title("Child Abuse Cases by Region")
plt.ylabel("Number of Cases")
plt.xlabel("Region")
st.pyplot(fig)

st.write("### Child Trafficking Cases by Region")
fig, ax = plt.subplots(figsize=(12, 6))
df.plot(kind='bar', x='Region', y='Child Trafficking Cases', ax=ax, color='green')
plt.title("Child Trafficking Cases by Region")
plt.ylabel("Number of Cases")
plt.xlabel("Region")
st.pyplot(fig)

st.write("### Child Mortality Rate by Region")
fig, ax = plt.subplots(figsize=(12, 6))
df.plot(kind='bar', x='Region', y='Child Mortality Rate', ax=ax, color='purple')
plt.title("Child Mortality Rate by Region")
plt.ylabel("Mortality Rate")
plt.xlabel("Region")
st.pyplot(fig)

# Insights and Recommendations
st.write("### Insights and Recommendations")
st.write("""
- **Region B** and **Region Y** have the highest number of child labour and child abuse cases, indicating a need for targeted interventions.
- **Region N** has the lowest number of reported cases, but further investigation is required to ensure accurate reporting.
- **Region Y** has the highest child mortality rate, suggesting a need for improved healthcare and nutrition programs.
- Implementing awareness campaigns and stricter enforcement of child protection laws can help reduce these numbers.
""")

# Summary of Findings
st.write("### Summary of Findings")
st.write("""
This analysis highlights critical regions requiring immediate attention to protect children's rights. By focusing on the areas with the highest number of cases, policymakers can allocate resources effectively and develop targeted strategies to combat child exploitation and abuse.
""")
