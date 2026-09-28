import streamlit as st

st.title('BMI Calculator')
weight=st.number_input("Enter You're Weight in kg: ",min_value=0)
height=st.number_input("Enter You're Height in cm: ",min_value=0)
button=st.button('BMI')
if button:
    result=(weight/((height/100)**2))
    print(result)
    if result<18.5:
        st.info('You are underweight')
    elif (18.5<=result <25):
        st.success('You are normal')
    elif (25<=result <40):
        st.warning('You are overweight')
    else:
        st.error('You are obesity')
