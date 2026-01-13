import streamlit as st
import pandas as pd
import sqlite3 as sql

# Home page content

st.title("Alei Khorshed - Planning App")
st.write("IBDP - Computer Science - IA")

#st.markdown("# Home 🏠")
st.sidebar.markdown("# Home 🏠")


# Create 3 equal-width columns
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Subject Data"):
        st.switch_page("subject_data.py") 

with col2:
    if st.button("Task Data"):
        st.switch_page("task_data.py") 


with col3:
    if st.button("Goal Planning"):
        st.switch_page("goal_planning.py") 



MyDB = "CS IA DB.db"

# Create DB Connection 
conn = sql.connect(MyDB)

#cur = conn.cursor()
#cur.execute("ALTER TABLE GoalPoints ADD COLUMN description TEXT")
#conn.commit() 

conn.close()
st.rerun()