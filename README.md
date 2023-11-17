# Python_project

# Voice-Activated Email Sender

This Python script allows users to send emails using voice commands. The script utilizes speech recognition to interpret voice commands and sends emails via the Gmail SMTP server.

## Features

- Voice-based interaction for email sending.
- Supports Gmail as the email service provider.
- Simple and easy-to-use interface.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- SpeechRecognition library (`pip install SpeechRecognition`)
- pyttsx3 library (`pip install pyttsx3`)
- smtplib (standard library)

## Configuration

1. Update the `emails` dictionary in the script with the email addresses of your contacts.
2. Replace the email credentials in the `mail_send` function with your Gmail credentials.

## Usage

1. Run the script using a Python interpreter: `python script_name.py`.
2. Follow the voice prompts to provide the recipient's name, email subject, and body.
3. The script will send the email using the specified Gmail account.

## Important Note

- **Security:** Avoid sharing or uploading this script with hardcoded email credentials. Consider using environment variables or a configuration file for sensitive information.


