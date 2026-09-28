import streamlit as st
st.title('Read book Record')
from Library_db import BookListCreateRetrieveUpdateDelete
b=BookListCreateRetrieveUpdateDelete()
result=b.list()
st.table(result)