import openai
import streamlit as st

st.set_page_config(page_title="Mood-to-Quote Generator")
st.title("💬 Mood-to-Quote Generator")

# Let user enter their own OpenAI API key
user_api_key = st.text_input("🔐 Enter your OpenAI API Key", type="password", help="Required to generate quotes")

# Mood input
mood = st.text_input("How are you feeling today?", placeholder="e.g., tired, happy, anxious")

# Submit button
if st.button("Generate Quote"):
    if not user_api_key:
        st.warning("Please enter your OpenAI API key.")
    elif not mood:
        st.warning("Please enter your mood.")
    else:
        try:
            client = openai.OpenAI(api_key=user_api_key)

            with st.spinner("Generating your quote..."):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "user",
                            "content": f"Give a motivational quote for someone feeling {mood}."
                        }
                    ]
                )
                quote = response.choices[0].message.content.strip()
                st.success("Here's your quote!")
                st.write(f"🌟 {quote}")
        except openai.OpenAIError as e:
            st.error("⚠️ Failed to generate quote. Please check your API key or try again later.")

# Optional footer
st.markdown("---")
st.info("🔑 Your API key is not stored. This app only works if your OpenAI account has quota.")
