import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv("/Users/aniamarjankowska/Documents/GitHub/python_programming/ev_charging_patterns.csv", sep=",")


# Divide the page into columns
col1, col2 = st.columns([0.25, 0.75])

# Title and first plot
col1.subheader('Pierwszy wykres')
col1.write(data.head())  # Displaying the first few rows of data for context

fig, ax = plt.subplots()
sns.histplot(data=data, x=data.columns[0], ax=ax, kde=True)
col2.pyplot(fig)
