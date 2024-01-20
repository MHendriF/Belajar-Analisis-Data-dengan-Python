import datetime
import streamlit as st
import pandas as pd

# Text input
name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)

# Text area
text = st.text_area('Feedback')
st.write('Feedback: ', text)

# Number input
number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')

# Date input
date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)

# File upload
uploaded_file = st.file_uploader('Choose a CSV file')
 
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

# Camera input
picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)