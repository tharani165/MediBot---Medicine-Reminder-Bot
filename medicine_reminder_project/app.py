
from flask import Flask, render_template, request, jsonify
import json
import os
import requests
from datetime import datetime
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "data.json"
ANDROID_SERVER = os.getenv("ANDROID_SERVER", "http://YOUR_ANDROID_IP:5000")

DATA_DIR.mkdir(exist_ok=True)


# Load JSON Data
def load_data():
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


# Save JSON Data
def save_data(data):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# Home Page - Display Form
@app.route("/")
def home():
    patients = load_data()
    current_time = datetime.now().strftime("%H:%M")
    active_patients = [p for p in patients if p.get("time", "") > current_time]
    finished_patients = [p for p in patients if p.get("time", "") <= current_time]
    return render_template(
        "index.html",
        active_patients=active_patients,
        finished_patients=finished_patients,
    )


# API to Add Medicine Reminder
@app.route("/add_reminder", methods=["POST"])
def add_reminder():
    data = load_data()
    patient_name = request.form["name"]
    phone = request.form["phone"]
    reminder_time = request.form["time"]

    medicine_names = request.form.getlist("medicine_name")
    dosages = request.form.getlist("dosage")
    medicines = [
        {"name": med_name.strip(), "dosage": dosage.strip()}
        for med_name, dosage in zip(medicine_names, dosages)
        if med_name.strip()
    ]

    data.append({
        "name": patient_name,
        "phone": phone,
        "time": reminder_time,
        "medicines": medicines,
    })
    save_data(data)
    return jsonify({"message": "Reminder Added!"}), 200


# API to Trigger Calls Based on Time
@app.route("/trigger_calls")
def trigger_calls():
    data = load_data()
    current_time = datetime.now().strftime("%H:%M")

    for patient in data:
        if patient["time"] == current_time:
            print(f"Calling {patient['name']} at {patient['phone']}...")
            requests.get(f"{ANDROID_SERVER}/make_call?phone={patient['phone']}", timeout=5)

    return jsonify({"message": "Calls Triggered!"}), 200


# API to Receive Call Status
@app.route("/call_status", methods=["POST"])
def call_status():
    status = request.json.get("status")
    phone = request.json.get("phone")

    if status == "answered":
        print(f"{phone} answered the call.")
    elif status == "rejected":
        print(f"{phone} rejected the call.")

    return jsonify({"message": "Call status received"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
