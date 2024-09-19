# streamlit_app.py
import streamlit as st

# Title of the app
st.title('Basic Streamlit App')

# Sidebar for user input
st.sidebar.title('User Input')
name = st.sidebar.text_input('Enter your name')
age = st.sidebar.slider('Select your age', 1, 100, 25)

# Main content
st.write('Hello, welcome to the app!')
if name:
    st.write(f'Hello, {name}!')

st.write(f'Your age is {age}')

# A simple chart example
st.write('Here is a simple chart:')
chart_data = {
    'Column A': [1, 2, 3],
    'Column B': [10, 20, 30],
    'Column C': [100, 200, 300]
}
st.bar_chart(chart_data)

# Add a button
if st.button('Click me'):
    st.write('Button clicked!')

# Input file uploader
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write(f"You uploaded: {uploaded_file.name}")
