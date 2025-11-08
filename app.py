# Importar las librerías necesarias
import streamlit as st
import pandas as pd
import plotly.express as px

# --- Carga de Datos ---
# Leer el archivo CSV en un DataFrame
# Se asume que vehicles_us.csv está en el mismo directorio que app.py
try:
    car_data = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("Error: El archivo 'vehicles_us.csv' no fue encontrado. Asegúrate de que esté en la raíz del proyecto.")
    st.stop() # Detener la ejecución si no se encuentran los datos

# Rellenar valores nulos para columnas clave que usaremos en las visualizaciones
# Esto es una buena práctica antes de visualizar
car_data['model_year'] = car_data['model_year'].fillna(car_data['model_year'].median())
car_data['cylinders'] = car_data['cylinders'].fillna(0) # Usar 0 para nulos
car_data['odometer'] = car_data['odometer'].fillna(car_data['odometer'].median())


# --- Estructura de la Aplicación Streamlit ---

# 1. Encabezado principal
st.header('Dashboard de Análisis de Anuncios de Venta de Coches')
st.markdown('Esta aplicación te permite explorar la distribución de las variables clave y la relación entre el precio y el millaje (odometer).')

# 2. Casillas de verificación para activar gráficos
st.subheader('Selecciona los gráficos que deseas visualizar:')

# Creamos las casillas de verificación
build_histogram = st.checkbox('Construir un Histograma de Millaje (Odometer)')
build_scatter = st.checkbox('Construir un Gráfico de Dispersión (Precio vs. Millaje)')

# 3. Lógica Condicional para el Histograma (Botón 1)
if build_histogram:
    # Escribir un mensaje en la aplicación
    st.write('Distribución del Millaje (Odometer)')

    # Crear el histograma utilizando Plotly Express
    # Usamos Plotly Express ya que es más conciso y tiene valores predeterminados razonables
    fig_hist = px.histogram(car_data, 
                            x='odometer', 
                            title='Distribución de Millaje (Odometer)',
                            labels={'odometer': 'Millaje (Odometer)'},
                            color_discrete_sequence=['#4287f5']) # Color para mejor estética
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# 4. Lógica Condicional para el Gráfico de Dispersión (Botón 2)
if build_scatter:
    # Escribir un mensaje en la aplicación
    st.write('Relación entre el Precio del Coche y el Millaje (Odometer)')

    # Crear el gráfico de dispersión utilizando Plotly Express
    fig_scatter = px.scatter(car_data, 
                             x='odometer', 
                             y='price',
                             title='Precio vs. Millaje',
                             labels={'odometer': 'Millaje', 'price': 'Precio ($)'},
                             hover_data=['model_year', 'condition']) # Mostrar datos adicionales al pasar el ratón
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)

st.info("Nota: Los gráficos se construyen en tiempo real utilizando Plotly y Streamlit.")