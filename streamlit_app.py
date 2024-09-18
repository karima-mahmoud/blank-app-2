import streamlit as st

# Input for name
name = st.text_input('Enter your name')
show_btn = st.button('Show')
if show_btn:
    st.write(f'Hello {name}')

# App1: Area calculation
st.header("Calculate Area")
shape = st.selectbox('Choose the shape', ['circle', 'rectangle'])

if shape == 'circle':
    r = st.number_input('Enter the radius', min_value=1.0, max_value=100.0)
    circle_btn = st.button('Calculate Circle Area')
    if circle_btn:
        area = 3.14 * r * r
        st.write(f'The area of the circle is {area}')

elif shape == 'rectangle':
    w = st.number_input('Enter the width', min_value=1.0, max_value=100.0)
    h = st.number_input('Enter the height', min_value=1.0, max_value=100.0)
    rect_btn = st.button('Calculate Rectangle Area')
    if rect_btn:
        area = w * h
        st.write(f'The area of the rectangle is {area}')


#app2
import streamlit as st
import pandas as pd

st.header('File Upload App')
file = st.file_uploader('Upload file', type=['csv'])

if file is not None:
    df = pd.read_csv(file)
    st.write(df)
    
    num_row = st.slider('Choose num rows', min_value=1, max_value=len(df))
    names_columns = st.multiselect('Choose names of columns', df.columns.tolist())

    if names_columns:
        st.write(df[:num_row][names_columns])
    else:
        st.write(df[:num_row])


num_row = st.slider('choose num rows', min_value=1, max_value=len(df), step=1)
names_column = st.multiselect('choose names of columns', df.columns.to_list())
st.write(df[:num_row][names_column])

if names_column:
    st.write(df[:num_row][names_column])
else:
    st.write(df[:num_row])

num_col = df.select_dtypes(include='number').columns.to_list()

color = st.selectbox('choose color', df.columns.to_list())

fig = px.scatter(df, x=x_col, y=y_col, color=color)
st.plotly_chart(fig)
