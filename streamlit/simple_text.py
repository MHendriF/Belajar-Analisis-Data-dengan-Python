import streamlit as st 
    
st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

st.title('Belajar Analisis Data')
st.header('Pengembangan Dashboard')
st.subheader('Pengembangan Dashboard')
st.caption('Copyright (c) 2023')
code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

st.text('Halo, calon praktisi data masa depan.')
st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")