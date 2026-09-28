import streamlit as st
from Library_db import BookListCreateRetrieveUpdateDelete
st.title("Update Book Record")
id=st.number_input("Enter Book ID")
title=st.text_input("Enter the Book Title")
author=st.text_input("Enter the Author Name")
price=st.number_input("Enter the Book Price")
page=st.number_input("Enter the Page Number")
language=st.text_input("Enter the Language")
bt=st.button("Update")

if bt:
    c=BookListCreateRetrieveUpdateDelete()
    records=c.update(id,title,author,price,page,language)
    if records:
        st.success("Book Updated Successfully")
    else:
        st.error("Book Not Found")