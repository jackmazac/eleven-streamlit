import streamlit as st
from streamlit.components.v1 import html

# Page config
st.set_page_config(
    page_title="ElevenLabs AI Chat",
    page_icon="🤖",
    layout="centered"
)

st.title("Chat with ElevenLabs AI Assistant")
st.markdown("Interact with the AI assistant using voice or text.")

# ElevenLabs widget embed code
widget_html = """
<elevenlabs-convai 
    agent-id="agent_01jyj2mn17e2jvdqkmrh6jzfd1"
    variant="expanded"
></elevenlabs-convai>
<script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
"""

# Render the widget
html(widget_html, height=600, scrolling=False) 