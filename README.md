# ElevenLabs AI Chat Streamlit App

A password-protected Streamlit app for interacting with ElevenLabs AI assistants.

## Features
- Password protection for secure access
- Voice and text chat interface
- Easy deployment to Streamlit Cloud

## Setup

1. **Clone and setup**
   ```bash
   git clone https://github.com/jackmazac/eleven-streamlit
   cd eleven-streamlit
   ./setup.sh
   ```

2. **Configure**
   - Get your agent ID from [ElevenLabs](https://elevenlabs.io)
   - Ensure your agent is public and has authentication disabled
   - Default password: `commanders-suck` (change in app.py for production)

3. **Run locally**
   ```bash
   streamlit run app.py
   ```

## Security Note
The app includes password protection. Users must authenticate before accessing the AI chat interface. Consider changing the default password for production deployments.