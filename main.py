import streamlit as st
from langchain_helper import *

st.set_page_config(
    page_title = 'Database Query Tool',
    page_icon="🛢"
)

st.title('T-Shirts 👕 Sales Chatbot')
st.image('db_schema.png')
question = st.text_input('Question: ')
if question:
    with st.spinner("Thinking ..."):
        answer = get_response(question)
    st.header("Answer")
    st.write(answer)
