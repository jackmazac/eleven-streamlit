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
    page_title="Cleatus AI",
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
fandom_image = get_base64_of_bin_file(Path(__file__).parent / "assets/fox-fandom.jpg")

# Get base64 encoded fonts
font_light = get_base64_of_bin_file(Path(__file__).parent / "assets/fonts/industry-font/IndustryTest-Light.otf")
font_book = get_base64_of_bin_file(Path(__file__).parent / "assets/fonts/industry-font/IndustryTest-Book.otf")
font_medium = get_base64_of_bin_file(Path(__file__).parent / "assets/fonts/industry-font/IndustryTest-Medium.otf")
font_demi = get_base64_of_bin_file(Path(__file__).parent / "assets/fonts/industry-font/IndustryTest-Demi.otf")

# Consolidated CSS - Fixed visual issues and reduced redundancy
st.markdown(f"""
<style>
    /* Font Face Declarations */
    @font-face {{
        font-family: 'Industry';
        font-weight: 300;
        font-style: normal;
        src: url(data:font/otf;base64,{font_light}) format('opentype');
    }}
    
    @font-face {{
        font-family: 'Industry';
        font-weight: 400;
        font-style: normal;
        src: url(data:font/otf;base64,{font_book}) format('opentype');
    }}
    
    @font-face {{
        font-family: 'Industry';
        font-weight: 500;
        font-style: normal;
        src: url(data:font/otf;base64,{font_medium}) format('opentype');
    }}
    
    @font-face {{
        font-family: 'Industry';
        font-weight: 600;
        font-style: normal;
        src: url(data:font/otf;base64,{font_demi}) format('opentype');
    }}
    
    /* Global font settings */
    * {{
        font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
    }}
    
    body {{
        font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
        font-weight: 400;
    }}
    
    /* Hide Streamlit elements */
    #MainMenu, footer, header, .stDeployButton {{visibility: hidden;}}
    
    /* Background styling - simplified */
    .stApp {{
        background: {f'linear-gradient(rgba(0,21,41,0.85), rgba(0,0,0,0.95)), url("data:image/jpeg;base64,{bg_image}") center/cover fixed' if st.session_state.authenticated and bg_image else 'linear-gradient(rgba(0,21,41,0.95), rgba(0,0,0,0.98)), radial-gradient(ellipse at top, rgba(0, 132, 255, 0.1) 0%, transparent 50%)'};
    }}
    
    /* Headers - Polished typography */
    h1 {{
        background: {'linear-gradient(135deg, #FFFFFF 0%, #E0E0E0 100%)' if st.session_state.authenticated else '#FFFFFF'};
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        font-weight: 300;
        text-align: center;
        font-size: clamp(2.5rem, 5vw, 3.5rem);
        margin-bottom: 0.5rem;
        letter-spacing: 0.05em;
        line-height: 1.2;
        position: relative;
        padding-bottom: 0.5rem;
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.6));
        transition: all 0.3s ease;
    }}

    
    /* Hover effect for h1 */
    h1:hover {{
        transform: scale(1.02);
        filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.8));
    }}
    
    /* Subtle underline accent */
    h1::after {{
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 2px;
        background: {'linear-gradient(90deg, #FFFFFF, #E0E0E0)' if st.session_state.authenticated else '#FFFFFF'};
        border-radius: 2px;
        opacity: {'0.6' if st.session_state.authenticated else '1'};
    }}
    
    /* Login container */
    .login-container {{
        background: rgba(0, 21, 41, 0.85);
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.4);
        text-align: center;
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }}
    
    .login-container h2 {{
        color: white;
        font-size: 1.5rem;
        margin-bottom: 0.3rem;
        font-weight: 300;
        letter-spacing: 0.06em;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
        font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        text-transform: uppercase;
    }}
    
    .login-container p {{
        color: rgba(255,255,255,0.8);
        font-size: 0.95rem;
        font-weight: 400;
        margin-bottom: 1.5rem;
        font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        letter-spacing: 0.02em;
    }}
    
    /* Button styling */
    .stButton > button {{
        background: linear-gradient(135deg, #0084FF 0%, #0066CC 100%);
        color: white;
        border: none;
        padding: 0.85rem 3rem;
        font-weight: 500;
        border-radius: 8px;
        text-transform: uppercase;
        transition: all 0.3s ease;
        font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        letter-spacing: 0.08em;
        font-size: 1rem;
        box-shadow: 0 4px 12px rgba(0, 132, 255, 0.3);
    }}
    
    .stButton > button:hover {{
        background: linear-gradient(135deg, #0066CC 0%, #0052A3 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 132, 255, 0.4);
    }}
    
    /* Input field styling */
    .stTextInput input {{
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 0.85rem 1rem;
        background: rgba(255, 255, 255, 0.05);
        color: white;
        font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        font-size: 1rem;
        letter-spacing: 0.02em;
        transition: all 0.3s ease;
    }}
    
    .stTextInput input:focus {{
        border-color: rgba(0, 132, 255, 0.5);
        outline: none;
        background: rgba(255, 255, 255, 0.08);
        box-shadow: 0 0 0 2px rgba(0, 132, 255, 0.2);
    }}
    
    .stTextInput input::placeholder {{
        color: rgba(255, 255, 255, 0.5);
        font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }}
    
    /* Footer - improved contrast */
    .footer {{
        text-align: center;
        color: {'rgba(255,255,255,0.8)' if st.session_state.authenticated else 'rgba(255,255,255,0.9)'};
        margin-top: 0.5rem;
        font-size: 0.85rem;
        font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        letter-spacing: 0.02em;
    }}
    
    /* Authenticated view styling */
    .main-header {{
        text-align: center;
        margin-bottom: 0.5rem;
    }}
    
    .main-header img {{
        margin: 0.5rem 0;
    }}
    
    .widget-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        padding: 1rem 0;
    }}
    
    /* Error message styling */
    .stAlert {{
        background: rgba(255, 68, 68, 0.1);
        border: 1px solid rgba(255, 68, 68, 0.3);
        border-radius: 8px;
        color: rgba(255, 255, 255, 0.9);
        font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }}
    
    /* Form container styling */
    .stForm {{
        background: transparent;
    }}
    
    /* Hide default form help text */
    .stForm > div[data-testid="stFormSubmitButton"] > div > div > small {{
        display: none !important;
    }}
    
    /* Form submit area */
    .stForm [data-testid="stFormSubmitButton"] {{
        margin-top: 0 !important;
    }}
    
    /* Additional button icon removal */
    .stButton > button > div {{
        display: flex;
        justify-content: center;
        align-items: center;
    }}
</style>
""", unsafe_allow_html=True)

# Authentication check
if not st.session_state.authenticated:
    # Login page
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Fox Sports Logo
        if logo_image:
            st.markdown(
                f'<div style="text-align: center; margin-bottom: 1.5rem;">'
                f'<img src="data:image/jpeg;base64,{logo_image}" style="width: 200px; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));">'
                f'</div>',
                unsafe_allow_html=True
            )
        
        # Login Container
        st.markdown("""
        <div class="login-container">
            <h2>Cleatus AI</h2>
            <p>Enter your credentials to access the AI Assistant</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Form with custom spacing
        with st.form("login_form", clear_on_submit=False):
            password = st.text_input("Password", type="password", placeholder="Enter password", label_visibility="collapsed")
            
            # Add help text that's always visible
            st.markdown("""
            <p style="text-align: center; color: rgba(255, 255, 255, 0.6); 
                      font-size: 0.85rem; margin: 0.5rem 0 1rem 0; 
                      font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                      letter-spacing: 0.02em;">
                Enter password to enter Cleatus
            </p>
            """, unsafe_allow_html=True)
            
            submitted = st.form_submit_button("▸ LOGIN", use_container_width=True)
            
            if submitted and password == "fsworldcup2026":
                st.session_state.authenticated = True
                st.rerun()
            elif submitted:
                st.error("❌ Incorrect password. Please try again.")
        
        # Add Fox Fandom image below the login form
        if fandom_image:
            st.markdown(
                f'<div style="text-align: center; margin-top: 1.5rem;">'
                f'<img src="data:image/jpeg;base64,{fandom_image}" style="width: 100%; max-width: 400px; border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.3);">'
                f'</div>',
                unsafe_allow_html=True
            )
        
        # Footer
        st.markdown("""
        <p class="footer" style="margin-top: 1.5rem;">
            © 2025 Fox Sports. All rights reserved.<br>
            <span style="font-size: 0.8rem; opacity: 0.8;">FIFA World Cup 2026™ Official Broadcaster</span>
        </p>
        """, unsafe_allow_html=True)

else:
    # Authenticated view
    st.markdown(f"""
    <div class="main-header">
        <h1>Cleatus AI</h1>
        {f'<img src="data:image/jpeg;base64,{logo_image}" width="150">' if logo_image else ''}
    </div>
    """, unsafe_allow_html=True)
    
    # Container for multiple widgets with custom styling
    st.markdown("""
    <style>
        /* Widget section styling */
        .widget-section {
            background: rgba(0, 33, 66, 0.4);
            border-radius: 16px;
            padding: 2rem;
            margin-bottom: 2rem;
            border: 1px solid rgba(0, 132, 255, 0.2);
            backdrop-filter: blur(10px);
            position: relative;
            overflow: hidden;
        }
        
        .widget-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: rgba(255, 255, 255, 0.3);
        }
        
        .widget-label {
            color: #FFFFFF;
            font-size: 1.25rem;
            font-weight: 500;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }
        
        .widget-label::before {
            content: '▸';
            font-size: 1.2rem;
            color: rgba(255, 255, 255, 0.6);
        }
        
        .widget-description {
            color: rgba(255, 255, 255, 0.85);
            font-size: 0.9rem;
            margin-bottom: 1rem;
            line-height: 1.4;
            font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }
        
        /* Divider styling */
        .section-divider {
            height: 1px;
            background: linear-gradient(90deg, 
                transparent, 
                rgba(255, 255, 255, 0.2) 20%, 
                rgba(255, 255, 255, 0.2) 80%, 
                transparent
            );
            margin: 1.5rem 0;
        }
        
        /* Make markdown headers visible on dark background */
        h3 {
            color: #FFFFFF !important;
            font-size: 1.15rem !important;
            font-weight: 500 !important;
            margin-bottom: 0.1rem !important;
            margin-top: 0 !important;
            padding-top: 0 !important;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8) !important;
            transition: all 0.3s ease !important;
            cursor: default !important;
            position: relative !important;
            display: inline-block !important;
            font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
            letter-spacing: 0.03em !important;
        }
        
        /* Hover effect for extra polish */
        h3:hover {
            transform: translateY(-1px) !important;
            text-shadow: 0 3px 6px rgba(0, 0, 0, 1) !important;
        }
        
        /* Make italic descriptions visible */
        p em {
            color: rgba(255, 255, 255, 0.85) !important;
            font-style: normal !important;
            font-size: 0.9rem !important;
            display: block;
            margin-bottom: 0.25rem;
            margin-top: 0;
            line-height: 1.3;
            font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
        }
        
        /* Hide horizontal rule dividers */
        hr {
            display: none !important;
        }
        
        /* Remove Streamlit default spacing */
        .element-container {
            margin: 0 !important;
            padding: 0 !important;
        }
        
        .stMarkdown {
            margin: 0 !important;
            padding: 0 !important;
        }
        
        .stMarkdown p {
            margin: 0 !important;
            padding: 0 !important;
        }
        
        /* Remove iframe container spacing */
        iframe {
            margin: 0 !important;
            padding: 0 !important;
            display: block !important;
        }
        
        .stComponent {
            margin: 0 !important;
            padding: 0 !important;
        }
        
        /* Tight spacing for widget sections */
        div[data-testid="stVerticalBlock"] > div {
            gap: 0 !important;
        }
        
        /* Additional spacing overrides */
        .main > div {
            padding-top: 1rem !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Widget 1 - Colin World Cup
    st.markdown("### Colin World Cup")
    st.markdown("*Get help with World Cup stats, team information, and tournament insights*")
    widget1_html = """
    <elevenlabs-convai 
        agent-id="agent_01jyj2mn17e2jvdqkmrh6jzfd1"
        variant="expanded"
    ></elevenlabs-convai>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
    """
    html(widget1_html, height=320)
    
    # Widget 2 - Colin General Sports
    st.markdown("### Colin General Sports")
    st.markdown("*Your go-to expert for all sports - NFL, NBA, MLB, NHL and more*")
    widget2_html = """
    <elevenlabs-convai 
        agent-id="agent_01k084d7dtfyaazh2e27y2kzcy"
        variant="expanded"
    ></elevenlabs-convai>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
    """
    html(widget2_html, height=320)
    
    # Widget 3 - Colin Smack Talk
    st.markdown("### Colin Smack Talk")
    st.markdown("*Ready to talk trash about your rivals and defend your team with passion*")
    widget3_html = """
    <elevenlabs-convai 
        agent-id="agent_01jyj64kjyenyahcts8pcwckxn"
        variant="expanded"
    ></elevenlabs-convai>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
    """
    html(widget3_html, height=320)
    
    st.markdown("""
    <p class="footer">
        © 2025 Fox Sports • FIFA World Cup 2026™ Official Broadcaster<br>
        <small>Powered by ElevenLabs AI Technology</small>
    </p>
    """, unsafe_allow_html=True)