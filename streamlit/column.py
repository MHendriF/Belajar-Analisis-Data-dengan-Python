import streamlit as st
    
st.title('Belajar Analisis Data')
col1, col2, col3 = st.columns(3)
    
with col1:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
    
with col2:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
    
with col3:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")


st.title('Belajar Analisis Data 2')
col4, col5, col6 = st.columns([2, 1, 1])
 
with col4:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with col5:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with col6:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")