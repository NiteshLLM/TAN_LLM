# app.py
import streamlit as st
import streamlit.components.v1 as components

st.title("Hello Streamlit!")
st.write("This is a simple Streamlit app.")
st.write("You can deploy it on Streamlit Cloud!")

# Add an input box and a button
name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write(f"Hello, {name}!")

# Embed the chatbot
chatbot_html = """
<script>
window.embeddedChatbotConfig = {
    chatbotId: "fsSeMDx7lQ0ZkDeR16T8V",
    domain: "www.chatbase.co"
}
</script>
<script
src="https://www.chatbase.co/embed.min.js"
chatbotId="fsSeMDx7lQ0ZkDeR16T8V"
domain="www.chatbase.co"
defer>
</script>
"""

# Use st.components.v1.html to embed the chatbot
components.html(chatbot_html, height=600)
