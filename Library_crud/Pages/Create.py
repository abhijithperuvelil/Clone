import streamlit as st
from Library_db import BookListCreateRetrieveUpdateDelete

st.title('Add new Book Record')
import streamlit as st
st.title('Welcome to Library App')
title=st.text_input("Enter the Book Title")
author=st.text_input("Enter the Author Name")
price=st.number_input("Enter the Book Price")
page=st.number_input("Enter the Page Number")
language=st.text_input("Enter the Language")
bt=st.button("Add Book")
if bt:
    st.write("Title: ",title)
    st.write(f"Author: ",author)
    st.write(f"Price: ",price)
    st.write(f"Page: ",page)
    st.write(f"Language: ",language)

    b=BookListCreateRetrieveUpdateDelete()
    b.create(title=title,author=author,price=price,pages=page,language=language)
    st.success("Record Added Successfully")