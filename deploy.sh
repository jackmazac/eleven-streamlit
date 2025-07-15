#!/bin/bash

# Quick deploy to GitHub for Streamlit Cloud
echo "🚀 Quick Deploy to Streamlit Cloud"

# Initialize git if needed
if [ ! -d .git ]; then
    git init
fi

# Add all files
git add .
git commit -m "Deploy to Streamlit Cloud"

# Check if remote exists
if ! git remote | grep -q origin; then
    echo "Enter your GitHub repo URL (e.g., https://github.com/username/eleven-streamlit):"
    read repo_url
    git remote add origin $repo_url
fi

# Push to GitHub
git push -u origin main

echo "✅ Pushed to GitHub!"
echo "📱 Now go to https://share.streamlit.io to deploy your app"
echo "🔗 Your public URL will be: https://[username]-eleven-streamlit-app-[random].streamlit.app" 