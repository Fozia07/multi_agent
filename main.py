from agent import myAgent
import streamlit as st
import asyncio


from agent import myAgent
import streamlit as st

st.title("Agent Management System")

# Show initial welcome message
if "chat_started" not in st.session_state:
    st.session_state.chat_started = True
    st.write("Welcome to the Agent Management System! How can I assist you today?")

# Input box
user_input = st.text_input("Enter your query:")

# Handle input and call agent
if user_input:
    with st.spinner("Thinking..."):
        response = asyncio.run(myAgent(user_input))  
    st.write("🤖:", response)