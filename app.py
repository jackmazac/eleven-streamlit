import streamlit as st
from streamlit.components.v1 import html
import base64
from pathlib import Path

# Function to load and encode image to Base64
@st.cache_data
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return None

# Page config
st.set_page_config(
    page_title="Cleetus AI",
    page_icon="🦊",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Get base64 encoded images
bg_image = get_base64_of_bin_file(Path(__file__).parent / "assets/world-cup.jpg")
logo_image = get_base64_of_bin_file(Path(__file__).parent / "assets/fox-sports.jpg")

# Consolidated CSS - Fixed visual issues and reduced redundancy
st.markdown(f"""
<style>
    /* Hide Streamlit elements */
    #MainMenu, footer, header, .stDeployButton {{visibility: hidden;}}
    
    /* Background styling - simplified */
    .stApp {{
        background: {f'linear-gradient(rgba(0,21,41,0.85), rgba(0,0,0,0.95)), url("data:image/jpeg;base64,{bg_image}") center/cover fixed' if st.session_state.authenticated and bg_image else '#f0f2f6'};
    }}
    
    /* Headers - Polished typography */
    h1 {{
        background: {'linear-gradient(135deg, #0084FF 0%, #0066CC 100%)' if st.session_state.authenticated else '#003366'};
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
        font-weight: 800;
        text-align: center;
        font-size: clamp(2rem, 5vw, 3rem);
        margin-bottom: 1.5rem;
        letter-spacing: -0.02em;
        line-height: 1.2;
        position: relative;
        padding-bottom: 0.5rem;
    }}
    
    /* Subtle underline accent */
    h1::after {{
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 4px;
        background: {'linear-gradient(90deg, #0084FF, #0066CC)' if st.session_state.authenticated else '#003366'};
        border-radius: 2px;
        opacity: {'0.8' if st.session_state.authenticated else '1'};
    }}
    
    /* Login container */
    .login-container {{
        background: #003366;
        padding: 2.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        text-align: center;
    }}
    
    .login-container h2 {{
        color: white;
        font-size: 1.8rem;
        margin-bottom: 0.5rem;
    }}
    
    .login-container p {{
        color: rgba(255,255,255,0.85);
        font-size: 1rem;
    }}
    
    /* Button styling */
    .stButton > button {{
        background: #ff4500;
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-weight: 600;
        border-radius: 6px;
        text-transform: uppercase;
        transition: all 0.2s;
    }}
    
    .stButton > button:hover {{
        background: #cc3700;
        transform: translateY(-1px);
    }}
    
    /* Input field */
    .stTextInput input {{
        border-radius: 6px;
        border: 2px solid #e0e0e0;
        padding: 0.75rem;
    }}
    
    .stTextInput input:focus {{
        border-color: #003366;
        outline: none;
    }}
    
    /* Footer - improved contrast */
    .footer {{
        text-align: center;
        color: {'rgba(255,255,255,0.7)' if st.session_state.authenticated else '#666'};
        margin-top: 2rem;
        font-size: 0.875rem;
    }}
    
    /* Authenticated view styling */
    .main-header {{
        text-align: center;
        margin-bottom: 2rem;
    }}
    
    .main-header img {{
        margin: 1rem 0;
    }}
    
    .widget-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        padding: 1rem 0;
    }}
</style>
""", unsafe_allow_html=True)

# Authentication check
if not st.session_state.authenticated:
    # Login page
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if logo_image:
            st.image(f"data:image/jpeg;base64,{logo_image}", width=250)
        
        st.markdown("""
        <div class="login-container">
            <h2>Cleetus AI</h2>
            <p>Enter your credentials to access the AI Assistant</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("login_form"):
            password = st.text_input("Password", type="password", placeholder="Enter your password", label_visibility="collapsed")
            submitted = st.form_submit_button("🔓 LOGIN", use_container_width=True)
            
            if submitted and password == "fsworldcup2026":
                st.session_state.authenticated = True
                st.rerun()
            elif submitted:
                st.error("❌ Incorrect password. Please try again.")
        
        st.markdown("""
        <p class="footer">
            © 2025 Fox Sports. All rights reserved.<br>
            FIFA World Cup 2026™ Official Broadcaster
        </p>
        """, unsafe_allow_html=True)

else:
    # Authenticated view
    st.markdown(f"""
    <div class="main-header">
        <h1>Cleetus AI</h1>
        {f'<img src="data:image/jpeg;base64,{logo_image}" width="150">' if logo_image else ''}
    </div>
    """, unsafe_allow_html=True)
    
    # ElevenLabs widget - wrapped for centering
    widget_html = """
    <div class="widget-container">
        <elevenlabs-convai 
            agent-id="agent_01jyj2mn17e2jvdqkmrh6jzfd1"
            variant="expanded"
        ></elevenlabs-convai>
    </div>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
    """
    
    html(widget_html, height=600)
    
    st.markdown("""
    <p class="footer">
        © 2025 Fox Sports • FIFA World Cup 2026™ Official Broadcaster<br>
        <small>Powered by ElevenLabs AI Technology</small>
    </p>
    """, unsafe_allow_html=True)