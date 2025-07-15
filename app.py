import streamlit as st
from streamlit.components.v1 import html

# Page config
st.set_page_config(
    page_title="ElevenLabs AI Chat",
    page_icon="🤖",
    layout="centered"
)

# Initialize session state for authentication
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Password check
if not st.session_state.authenticated:
    st.title("🔒 Authentication Required")
    st.markdown("Please enter the password to access the AI Assistant.")
    
    # Password input
    password = st.text_input("Password", type="password", key="password_input")
    
    # Login button
    if st.button("Login", type="primary"):
        if password == "fsworldcup2026":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Incorrect password. Please try again.")
else:
    # Show the main app content only after authentication
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
    
    # Add logout button
    if st.button("Logout", type="secondary"):
        st.session_state.authenticated = False
        st.rerun() 