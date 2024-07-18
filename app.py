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

