import streamlit as st 

# Init Session States
st.session_state.gCurrentUser = 2
st.session_state.gDateFormat = "DD/MM/YYYY"


# Define the pages
home_page = st.Page("home.py", title="Home", icon="🏠", default=True)
subject_page = st.Page("subject_data.py", title="Subject Data", icon="➕")
task_page = st.Page("task_data.py", title="Task Data", icon="📊")
goal_planning = st.Page("goal_planning.py", title="Goal Planning", icon="➕")


# Set up navigation
pg = st.navigation([home_page, subject_page, task_page,goal_planning])

# Run the selected page
pg.run()



