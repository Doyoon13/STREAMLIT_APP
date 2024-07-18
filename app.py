import streamlit as st
import sqlite3

# Imports the functions we coded above
from response import *
from header import *

# Create the header
create_header()

hours = st.number_input('Hours:')
minutes = st.number_input('Minutes:')
if st.button('Start Timer'):
    countdown(hours, minutes)

title_placeholder = st.empty()

Timer_placeholder = st.empty()

@st.cache
def count_visitor():
 conn = sqlite3.connect("/path/to/database.db")
 cur = conn.cursor()
 cur.execute("UPDATE name_of_table SET total_visitors = total_visitors + " + str(1))
 conn.commit()
 conn.close()

count_visitor()
