#!/bin/bash

# Install requirements
echo "Installing dependencies..."
python3 -m pip install -r requirements.txt

# Run the app
echo "Starting AutoNB..."
python3 -m streamlit run app.py
