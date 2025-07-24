import streamlit as st
from streamlit.components.v1 import html
import base64
from pathlib import Path

# Function to load and encode image to Base64
@st.cache_data
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

# Page config
st.set_page_config(
    page_title="Cleetus AI",
    page_icon="🦊",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- BACKGROUND IMAGE ---
bg_image_path = str(Path(__file__).parent / "assets/world-cup.jpg")
encoded_bg_image = get_base64_of_bin_file(bg_image_path)

if encoded_bg_image:
    background_css = f"""
    <style>
    .stApp {{
        background: linear-gradient(to bottom, rgba(0, 21, 41, 0.6), rgba(0, 0, 0, 0.9));
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        left: 0;
        right: 0;
        top: 0;
        bottom: 0;
        z-index: -1;
        background-image: url("data:image/jpeg;base64,{encoded_bg_image}");
        background-size: cover;
        background-position: center;
        filter: blur(4px) brightness(0.6);
        -webkit-filter: blur(4px) brightness(0.6);
        transform: scale(1.1);
    }}
    </style>
    """
    st.markdown(background_css, unsafe_allow_html=True)
else:
    st.warning("Background image not found. Please ensure 'assets/world-cup.jpg' exists.")


# Custom CSS for Fox Sports branding
st.markdown("""
<style>
    /* Hide Streamlit branding and menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
        
    /* Login container styling */
    .login-container {
        background-color: #003366;
        padding: 3rem 2rem;
        border-radius: 10px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
        margin-top: 2rem;
    }
    
    /* White text styling - ensure visibility */
    .login-container h2 {
        color: white !important;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .login-container p {
        color: #ffffff !important;
        opacity: 0.95;
    }
    
    /* Login button styling */
    .stButton > button {
        background-color: #ff4500;
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-weight: bold;
        border-radius: 5px;
        transition: all 0.3s;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        background-color: #cc3700;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }
    
    /* Style text input */
    .stTextInput > div > div > input {
        border: 2px solid #e0e0e0;
        border-radius: 5px;
        padding: 0.75rem;
        font-size: 16px;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #003366;
        box-shadow: 0 0 0 2px rgba(0, 51, 102, 0.1);
    }
    
    /* Password label styling */
    .stTextInput > label {
        color: white !important;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    /* Headers with Fox Sports blue */
    h1, h3 {
        color: #003366 !important;
        font-weight: bold;
        text-align: center;
        /* Subtle white glow for readability */
        text-shadow: 0 0 3px rgba(255, 255, 255, 0.4);
    }
        
    /* Error message styling */
    div[data-testid="stNotification"] {
        background-color: rgba(220, 53, 69, 0.1);
        border: 1px solid #dc3545;
        border-radius: 5px;
    }
        
    /* Footer styling */
    .custom-footer {
        text-align: center;
        color: #A0A0A0;
        margin-top: 2rem;
        font-size: 0.85rem;
        opacity: 0.8;
    }

    /* Simple centering handled inline; extra wrapper removed */
</style>
""", unsafe_allow_html=True)

# Initialize session state for authentication
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Password check
if not st.session_state.authenticated:
    # On login page, the background is light, so headers should be blue
    st.markdown("""
    <style>
        .stApp { background: #f0f2f6; }
        .stApp::before { display: none; }
        h1, h3 { color: #003366 !important; text-shadow: none !important; }
    </style>
    """, unsafe_allow_html=True)

    # Create centered column for login
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Display Fox Sports logo
        st.image("assets/fox-sports.jpg", width=250)
        
        # Login container with Fox Sports styling
        with st.container():
            st.markdown("""
            <div class="login-container">
                <h2 style="text-align: center; color: white; font-size: 28px; margin-bottom: 0.5rem;">
                    Cleetus AI
                </h2>
                <p style="text-align: center; color: rgba(255,255,255,0.9); margin-bottom: 2rem; font-size: 16px;">
                    Enter your credentials to access the AI Assistant
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        # Create a form for better UX
        with st.form("login_form"):
            password = st.text_input("Password", type="password", placeholder="Enter your password", label_visibility="collapsed")
            submitted = st.form_submit_button("🔓 LOGIN", use_container_width=True)
            
            if submitted:
                if password == "fsworldcup2026":
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("❌ Incorrect password. Please try again.")
        
        # Footer
        st.markdown("""
        <p class="custom-footer">
            © 2025 Fox Sports. All rights reserved.<br>
            FIFA World Cup 2026™ Official Broadcaster
        </p>
        """, unsafe_allow_html=True)
        
else:
    # --- Authenticated View ---
    logo_path = str(Path(__file__).parent / "assets/fox-sports.jpg")
    encoded_logo = get_base64_of_bin_file(logo_path)

    # Centered Header
    if encoded_logo:
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 0.5rem;">
            <h1>Fox Sports AI Assistant</h1>
            <img src="data:image/jpeg;base64,{encoded_logo}" width="120" style="margin: 0.5rem 0;">
        </div>
        """, unsafe_allow_html=True)

    
    # ElevenLabs widget - centered and properly positioned
    widget_html = """
    <div style="display:flex; justify-content:center; margin-top:1.2rem;">
        <elevenlabs-convai 
            agent-id="agent_01jyj2mn17e2jvdqkmrh6jzfd1"
            variant="expanded"
        ></elevenlabs-convai>
    </div>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
    """

    html(widget_html, height=520)
    
    # Footer
    st.markdown("""
    <p class="custom-footer" style="margin-top: 1.5rem;">
        © 2024 Fox Sports • FIFA World Cup 2026™ Official Broadcaster<br>
        <small>Powered by ElevenLabs AI Technology</small>
    </p>
    """, unsafe_allow_html=True) 