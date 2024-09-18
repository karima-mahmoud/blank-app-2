import streamlit as st

import streamlit as st
name=st.text_input('Enter your name')
btn=st.button('show')
if btn:
  st.write(f'Hello {name}')


# app1
area =None
st.header("calculate area")
choose=st.selectbox('choose the shape',['circle'],['rectangle'])
if choose=='circle':
    r=st.number_input('enter the radius',min_value=1.0,max_value=100.0)
    area=3.14*r*r
    btn=st.button('calculate')

elif choose=='rectangle':
    w=st.number_input('enter the width',min_value=1.0,max_value=100.0)
    h=st.number_input('enter the hight',min_value=1.0,max_value=100.0)
    area=h*w
    btn=st.button('calculate')
if btn:
   st.write(f'area  is {area}')
    
      
