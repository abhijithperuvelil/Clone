import streamlit as st
st.title('Multiplication')
num1=st.number_input('Enter the number 1: ',min_value=0)
print(num1)
num2=st.number_input('Enter the second number 2: ',min_value=0)
print(num2)
btn=st.button('Multiplication')

if btn:
    result=num1*num2
    print(result)
    st.write('Product: ',result)