# MediBot – Smart Medicine Reminder & Monitoring System

> An IoT-based healthcare prototype that assists elderly patients with medication adherence by combining automated reminders, a web-based management dashboard, and Android-powered voice call notifications.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Application-black)
![IoT](https://img.shields.io/badge/IoT-Healthcare-green)
![Arduino](https://img.shields.io/badge/Arduino-Embedded-blue)
![Android](https://img.shields.io/badge/Android-SL4A-brightgreen)

---

# Project Overview

Medication non-adherence is a major challenge among elderly patients, particularly those living alone or managing multiple prescriptions. Traditional alarm-based reminder systems can be easily ignored, reducing their effectiveness.

MediBot is an IoT-based healthcare prototype that integrates embedded hardware with a web application to help caregivers manage medication schedules while automatically reminding patients through Android phone calls and voice alerts.

The project combines embedded systems, web technologies, and Android automation to provide a practical medication reminder solution.

---

# Problem Statement

Many elderly patients forget to take medicines on time due to memory loss, busy schedules, or the absence of caregivers. Conventional reminder methods such as alarms and mobile notifications are often ignored or dismissed.

A reliable reminder mechanism capable of actively notifying patients and allowing caregivers to monitor scheduled reminders can significantly improve medication adherence.

---

# Proposed Solution

MediBot provides:

- A web dashboard for caregivers to manage medicine schedules
- Automatic reminder scheduling
- Android-based voice call notifications
- Text-to-Speech (TTS) reminders
- Reminder status tracking
- Local JSON-based reminder storage

The embedded hardware and Android device work together with the web application to deliver timely reminders.

---

# Features

- Add patient medicine schedules
- Manage multiple medicines per reminder
- Automatic reminder scheduling
- Android phone call notifications
- Text-to-Speech medicine reminders
- Reminder completion tracking
- Live dashboard with Active and Finished reminders
- Local JSON data storage
- Lightweight Flask backend

---

# Technology Stack

### Embedded / IoT

- Arduino
- Android (SL4A)
- IoT Healthcare Prototype

### Software

- Python
- Flask
- HTML
- CSS
- JavaScript
- Jinja2
- Requests

### Data Storage

- JSON

---

# System Architecture

```
Caregiver
     │
     ▼
 Web Dashboard (Flask)
     │
     ▼
 Reminder Scheduler
     │
     ▼
 Android Device (SL4A)
     │
     ▼
 Text-to-Speech
     │
     ▼
 Phone Call Reminder
     │
     ▼
 Patient
```

---

# Workflow

1. Caregiver registers a patient's medication schedule through the web dashboard.
2. Reminder information is stored locally in JSON format.
3. The Flask scheduler continuously monitors reminder timings.
4. When the scheduled time arrives, the Flask server triggers the Android device.
5. The Android device announces the reminder using Text-to-Speech and places a phone call.
6. Call status is sent back to the server.
7. The dashboard updates the reminder status automatically.

---

# My Contribution

This project was developed as a collaborative IoT healthcare project.

### My primary contributions focused on the software development side, including:

- Designed and developed the Flask-based web dashboard.
- Implemented the backend reminder scheduling system using Python and Flask.
- Developed the frontend interface using HTML, CSS, JavaScript, and Jinja2.
- Designed the JSON-based reminder storage workflow.
- Integrated the Flask backend with the Android reminder application.
- Developed reminder status tracking and dashboard updates.
- Participated in software testing, debugging, and system integration.

---

# Repository Structure

```
MediBot---Medicine-Reminder-Bot/

├── android/
│   └── call_reminder.py
│
├── server/
│   ├── app.py
│   ├── templates/
│   ├── static/
│   ├── data/
│   └── requirements.txt
│
├── hardware/
├── software/
├── docs/
├── images/
├── demo/
└── README.md
```

---

# Hardware Components

See **hardware/hardware.md** for the complete list of hardware components used in the IoT prototype.

---

# Software Components

See **software/software_used.md** for all software frameworks and libraries used in the project.

---

## Project Images

| Prototype | Block Diagram |
|---|---|
| ![Prototype](images/prototype.jpg) | ![Block Diagram](images/block_diagram.png) |

| Workflow | Circuit Diagram |
|---|---|
| ![Workflow](images/workflow.png) | ![Circuit Diagram](images/circuit_diagram.png) |

## Demo Video

| New Reminder Form | Active Reminders |
|---|---|
| ![New Reminder Form](demo/new_reminder_form.png) | ![Active Reminders](demo/active_reminders.png) |

| Finished Reminders | Full Dashboard |
|---|---|
| ![Finished Reminders](demo/finished_reminders.png) | ![Full Dashboard](demo/dashboard_full_view.png) |

## Applications

- Medication adherence reminders for elderly or forgetful patients
- Caregiver/family monitoring of a patient's dosing schedule
- Clinics or care homes managing reminders for multiple patients

## Future Scope

- Support multiple caregiver-configurable devices/phone numbers per patient
- Add SMS as a fallback if a call goes unanswered
- Persist data in a proper database instead of a flat JSON file
- Add authentication so the dashboard isn't open to anyone on the network

# Team

This project was developed collaboratively.

### Team Members

- T. Hemachandiran
- Tharani R.

## Setup

1. Install dependencies:
   ```bash
   pip install -r server/requirements.txt
   ```
2. Run the Flask app:
   ```bash
   python server/app.py
   ```
3. Open your browser at:
   ```text
   http://127.0.0.1:5000/
   ```
4. Copy `android/call_reminder.py` onto the Android device and run it under SL4A to enable the reminder calls.

# Disclaimer

This repository showcases the software implementation developed as part of an academic IoT healthcare project. The software components presented here demonstrate the web-based reminder management system and Android integration developed for the overall prototype.


## Notes

- The Android-specific reminder endpoint is kept in [android/call_reminder.py](android/call_reminder.py).
- Keep sensitive values such as phone numbers and server addresses in environment variables when deploying.
