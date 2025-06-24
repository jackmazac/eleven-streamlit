# ElevenLabs AI Chat Streamlit App

A simple Streamlit app that embeds the ElevenLabs Conversational AI widget for voice and text interactions.

## Quick Start

1. **Clone and setup**
   ```bash
   git clone <your-repo-url>
   cd eleven-streamlit
   ./setup.sh
   ```

2. **Configure**
   - Get your agent ID from [ElevenLabs](https://elevenlabs.io)
   - Replace `YOUR_AGENT_ID_HERE` in `app.py` with your actual agent ID
   - Ensure your agent is public and has authentication disabled

3. **Run locally**
   ```bash
   streamlit run app.py
   ```

## Deployment

### Streamlit Cloud
1. Push to GitHub
2. Connect to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy directly from your repo

### Other platforms
- **Heroku**: Use included `Procfile`
- **Railway/Render**: Auto-detects Streamlit apps
- **Docker**: Build with `docker build -t elevenlabs-chat .`

## Requirements
- Python 3.8+
- Streamlit 1.28+

## Security Notes
- Add your deployment URL to the agent's allowlist in ElevenLabs
- The widget runs in a sandboxed iframe for security 