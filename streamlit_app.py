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