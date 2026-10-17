from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Análisis de vehículos", layout="wide")

ruta_csv = Path(__file__).parent / "vehicles_us.csv"
car_data = pd.read_csv(ruta_csv)

st.header("Análisis de anuncios de vehículos")

st.write("Explora la lectura del odómetro y los precios de los vehículos.")
st.dataframe(car_data.head())

if st.checkbox("Mostrar histograma del odómetro"):
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        title="Distribución de la lectura del odómetro",
        labels={"odometer": "Lectura del odómetro"}
    )
    st.plotly_chart(fig_hist)

if st.checkbox("Mostrar relación entre odómetro y precio"):
    fig_disp = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Relación entre odómetro y precio",
        labels={
            "odometer": "Lectura del odómetro",
            "price": "Precio en dólares"
        },
        opacity=0.4
    )
    st.plotly_chart(fig_disp)