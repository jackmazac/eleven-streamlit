import streamlit as st
from streamlit.components.v1 import html
import base64
from pathlib import Path
import time

# Function to load and encode image to Base64
@st.cache_data
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return None

# Cookie management functions using localStorage (more reliable with Streamlit)
def set_auth_cookie(value, days=30):
    """Set authentication cookie using JavaScript"""
    js_code = f"""
    <script>
        localStorage.setItem('herd_ai_auth', '{value}');
        // Also set a cookie for server-side persistence
        const expiry = new Date();
        expiry.setTime(expiry.getTime() + ({days} * 24 * 60 * 60 * 1000));
        document.cookie = "herd_ai_auth={value}; expires=" + expiry.toUTCString() + "; path=/; SameSite=Lax";
    </script>
    """
    html(js_code)

def check_auth_cookie():
    """Check if authentication cookie exists and redirect if authenticated"""
    js_code = """
    <script>
        // Check localStorage first
        const authValue = localStorage.getItem('herd_ai_auth');
        if (authValue === 'authenticated') {
            // Redirect with authentication parameter
            const url = new URL(window.location);
            url.searchParams.set('authenticated', 'true');
            window.location.href = url.toString();
        } else {
            // Check cookie as backup
            const cookies = document.cookie.split(';');
            for (let cookie of cookies) {
                const [name, value] = cookie.trim().split('=');
                if (name === 'herd_ai_auth' && value === 'authenticated') {
                    const url = new URL(window.location);
                    url.searchParams.set('authenticated', 'true');
                    window.location.href = url.toString();
                    break;
                }
            }
        }
    </script>
    """
    html(js_code)

def clear_auth_cookie():
    """Clear authentication cookie using JavaScript"""
    js_code = """
    <script>
        localStorage.removeItem('herd_ai_auth');
        document.cookie = "herd_ai_auth=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    </script>
    """
    html(js_code)

# Page config
st.set_page_config(
    page_title="Herd AI",
    page_icon="🦊",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Check for authentication cookie/localStorage on first load
if not st.session_state.authenticated:
    check_auth_cookie()
    # Check for authentication query parameter
    query_params = st.query_params
    if query_params.get('authenticated') == 'true':
        st.session_state.authenticated = True
        # Clear the query param to clean up the URL
        st.query_params.clear()

# Get base64 encoded images
bg_image = get_base64_of_bin_file(Path(__file__).parent / "assets/world-cup.jpg")
logo_image = get_base64_of_bin_file(Path(__file__).parent / "assets/fox-sports.jpg")
login_bg_image = get_base64_of_bin_file(Path(__file__).parent / "assets/login-background.png")

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
        background: {f'linear-gradient(rgba(0,21,41,0.85), rgba(0,0,0,0.95)), url("data:image/jpeg;base64,{bg_image}") center/cover fixed' if st.session_state.authenticated and bg_image else f'linear-gradient(rgba(0,21,41,0.3), rgba(0,0,0,0.4)), url("data:image/png;base64,{login_bg_image}") center/cover fixed' if login_bg_image else 'linear-gradient(rgba(0,21,41,0.95), rgba(0,0,0,0.98))'};
    }}
    
    /* Headers - Polished typography */
    h1 {{
        background: {'linear-gradient(135deg, #FFFFFF 0%, #E0E0E0 100%)' if st.session_state.authenticated else '#FFFFFF'};
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        font-weight: 600;
        text-align: center;
        font-size: clamp(3.5rem, 5vw, 4.5rem);
        margin-bottom: 1rem;
        letter-spacing: 0.1em;
        line-height: 1.2;
        position: relative;
        padding-bottom: 0.5rem;
        filter: drop-shadow(0 3px 6px rgba(0, 0, 0, 0.8));
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
    
    /* Login container - REMOVED - form elements now appear directly on background */
    
    /* Button styling */
    .stButton > button {{
        background: linear-gradient(135deg, #0084FF 0%, #0066CC 100%);
        color: white;
        border: none;
        padding: 1.2rem 4rem;
        font-weight: 600;
        border-radius: 10px;
        text-transform: uppercase;
        transition: all 0.3s ease;
        font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        letter-spacing: 0.12em;
        font-size: 1.3rem;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5);
    }}
    
    .stButton > button:hover {{
        background: linear-gradient(135deg, #0066CC 0%, #0052A3 100%);
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.6);
    }}
    
    /* Input field styling */
    .stTextInput > div > div > input {{
        border-radius: 10px !important;
        border: 2px solid rgba(255, 255, 255, 0.4) !important;
        padding: 1.2rem 1.5rem !important;
        background: rgba(255, 255, 255, 0.9) !important;
        color: #000000 !important;
        font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
        font-size: 1.2rem !important;
        font-weight: 500 !important;
        letter-spacing: 0.04em !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(20px) !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3) !important;
        -webkit-text-fill-color: #000000 !important;
    }}
    
    .stTextInput > div > div > input:focus {{
        border-color: rgba(0, 132, 255, 0.8) !important;
        outline: none !important;
        background: rgba(255, 255, 255, 1) !important;
        box-shadow: 0 0 0 3px rgba(0, 132, 255, 0.3), 0 8px 32px rgba(0, 0, 0, 0.4) !important;
    }}
    
    .stTextInput > div > div > input::placeholder {{
        color: rgba(0, 0, 0, 0.5) !important;
        font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
        font-weight: 400 !important;
        -webkit-text-fill-color: rgba(0, 0, 0, 0.5) !important;
    }}
    
    /* Input field wrapper */
    .stTextInput > div {{
        background: transparent !important;
        position: relative !important;
    }}
    
    /* Password visibility toggle button */
    .stTextInput > div > div > button {{
        background: transparent !important;
        border: none !important;
        color: rgba(0, 0, 0, 0.6) !important;
        right: 1rem !important;
        position: absolute !important;
        top: 50% !important;
        transform: translateY(-50%) !important;
    }}
    
    .stTextInput > div > div > button:hover {{
        color: rgba(0, 0, 0, 0.9) !important;
    }}
    
    /* Footer - improved contrast */
    .footer {{
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: {'rgba(0, 21, 41, 0.9)' if st.session_state.authenticated else 'transparent'};
        backdrop-filter: blur(10px);
        padding: 1rem 0;
        text-align: center;
        color: {'rgba(255,255,255,0.9)' if st.session_state.authenticated else 'rgba(255,255,255,0.9)'};
        font-size: 1rem;
        font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        letter-spacing: 0.03em;
        border-top: {'1px solid rgba(255, 255, 255, 0.1)' if st.session_state.authenticated else 'none'};
        z-index: 100;
    }}
    
    /* Fixed footer for login page */
    .login-footer {{
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: transparent;
        padding: 1.5rem 0;
        text-align: center;
        color: rgba(255,255,255,1);
        font-size: 1rem;
        font-weight: 500;
        font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        letter-spacing: 0.03em;
        z-index: 100;
        text-shadow: 0 2px 6px rgba(0, 0, 0, 1), 0 0 20px rgba(0, 0, 0, 0.8);
    }}
    
    .login-footer span {{
        font-size: 0.9rem;
        opacity: 0.9;
    }}
    
    /* Authenticated view styling */
    .main-header {{
        text-align: center;
        margin-bottom: 0.25rem;
    }}
    
    .main-header img {{
        margin: 0.25rem 0;
        width: 120px;
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
        background: rgba(255, 68, 68, 0.2);
        border: 2px solid rgba(255, 68, 68, 0.5);
        border-radius: 10px;
        color: rgba(255, 255, 255, 1);
        font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        backdrop-filter: blur(12px);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
        max-width: 500px;
        margin: 1rem auto 0 auto;
    }}
    
    /* Form container styling */
    .stForm {{
        background: transparent;
        max-width: 500px;
        margin: 0 auto;
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
    

    /* Add padding to bottom when footer is fixed */
    .main > div {{
        padding-bottom: {'1rem' if st.session_state.authenticated else '6rem'};
    }}
</style>
""", unsafe_allow_html=True)

# Authentication check
if not st.session_state.authenticated:
    # Login page
    col1, col2, col3 = st.columns([0.5, 4, 0.5])
    
    with col2:
        # Add spacing at top
        st.markdown('<div style="margin-top: 2rem;"></div>', unsafe_allow_html=True)
        
        # Title without box
        st.markdown("""
        <h2 style="color: white; font-size: 3.5rem; font-weight: 600; 
                   letter-spacing: 0.12em; text-shadow: 0 4px 8px rgba(0, 0, 0, 1); 
                   font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; 
                   text-transform: uppercase; text-align: center; margin-bottom: 2rem;">
            HERD AI
        </h2>
        """, unsafe_allow_html=True)
        
        # Form without container
        with st.form("login_form", clear_on_submit=False):
            password = st.text_input("Password", type="password", placeholder="Enter password", label_visibility="collapsed")
            
            st.markdown('<div style="margin-top: 1.5rem;"></div>', unsafe_allow_html=True)
            
            submitted = st.form_submit_button("▸ LOGIN", use_container_width=True)

            if submitted and password == "fsworldcup2026":
                st.session_state.authenticated = True
                set_auth_cookie("authenticated", days=30)  # Cookie expires in 30 days
                st.rerun()
            elif submitted:
                st.error("❌ Incorrect password. Please try again.")
        
    # Footer - pinned to bottom
    st.markdown("""
    <div class="login-footer">
        © 2025 Fox Sports. All rights reserved.<br>
        <span>FIFA World Cup 2026™ Official Broadcaster</span>
    </div>
    """, unsafe_allow_html=True)

else:
    # Authenticated view

    # Fox Sports logo in top right
    if logo_image:
        st.markdown(f"""
        <div style="position: fixed; top: 1rem; right: 1rem; z-index: 100;">
            <img src="data:image/jpeg;base64,{logo_image}" style="width: 100px; opacity: 0.9; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.5));">
        </div>
        """, unsafe_allow_html=True)
    
    # Main header
    st.markdown("""
    <div class="main-header">
        <h1>Herd AI</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Container for multiple widgets with custom styling
    st.markdown("""
    <style>
        /* Widget container styling for horizontal layout */
        .widget-container {
            display: flex;
            justify-content: center;
            align-items: start;
            gap: 3rem;
            margin-top: 1rem;
            max-width: 1400px;
            margin-left: auto;
            margin-right: auto;
        }
        
        /* Main content area padding for fixed footer */
        .stApp > div {
            padding-bottom: 5rem !important;
        }
        
        /* Container max width for better layout */
        .main .block-container {
            max-width: 1400px !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
        }
        
        /* Make markdown headers visible on dark background */
        h3 {
            color: #FFFFFF !important;
            font-size: 1.4rem !important;
            font-weight: 600 !important;
            margin-bottom: 0.3rem !important;
            margin-top: 0 !important;
            padding-top: 0 !important;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8) !important;
            transition: all 0.3s ease !important;
            cursor: default !important;
            position: relative !important;
            display: inline-block !important;
            font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
            letter-spacing: 0.03em !important;
            white-space: nowrap !important;
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
            font-size: 1.1rem !important;
            display: block;
            margin-bottom: 0.8rem;
            margin-top: 0;
            line-height: 1.3;
            font-family: 'Industry', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
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
        
        /* Column container styling for horizontal layout */
        [data-testid="column"] {
            padding: 1.5rem !important;
            background: rgba(0, 33, 66, 0.2) !important;
            border-radius: 12px !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            backdrop-filter: blur(10px) !important;
            position: relative !important;
        }
        
        /* Grid column defaults for all quadrants */
        /* No extra dividers or nth-child overrides needed */
        
        /* Ensure widgets fill column width */
        [data-testid="column"] iframe {
            width: 100% !important;
        }
        
        /* Center align content in columns */
        [data-testid="column"] > div {
            text-align: center;
        }
        
        /* Responsive design for smaller screens */
        @media (max-width: 1024px) {
            [data-testid="column"] {
                margin-bottom: 1.5rem !important;
                margin-left: 0 !important;
                margin-right: 0 !important;
            }
            
            /* No divider overrides required in responsive mode */
            
            h3 {
                font-size: 1.2rem !important;
            }
            
            p em {
                font-size: 1rem !important;
            }
            
            h1 {
                font-size: clamp(2.5rem, 4vw, 3.5rem) !important;
            }
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Container for widgets with max width
    container = st.container()
    
    with container:
        # Top row
        top_left, top_right = st.columns(2, gap="large")
        
        # Widget 1 - Colin World Cup (top-left)
        with top_left:
            st.markdown("### Colin World Cup")
            st.markdown("*World Cup stats & insights*")
            widget1_html = """
            <elevenlabs-convai 
                agent-id="agent_01jyj2mn17e2jvdqkmrh6jzfd1"
                variant="expanded"
            ></elevenlabs-convai>
            <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
            """
            html(widget1_html, height=260)
        
        # Widget 2 - Colin General Sports (top-right)
        with top_right:
            st.markdown("### Colin General Sports")
            st.markdown("*All sports coverage*")
            widget2_html = """
            <elevenlabs-convai 
                agent-id="agent_01k084d7dtfyaazh2e27y2kzcy"
                variant="expanded"
            ></elevenlabs-convai>
            <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
            """
            html(widget2_html, height=260)
        
        # Spacer between rows
        st.markdown('<div style="height: 1.5rem;"></div>', unsafe_allow_html=True)
        
        # Bottom row
        bottom_left, bottom_right = st.columns(2, gap="large")
        
        # Widget 3 - Additional Agent (bottom-left)
        with bottom_left:
            st.markdown("### Colin Additional Agent")
            st.markdown("*Custom agent*")
            widget3_html = """
            <elevenlabs-convai agent-id="agent_6601k4zk42ebeagrspzca4mvebn8"></elevenlabs-convai>
            <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
            """
            html(widget3_html, height=400)
        
        # Bottom-right quadrant intentionally left unused for now
        with bottom_right:
            st.empty()
        

    
    st.markdown("""
    <p class="footer">
        © 2025 Fox Sports • FIFA World Cup 2026™ Official Broadcaster<br>
        <small>Powered by ElevenLabs AI Technology</small>
    </p>
    """, unsafe_allow_html=True)