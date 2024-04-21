import os
import dotenv
import streamlit as st
from typing import Generator
from groq import Groq

dotenv.load_dotenv()

st.set_page_config(page_icon="💬", layout="wide", page_title="Muyakwa ChatBot")

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

icon("🏎️")

st.subheader("Rotz-Schneller Chat-Bot", divider="rainbow", anchor=False)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

# Initialize chat history and selected model
if "messages" not in st.session_state:
    st.session_state.messages = []

# Define model details
model_option = "mixtral-8x7b-32768"

models = {
    "mixtral-8x7b-32768": {
        "name": "Mixtral-8x7b-Instruct-v0.1",
        "tokens": 32768,
        "developer": "Mistral",
    },
}

max_tokens_range = models[model_option]["tokens"]

def reset_context_length():
    st.session_state.messages = []

# Create a column layout
col1, _, _ = st.columns([1, 0.1, 0.1])

with col1:
    # Add a reset context button
    reset_button = st.button(
        "Reset Context Length", on_click=reset_context_length, key="reset_button"
    )

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    avatar = "🤖" if message["role"] == "assistant" else "👨‍💻"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

def generate_chat_responses(chat_completion) -> Generator[str, None, None]:
    """Yield chat response content from the Groq API response."""
    for chunk in chat_completion:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content

if prompt := st.chat_input("Enter your prompt here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user", avatar="👨‍💻"):
        st.markdown(prompt)

    # Add the system message to instruct the model to respond in German
    st.session_state.messages.insert(0, {"role": "system", "content": "Please respond in German."})

    # Fetch response from Groq API
    try:
        chat_completion = client.chat.completions.create(
            model=model_option,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            max_tokens=max_tokens_range,
            stream=True,
        )

        # Use the generator function with st.write_stream
        with st.chat_message("assistant", avatar="🤖"):
            chat_responses_generator = generate_chat_responses(chat_completion)
            full_response = st.write_stream(chat_responses_generator)
    except Exception as e:
        st.error(e, icon="🚨")

    # Append the full response to session_state.messages
    if isinstance(full_response, str):
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )
    else:
        # Handle the case where full_response is not a string
        combined_response = "\n".join(str(item) for item in full_response)
        st.session_state.messages.append(
            {"role": "assistant", "content": combined_response}
        )