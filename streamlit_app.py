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

# العنوان
st.header('رفع ملف')

# رفع الملف
uploaded_file = st.file_uploader("اختر ملف", type=["csv", "txt", "pdf", "jpg", "png"])

# التحقق إذا كان هناك ملف مرفوع
if uploaded_file is not None:
    # عرض بعض المعلومات عن الملف
    st.write(f"اسم الملف: {uploaded_file.name}")
    st.write(f"نوع الملف: {uploaded_file.type}")
    st.write(f"حجم الملف: {uploaded_file.size} bytes")
    
    # إذا كان الملف نصي (csv أو txt)، عرض محتوياته
    if uploaded_file.type == "text/csv" or uploaded_file.type == "text/plain":
        file_content = uploaded_file.read().decode("utf-8")
        st.text(file_content)

    # إذا كان الملف صورة، عرضها
    elif uploaded_file.type in ["image/jpeg", "image/png"]:
        st.image(uploaded_file, caption="الصورة التي تم رفعها", use_column_width=True)

