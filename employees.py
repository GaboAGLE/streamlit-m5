import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title('DSA05 Reto | Mi Plan de aplicación: Aplicación web de Ciencia de Datos')
st.header('Desarrollado por: Gabriel Aguilar López Escalera')
st.write('El siguiente trabajo consiste en complementar el análisis de datos con la representación en un dashboard usando Streamlit de manera eficiente y atractiva para un usuario final.')
DATA_URL = ('Employees.csv')

@st.cache
def load_data(nrows):
    employees = pd.read_csv(DATA_URL, nrows=nrows)
    return employees

employees = load_data(500)

sidebar = st.sidebar
st.sidebar.header('Información')
agree = st.sidebar.checkbox("Mostarar dataframe Employees")
if agree:
    st.dataframe(employees)



@st.cache
def buscar_empleados(empleado_id, ciudad, unidad):
    # Filtrar los empleados según los criterios de búsqueda
    employees = pd.read_csv(DATA_URL)
    resultado = employees[
        (employees['Employee_ID'] == empleado_id) |
        (employees['Hometown'] == ciudad) |
        (employees['Unit'] == unidad)
    ]
    return resultado


# Diseño de la aplicación web con Streamlit
st.title("Buscador de Empleados")
st.write("Ingrese los criterios de búsqueda:")

# Cajas de texto para ingresar los criterios de búsqueda
empleado_id = st.text_input("Employee ID")
ciudad = st.text_input("Hometown")
unidad = st.text_input("Unit")

# Botón para realizar la búsqueda
if st.button("Buscar"):
    # Llamar a la función para buscar empleados
    resultados = buscar_empleados(empleado_id, ciudad, unidad)

    # Mostrar el DataFrame con los resultados encontrados
    st.write("Resultados encontrados:")
    st.write(resultados)

    # Mostrar el total de empleados encontrados
    total_empleados = len(resultados)
    st.write(f"Total de empleados encontrados: {total_empleados}")



# Función para filtrar los empleados por nivel educativo
def filtrar_por_nivel(nivel):
    employees = pd.read_csv(DATA_URL)
    # Filtrar empleados según el nivel educativo seleccionado
    resultado_nivel = employees[employees['Education_Level'] == nivel]
    return resultado_nivel


# Diseño de la aplicación web con Streamlit

st.sidebar.title("Filtro por Nivel Educativo")

# Obtener los niveles educativos únicos del DataFrame
niveles_educativos = employees['Education_Level'].unique()

# Control selectbox en el sidebar para seleccionar el nivel educativo
nivel_seleccionado = st.sidebar.selectbox("Seleccionar Nivel Educativo", niveles_educativos)
st.title("Buscador de Empleados por nivel educativo")
# Filtrar los empleados por el nivel educativo seleccionado
empleados_filtrados = filtrar_por_nivel(nivel_seleccionado)

# Mostrar el DataFrame con los resultados encontrados
st.write("Resultados encontrados:")
st.write(empleados_filtrados)

# Mostrar el total de empleados encontrados
total_empleados_nivel = len(empleados_filtrados)
st.write(f"Total de empleados encontrados: {total_empleados_nivel}")