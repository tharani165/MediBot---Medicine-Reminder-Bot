# MediBot - Medicine Reminder Bot

A simple Flask-based medicine reminder application that lets you store reminder details and trigger calls for patients.

## Project Structure

```text
medicine_reminder_project/
├── app.py
├── call_reminder.py
├── static/
├── templates/
├── data/
└── requirements.txt
```

## Features

- Add medicine reminders through a web form
- Store reminders in a local JSON file
- Trigger calls based on scheduled reminder time
- Receive call status from the device endpoint

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Flask app:
   ```bash
   python medicine_reminder_project/app.py
   ```
3. Open your browser at:
   ```text
   http://127.0.0.1:5000/
   ```

## Notes

- The Android-specific reminder endpoint is kept in [medicine_reminder_project/call_reminder.py](medicine_reminder_project/call_reminder.py).
- Keep sensitive values such as phone numbers and server addresses in environment variables when deploying.
