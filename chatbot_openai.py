import streamlit as st
import google.generativeai as genai

API_KEY = "YOUR_API_KEY_HERE"
PAGE_TITLE = "Chat with Kim"
PAGE_ICON = ":robot:"
MODEL_NAME = 'gemini-pro'
INSTRUCTION = "In this chat, respond as if you're explaining things to a five-year-old child. "

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.title(PAGE_TITLE)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "genai_configured" not in st.session_state:
    st.session_state.genai_configured = False

def configure_genai():
    try:
        genai.configure(api_key=API_KEY)
        st.session_state.genai_configured = True
        st.success("Generative AI client configured successfully!")
    except Exception as e:
        st.error(f"Error configuring Generative AI: {e}")

def clear_chat_history():
    st.session_state.chat_history = []

if not st.session_state.genai_configured:
    configure_genai()

if st.session_state.genai_configured:
    model = genai.GenerativeModel(MODEL_NAME)
    chat = model.start_chat(history=[])

    user_input = st.text_input(
        "Ask Kim a question (explain things like I'm 5!):",
        key="user_input"
    )

    if user_input:
        with st.spinner("Kim is thinking..."):
            response = chat.send_message(INSTRUCTION + user_input)
        st.session_state.chat_history.append({"you": user_input, "bot": response.text})

    chat_container = st.container()
    with chat_container:
        for message in st.session_state.chat_history:
            st.markdown(f"**You:** {message['you']}")
            st.markdown(f"**Kim:** {message['bot']}")
            st.markdown("---")

    st.button("Clear Chat History", on_click=clear_chat_history)

else:
    st.warning("Generative AI is not configured. Please check your API key.")
