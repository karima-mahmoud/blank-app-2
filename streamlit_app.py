import streamlit as st

import streamlit as st
name=st.text_input('Enter your name')
btn=st.button('show')
if btn:
  st.write(f'Hello {name}')
