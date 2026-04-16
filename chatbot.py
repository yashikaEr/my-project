import streamlit as st

st.title("🤖 My Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

def get_response(user_input):
    user_input = user_input.lower()

    if "hi" in user_input or "hello" in user_input:
        return "Hello! How can I help you?"
    elif "fees" in user_input:
        return "The fees is ₹5000."
    elif "timing" in user_input:
        return "Timing is 9 AM to 5 PM."
    elif "contact" in user_input:
        return "You can contact us at 9876543210."
    else:
        return "Sorry, I didn't understand."

user_input = st.text_input("Type your message:")

if user_input:
    st.session_state.messages.append(("You", user_input))
    bot_reply = get_response(user_input)
    st.session_state.messages.append(("Bot", bot_reply))

for sender, msg in st.session_state.messages:
    if sender == "You":
        st.write(f"🧑 {msg}")
    else:
        st.write(f"🤖 {msg}")
