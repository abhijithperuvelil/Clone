import streamlit as st
name=st.text_input('Enter your Name')
age=st.text_input('Enter your Age')
place=st.text_input('Enter Your Place')
gender=st.radio('Select Gender',['Male','Female'])
qualifications=st.selectbox('Select Qualifications',['BBA','BCA','B.TECH'])
b=st.button('Submit')
if b:
    st.title('User Info')
    st.write('Name: ',name)
    st.write('Age: ',age)
    st.write('Place: ',place)
    st.write('Gender: ',gender)
    st.write('Qualification: ',qualifications)
