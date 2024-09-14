# app.py
import streamlit as st
import streamlit.components.v1 as components

# Set page configuration for a cleaner layout
st.set_page_config(page_title="Chatbot Web App", layout="centered")

# Add a custom CSS to style the app
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;
    }
    .main-title {
        font-size: 3em;
        color: #4CAF50;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .description {
        text-align: center;
        font-size: 1.2em;
        color: #555;
        margin-bottom: 50px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Big heading
st.markdown('<h1 class="main-title">Welcome to the Chatbot App!</h1>', unsafe_allow_html=True)
st.markdown('<p class="description">Interact with our AI-powered chatbot below and get instant responses.</p>', unsafe_allow_html=True)

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
