#!/bin/bash

echo "Setting up ElevenLabs Streamlit App..."

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

echo "Setup complete! Run 'streamlit run app.py' to start the app."
echo "Don't forget to update YOUR_AGENT_ID_HERE in app.py with your actual agent ID." 