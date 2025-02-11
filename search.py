import streamlit as st
from langchain_groq import ChatGroq
llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0.2,
    groq_api_key="your api key here"
)



st.title("simple LLM Chatbot")
st.write("Enter your query below:")
user__input = st.text_input("Your Question:","")


if st.button("Get Answer"):
    response = llm.invoke(user__input)
    st.write("### Response:")
    st.write(response.content)