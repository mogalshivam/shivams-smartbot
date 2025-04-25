import streamlit as st
import openai

# Load API Key securely
openai.api_key = st.secrets["openai"]["api_key"]

st.title("Shivam's SmartBot")

user_input = st.text_input("You: ", "")

if user_input:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    bot_reply = response['choices'][0]['message']['content']
    st.write("Bot:", bot_reply)