import streamlit as st
import pandas as pd
import numpy as np

st.title("🎈 Tarek Khorshed's App 2025")
#st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")


st.write("My first python APP 2025.")
st.write("Now you need to code ya Aloshi")
st.write("Test2")


x = st.slider('x', key="mySLider")  
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="txtName")

# You can access the value at any point with:
st.session_state.txtName
#st.session_state.mySlider


# Session states
if 'key' not in st.session_state:
    st.session_state.key = 'value'

st.session_state.key = 'value2'     # Attribute API
st.session_state['key'] = 'value2'  # Dictionary like API

st.write(st.session_state)




def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)
    st.write(st.session_state.my_textbox)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    textbox_input = st.text_input("Your name", key="my_textbox")
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)



# Sidebar
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)



if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data



df = pd.DataFrame({
  'column1': [1, 2, 3, 4],
  'column2': [10, 20, 30, 40]
})

st.write(df)


# Dynamic table
df2 = np.random.randn(10, 20)
st.dataframe(df2)
#st.dataframe(df2.style.highlight_max(axis=0))

# static table
st.table(df2)  

# Highlight max value in each row
df3 = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df3.style.highlight_max(axis=0))