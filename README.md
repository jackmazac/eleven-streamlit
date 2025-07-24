# Fox Sports AI Assistant - Streamlit App

A password-protected Streamlit app featuring Fox Sports branding for interacting with AI assistants, perfect for World Cup 2026 coverage and sports insights.

## Features
- Fox Sports branded interface with official navy blue theme
- Password protection for secure access
- Voice and text chat interface
- Professional sports broadcast UI/UX
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
   - Default password: `fsworldcup2026` (change in app.py for production)
   - Fox Sports logo should be placed at `assets/fox-sports.jpg`

3. **Run locally**
   ```bash
   streamlit run app.py
   ```

## Branding
The app features official Fox Sports branding including:
- Navy blue color scheme (#003366)
- Fox Sports logo integration
- Professional sports broadcast styling
- FIFA World Cup 2026™ ready

## Security Note
The app includes password protection. Users must authenticate before accessing the AI chat interface. Consider changing the default password and storing it in environment variables for production deployments.