import streamlit as st
from datetime import date
st.title('Student Registration Form')
name=st.text_input('Name: ')
age=st.number_input('Age: ',min_value=0)
Date=st.date_input('Date Of Birth: ',min_value=date(1990,1,1),max_value=date.today())
Email=st.text_input('Email: ')
gender=st.radio('Gender: ',('Male','Female'))
Course=st.selectbox('Course: ',('Python','Java','Dotnet','Testing'))
bt=st.button('Submit')
if bt:
    st.write('Name: ',name)
    st.write('Age: ',age)
    st.write('Date: ',Date)
    st.write('Email: ',Email)
    st.write('Gender: ',gender)
    st.write('Course: ',Course)