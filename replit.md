# Hidster KvK

## Overview
A Flask-based web application that displays random songs with QR codes that link to Spotify. This is a Dutch music guessing game app.

## Project Structure
- `app.py` - Main Flask application
- `templates/index.html` - HTML template for the UI
- `songs.json` - JSON file containing song data
- `requirements.txt` - Python dependencies

## How It Works
1. User visits the homepage and sees a QR code
2. Scanning the QR code opens the Spotify track
3. Clicking "Laat maar zien!" reveals song details
4. "Volgende" button loads a new random song

## Running the App
The app runs on port 5000 with Flask's development server in development mode, and gunicorn in production.

## Dependencies
- Flask - Web framework
- qrcode - QR code generation
- Pillow - Image processing for QR codes
- gunicorn - Production WSGI server
