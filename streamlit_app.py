import streamlit as st

import streamlit as st
name=st.text_input('Enter your name')
btn=st.button('show')
if btn:
  st.write(f'Hello {name}')


# app1
st.header("calculate area")
choose=st.selectbox('choose the shape',['circle'],['rectangle'])
if choose=='circle':
    r=st.number_input('enter the radius',min_value=1.0,max_value=100)
    btn=st.button('calculate')
    if btn:
      area=3.14*r*r
      st.write(f'area of circle is {area}')
elif choose=='rectangle':
    w=st.number_input('enter the radius',min_value=1.0,max_value=100)
    h=st.number_input('enter the radius',min_value=1.0,max_value=100)
    area=h*w
    btn=st.button('calculate')
    if btn:
