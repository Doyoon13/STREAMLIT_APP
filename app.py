import streamlit as st

# Imports the functions we coded above
from response import *
from header import *

# Create the header
create_header()


days = st.number_input('Days:')
hours = st.number_input('Hours:')
minutes = st.number_input('Minutes:')

col1, col2 = st.columns(2)

with col1:
  if st.button('Start Timer'):
    st.session_state['remaining_time'] = days * 86400 + hours * 3600 + minutes * 60
    
with col2:
  if st.button('Reset Timer'):
    st.session_state['remaining_time'] = 0

if st.session_state['remaining_time'] > 0:
  countdown(0, 0, st.session_state['remaining_time'])

title_placeholder = st.empty()

Timer_placeholder = st.empty()
