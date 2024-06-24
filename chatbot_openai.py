import streamlit as st
import google.generativeai as genai

API_KEY = "AIzaSyCkC_rt82O1YZ14gTwaWr7a34nSiOAr-nA"
import streamlit as st


st.set_page_config(
    page_title="Chat with Kim",
    page_icon=":robot:", 
)

st.title("Chat with Kim")


def configure_genai():
  """Configures the Generative AI client with the provided API key."""
  try:
    genai.configure(api_key=API_KEY)
    st.success("Generative AI client configured successfully!")
  except Exception as e:
    st.error(f"Error configuring Generative AI: {e}")



if "genai_configured" not in st.session_state:
  configure_genai()
  st.session_state["genai_configured"] = True
  st.session_state["chat_history"] = []  


if st.session_state["genai_configured"]:
  model = genai.GenerativeModel('gemini-pro')
  chat = model.start_chat(history=[])

  instruction = "In this chat, respond as if you're explaining things to a five-year-old child"

  
  user_input = st.text_input(
      "Ask Kim a question (explain things like I'm 5!):", key="user_input"
  )

  if user_input:
    response = chat.send_message(instruction + user_input)
    st.session_state["chat_history"].append({"you": user_input, "bot": response.text})

   
    chat_container = st.container()
    chat_container.markdown(
        """<style>
        .chat-container {
          background-color: #f0f0f0;
          padding: 10px;
          border-radius: 5px;
        }
        .you {
          font-weight: bold;
          color: white;
        }
        .bot {
          font-weight: bold;
          color: #FFBA00;
        }
        </style>""",
        unsafe_allow_html=True,
    )
    with chat_container:
      for message in st.session_state["chat_history"]:
        st.write(f"<div class='you'>**You: {message['you']}</div>", unsafe_allow_html=True)
        st.write(f"<div class='bot'>**Kim: {message['bot']}</div>", unsafe_allow_html=True)
        st.write("<br>", unsafe_allow_html=True)

 
    st.write("---")
    st.button("Clear Chat History", on_click=st.session_state.clear)

