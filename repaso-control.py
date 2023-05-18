import streamlit as st
import datetime 
import pandas as pd
#control de un calendario
today = datetime.date.today()
today_date = st.sidebar.date_input('Current date', today)
st.success('Current date: `%s`' % (today_date))

titanic_link ='https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
titanic_data = pd.read_csv(titanic_link)
# Display the content of the dataset if checkbox is true
st.header("Dataset")
agree = st.checkbox("show DataSet Overview ? ")
if agree:
    st.dataframe(titanic_data)

#radio

selected_class = st.sidebar.radio("Select Class",
titanic_data['class'].unique())
st.write("Selected Class:", selected_class)

selected_sex = st.selectbox("Select Sex", titanic_data['sex'].unique())
st.write(f"Selected Option: {selected_sex!r}")


optionals = st.expander("Optional Configurations", True)
fare_select = optionals.slider(
    "Select the Fare",
        min_value=float(titanic_data['fare'].min()),
        max_value=float(titanic_data['fare'].max())
)


subset_fare = titanic_data[(titanic_data['fare'] >= fare_select)]
st.write(f"Number of Records With this Fare {fare_select}:{subset_fare.shape[0]}")
