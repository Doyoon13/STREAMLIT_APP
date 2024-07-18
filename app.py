import streamlit as st

# Imports the functions we coded above
from response import *
from header import *

# Create the header
create_header()

days = st.number_input('Days:')
hours = st.number_input('Hours:')
minutes = st.number_input('Minutes:')
if st.button('Start Timer'):
    countdown(days, hours, minutes)
elif st.button('Reset Timer'):
    countdown(0,0,0)

title_placeholder = st.empty()

Timer_placeholder = st.empty()
