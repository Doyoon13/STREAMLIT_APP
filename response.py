import time
import streamlit as st
import librosa

def countdown(duration_hours, duration_minutes):
  total_seconds = duration_hours * 3600 + duration_minutes * 60
  start_time = time.time()
  end_time = start_time + total_seconds

  timer_placeholder = st.empty()

  while time.time() < end_time:
    remaining_time = int(end_time - time.time())
    hours, remainder = divmod(remaining_time, 3600)
    mins, secs = divmod(remainder, 60)
    timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)

    timer_placeholder.title(timer)

    time.sleep(1)

  timer_placeholder.title("Time's up!")
  audio_path = '/content/mixkit-vintage-warning-alarm-990.wav'
  st.audio(audio_path, autoplay = True)
