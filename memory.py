def initialize_memory(session_state):
    if "messages" not in session_state:
        session_state.messages = []


def add_user_message(session_state, user_input):
    session_state.messages.append({
        "role": "user",
        "content": user_input
    })


def add_assistant_message(session_state, reply):
    session_state.messages.append({
        "role": "assistant",
        "content": reply
    })
