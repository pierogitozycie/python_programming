import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Zadanie 1
data = pd.read_csv("/Users/aniamarjankowska/Documents/GitHub/python_programming/ev_charging_patterns.csv", sep=",")
print(data.head())

# Podziel stronę na kolumny : col1, col2 = st.columns([0.25 , 0.75])
col1, col2 = st.columns([0.25, 0.75])


col1.subheader('Pierwszy wykres')
col1.write("Kolumna pierwsza")
col2.write("Kolumna druga")
st.write(data.head()) 
fig = px.scatter(data, x = "Battery Capacity (kWh)", y="Vehicle Model")
st.plotly_chart(fig)

# Zadanie 2

st.sidebar.header("Nawigacja")
select_model= st.sidebar.selectbox("Wybierz kolumnę do analizy", options=data['Vehicle Model'])
slider_value = st.sidebar.slider("Wybierz zakres", min_value=int(data['Charging Cost (USD)'].min()), max_value=int(data['Charging Cost (USD)'].max()), value=(10, 100))
show_plot = st.sidebar.checkbox("Pokaż wykresy")

filtered_data = data[(data['Charging Cost (USD)'] >= slider_value[0]) & (data['Charging Cost (USD)'] <= slider_value[1])]



if show_plot:
    filtered_data = data[data["Vehicle Model"] == select_model]
    st.write(f"Model: {select_model}")
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('black') 
    ax.set_facecolor('black')    
    ax.tick_params(colors="white") 
    ax.set_xlabel("Log Charging Rate (kW)", color="white") 
    ax.set_ylabel("Charging Cost (USD)", color="white")  
    sns.histplot(
        filtered_data, 
        x = "Charging Rate (kW)", 
        y = "Charging Cost (USD)", 
        cbar = True, 
        ax = ax,
        cmap = 'cool'
    )
    st.pyplot(fig)

    fig, ax = plt.subplots()
    fig.patch.set_facecolor('black') 
    ax.set_facecolor('black')    
    ax.tick_params(colors="white") 
    ax.scatter(
        filtered_data['Temperature (°C)'], 
        filtered_data['Charging Cost (USD)'], 
        color='blue', alpha=0.7
    )
    ax.set_title(f"Charging Cost vs Temperature for {select_model}", color = "white")
    ax.set_xlabel("Temperature (°C)", color = "white")
    ax.set_ylabel("Charging Cost (USD)", color = "white")
    ax.grid()
    st.pyplot(fig)



# streamlit run /Users/aniamarjankowska/Documents/GitHub/python_programming/Zadania_Streamlit_Anna_Marjankowska.py