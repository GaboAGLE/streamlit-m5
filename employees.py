import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

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


# Función para filtrar los empleados por ciudad
def filtrar_por_ciudad(hometown):
    employees = pd.read_csv(DATA_URL)
    # Filtrar empleados según el nivel educativo seleccionado
    resultado_ciudad = employees[employees['Hometown'] == hometown]
    return resultado_ciudad

# Diseño de la aplicación web con Streamlit

st.sidebar.title("Filtro por Ciudad")

# Obtener las ciudades únicos del DataFrame
hometown = employees['Hometown'].unique()

# Control selectbox en el sidebar para seleccionar el ciudad
ciudad_seleccionado = st.sidebar.selectbox("Seleccionar ciudad", hometown)
st.title("Buscador de Empleados por ciudad")
# Filtrar los empleados por ciudad seleccionado
empleados_ciudad = filtrar_por_ciudad(ciudad_seleccionado)

# Mostrar el DataFrame con los resultados encontrados
st.write("Resultados encontrados:")
st.write(empleados_ciudad)

# Mostrar el total de empleados encontrados
total_empleados_ciudad = len(empleados_ciudad)
st.write(f"Total de empleados encontrados: {total_empleados_ciudad}")



# Función para filtrar los empleados por unit
def filtrar_por_unit(unit):
    employees = pd.read_csv(DATA_URL)
    # Filtrar empleados según el nivel educativo seleccionado
    resultado_unit = employees[employees['Unit'] == unit]
    return resultado_unit

# Diseño de la aplicación web con Streamlit

st.sidebar.title("Filtro por Unit")

# Obtener las ciudades únicos del DataFrame
unit = employees['Unit'].unique()

# Control selectbox en el sidebar para seleccionar unit
unit_seleccionado = st.sidebar.selectbox("Seleccionar unit", unit)
st.title("Buscador de Empleados por unit")
# Filtrar los empleados por unit seleccionado
empleados_unit = filtrar_por_unit(unit_seleccionado)

# Mostrar el DataFrame con los resultados encontrados
st.write("Resultados encontrados:")
st.write(empleados_unit)

# Mostrar el total de empleados encontrados
total_empleados_unit = len(empleados_unit)
st.write(f"Total de empleados encontrados: {total_empleados_unit}")


# Crear el histograma
fig, ax = plt.subplots()
ax.hist(employees['Age'], bins=10)
ax.set_xlabel('Edad')
ax.set_ylabel('Número de Empleados')

# Configurar la visualización con Streamlit
st.title('Histograma de Edades de Empleados')
st.pyplot(fig)


# Calcular frecuencias de las unidades funcionales
frecuencias = employees['Unit'].value_counts()

# Crear gráfico de frecuencias
fig, ax = plt.subplots()
frecuencias.plot(kind='bar', ax=ax)

# Configuración del gráfico
ax.set_title('Frecuencias de Unidades Funcionales')
ax.set_xlabel('Unidad Funcional')
ax.set_ylabel('Número de Empleados')

# Mostrar el gráfico en Streamlit
st.title('Gráfica de frecuencias para las unidades funcionales')
st.pyplot(fig)


# Calcular el índice de deserción por ciudad
employees_by_hometown = employees.groupby('Hometown').mean()
desercion_por_ciudad = employees.groupby('Hometown')['Attrition_rate'].mean().sort_values(ascending=True)

# Crear gráfico de barras horizontales
fig, ax = plt.subplots()
desercion_por_ciudad.plot(kind='bar', ax=ax)

# Configuración del gráfico
ax.set_title('Índice de Deserción por Ciudad')
ax.set_xlabel('Ciudad')
ax.set_ylabel('Índice de Deserción')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)


# Crear gráfico de dispersión

fig, ax = plt.subplots()
ax.scatter(employees['Age'], employees['Attrition_rate'], alpha=0.5)

# Configuración del gráfico
sns.scatterplot(y=employees['Attrition_rate'],x=employees['Age'])

# Mostrar el gráfico en Streamlit
st.pyplot(fig)


# Crear gráfico de dispersión
fig, ax = plt.subplots()
ax.scatter(employees['Time_of_service'], employees['Attrition_rate'], alpha=0.5)

# Configuración del gráfico
ax.set_title('Tiempo de Servicio vs Tasa de Deserción')
ax.set_xlabel('Tiempo de Servicio')
ax.set_ylabel('Tasa de Deserción')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)