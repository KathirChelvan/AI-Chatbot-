# Chat with Kim

Welcome to the "Chat with Kim" AI chatbot! This application uses Streamlit and Google Generative AI to create an interactive chatbot that explains concepts in simple terms, as if to a five-year-old child.

## Features

- Interactive chat interface.
- Responses are simplified for easy understanding.
- Maintains chat history for the session.
- Clear chat history with a button click.

## Live Demo

You can access the live demo of the chatbot [here](https://7yh5yrvd2g9enlod8bpcj5.streamlit.app/).

## Installation

To run this application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/KathirChelvan/AI-Chatbot-.git
   cd AI-Chatbot-
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Usage

Once the application is running, you can interact with Kim by typing questions into the text input field. The responses will be simplified to make them easy to understand.

## Code Explanation

```python
import streamlit as st
import google.generativeai as genai

API_KEY = "YOUR_API_KEY_HERE"

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
```

## Configuration

Make sure to replace `"YOUR_API_KEY_HERE"` with your actual API key from Google Generative AI.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://ai.google/tools/)

---

Feel free to explore the code, use it, and contribute to the project. Enjoy chatting with Kim!
