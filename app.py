import streamlit as st

# Title of the app
st.title('My First Streamlit App')

# Display a message
st.write("Hello, Streamlit!")

# Create a slider
slider_value = st.slider('Pick a number', 0, 100)
st.write(f'Slider Value: {slider_value}')
