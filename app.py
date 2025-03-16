import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"
st.set_page_config(page_title="Elysia AI - Emotion Chat", page_icon="💬", layout="wide")

st.markdown("""
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #2E2E2E;
            color: white;
        }
        h1 {
            color: #4CAF50;
        }
        .stTextInput, .stButton, .stTextArea {
            font-family: 'Inter', sans-serif;
        }
        .stTextInput>div>div>input {
            background-color: #3A3A3A;
            color: white;
            border-radius: 5px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []


st.markdown("""
    <h1 style='text-align: center;'>💬 Elysia AI - Emotion Detection Chat</h1>
    <p style='text-align: center;'>Type your message below and detect the emotion in real-time!</p>
""", unsafe_allow_html=True)

with st.container():
    chat_container = st.container()
    for msg in st.session_state.messages:
        role = msg["role"]
        content = msg["content"]
        if role == "user":
            chat_container.markdown(f"""
                <div style="text-align: right;color: black; padding: 8px; margin: 5px; background-color: #4CAF50; border-radius: 10px;">
                    {content}
                </div>
            """, unsafe_allow_html=True)
        else:
            chat_container.markdown(f"""
                <div style="text-align: left; padding: 8px;color: black; margin: 5px; background-color: #8F8F8F; border-radius: 10px;">
                    <strong>Emotion:</strong> {content}
                </div>
            """, unsafe_allow_html=True)

with st.form(key="chat_form", clear_on_submit=True):
    col1, col2 = st.columns([10, 1])

    user_input = col1.text_input("You:", placeholder="Type your message here...", label_visibility="collapsed")
    submit_button = col2.form_submit_button("➡️")

if submit_button and user_input.strip() != "":
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = requests.post(API_URL, json={"text": user_input})
        response.raise_for_status()
        emotion = response.json().get("emotions", ["Unknown"])

    except Exception as e:
        emotion = "Error detecting emotion!"

    st.session_state.messages.append({"role": "assistant", "content": emotion})
    st.rerun()
