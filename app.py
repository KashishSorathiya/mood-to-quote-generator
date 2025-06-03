import openai
import streamlit as st
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Mood-to-Quote Generator")
st.title("💬 Mood-to-Quote Generator")

mood = st.text_input("How are you feeling today?")

if st.button("Generate Quote"):
    if mood:
        with st.spinner("Generating..."):
            client = openai.OpenAI()  # 🔁 new client interface
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": f"Give me a motivational quote for someone feeling {mood}."}
                ]
            )
            st.success("Here's your quote!")
            st.write(f"🌟 {response.choices[0].message.content.strip()}")
    else:
        st.warning("Please enter a mood.")
