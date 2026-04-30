import streamlit as st
from chatbot import generate_response, build_messages
from memory import initialize_memory, add_user_message, add_assistant_message

st.set_page_config(page_title="Medical AI Assistant")

st.title("🧠 Medical AI Learning Assistant")

initialize_memory(st.session_state)

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Ask about anatomy, physiology, or biochemistry...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.write(user_input)

    add_user_message(st.session_state, user_input)

    # Build messages with context
    messages = build_messages(st.session_state.messages)

    # Generate response
    reply = generate_response(messages)

    # Show assistant reply
    with st.chat_message("assistant"):
        st.write(reply)

    add_assistant_message(st.session_state, reply)
