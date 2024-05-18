import streamlit as st 


st.title('My First Streamlit App') 
st.write('Welcome to my Streamlit app!') 
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 
st.write('Customized Message:',widgetuser_input)