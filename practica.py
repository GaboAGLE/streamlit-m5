import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

@st.cache
def load_data(nrows):
    data = pd.read_csv('movies.csv', nrows=nrows)
    return data

@st.cache
def load_data_myname(myname):
    data = pd.read_csv('movies.csv')
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    filtered_data_byname = data[data['name'].str.contains(myname)]
    return filtered_data_byname

data = load_data(500)
#st.dataframe(data)
sidebar = st.sidebar
st.header("Movies")
agree = st.sidebar.checkbox("show DataSet Overview ? ")
if agree:
    st.dataframe(data)

myname = st.sidebar.text_input("Ingresa filme :")

if (myname):
    filterbyname = load_data_myname(myname)
    count_row = filterbyname.shape[0]
    st.write(f"Total names : {count_row}")

    st.dataframe(filterbyname)


