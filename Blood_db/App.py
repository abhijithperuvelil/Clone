import streamlit as st
from blood_donor import bloodDonor
tab1,tab2,tab3,tab4,tab5=st.tabs(['New','Read','Update','Retrieve','Delete'])
with  tab1:
    st.title('New Registration')
    name=st.text_input('Enter your name')
    blood=st.text_input('Enter your blood group')
    phn=st.text_input('Enter your phone number')
    city=st.text_input('Enter your City')
    date=st.text_input('Enter your Last donation date')
    btn=st.button('Submit')
    if btn:
        c=bloodDonor()
        c.post(name=name,bloodgroup=blood,phone=phn,city=city,last_donation=date)
        st.success('Your blood donor Account has been successfully created')

with tab2:
    st.title('Read Detials')
    id=st.number_input('Enter youre id',min_value=1,max_value=100)
    bt=st.button('Read Details')
    if bt:
        c=bloodDonor()
        result=c.get(id=id)
        st.write('Name',result[1])
        st.write('Blood Group',result[2])
        st.write('Phone Number',result[3])
        st.write('City',result[4])
        st.write('Last Donation',result[5])

with tab3:
    st.title('Update Details')
    donor_id=st.number_input('Enter Donors id',min_value=0)
    name=st.text_input('Enter the Donor name')
    blood=st.text_input("Enter Donor blood group")
    phn=st.text_input('Enter Donor phone number')
    city=st.text_input('Enter Donor City')
    date=st.text_input('Enter Donor Last donation date')
    bt=st.button('Update Details')
    if bt:
        c=bloodDonor()
        c.put(name=name,bloodgroup=blood,phone=phn,city=city,last_donation=date,id=donor_id)
        st.success('Your blood donor Account has been successfully updated')


with tab4:
    st.title('Retrieve Details')
    id=st.number_input('Enter youre id')
    bt=st.button('Retrieve Details')
    if bt:
        b=bloodDonor()
        result=c.get_id(id=id)
        st.write('Name',result[1])
        st.write('Blood Group',result[2])
        st.write('Phone Number',result[3])
        st.write('City',result[4])
        st.write('Last Donation',result[5])

with tab5:
    st.title('Delete Donor Details')
    id=st.number_input('Enter your id')
    bt=st.button('Delete Details')
    if bt:
        a=bloodDonor()
        a.delete(id=id)
        st.success('Your blood donor Account has been successfully deleted')
''