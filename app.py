import streamlit as st

st.title("AI Governance Dashboard")
st.write("LLM Evaluation & Monitoring Platform")

prompt = st.text_input("Enter a prompt:")

if prompt:
    st.write("You entered:", prompt)

