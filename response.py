import time
import streamlit as st


def countdown(duration_days, duration_hours, duration_minutes):

  total_seconds = duration_days * 86400 + duration_hours * 3600 + duration_minutes * 60
  start_time = time.time()
  end_time = start_time + total_seconds

timer_placeholder = st.empty()

  while time.time() < end_time:
    remaining_time = int(end_time - time.time())
    days, remainder1 = divmod(remaining_time, 86400)
    hours, remainder2 = divmod(remainder1, 3600)
    mins, secs = divmod(remainder2, 60)
    timer = '{:02d}:{:02d}:{:02d}:{:02d}'.format(days,hours, mins, secs)

    timer_placeholder.title(timer)
    time.sleep(0)
    time.sleep(1)

audio_path = 'mixkit-vintage-warning-alarm-990.wav'
st.audio(audio_path, autoplay = True)
timer_placeholder.title("Time's up!")
  
