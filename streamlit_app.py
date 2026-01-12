import streamlit as st
import pandas as pd
import numpy as np

import sqlite3 as sql


st.title("🎈 Tarek Khorshed's App 2025")
st.write("Test2")


MyDB = "CS IA DB.db"

# Create DB Connection 
conn = sql.connect(MyDB)


with st.form("data_form"):
    title = st.text_input("Subject Title")
    id = st.number_input("id", min_value=0, max_value=120)
    submit = st.form_submit_button("Save")
    
    if submit:
        # Create a DataFrame for the new record
        data_record = [{"title": [title], "id": [id]}]
        df_data = pd.DataFrame(data_record)
        
        # Write to SQLite
        # 'append' adds to the table; 'replace' would overwrite it        
        #df_data.to_sql("Subject", conn, if_exists="append", index=False)
        #conn.close()


        cur = conn.cursor()


        cur.executemany("INSERT INTO Subject VALUES(:subject_id, title)", data_record)
        conn.commit() 
        




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