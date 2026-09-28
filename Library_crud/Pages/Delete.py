import streamlit as st
st.title('Delete Book Record')

from Library_db import BookListCreateRetrieveUpdateDelete

id=st.number_input("Enter Book Id: ")
btn=st.button("Delete Book Record")
if btn:
        c=BookListCreateRetrieveUpdateDelete()
        c.delete(id)
        st.success("Book Deleted Successfully")