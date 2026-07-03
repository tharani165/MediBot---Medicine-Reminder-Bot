import os
import time

import flask
import requests
from flask import request, jsonify

try:
    import androidhelper
    droid = androidhelper.Android()
    IS_MOCK = False
except ImportError:
    IS_MOCK = True

    class MockAndroid:
        """Stand-in for SL4A's androidhelper.Android() when not running on an Android device."""

        def phoneCall(self, phone_number):
            print(f"[MOCK] Would call {phone_number}")

        def ttsSpeak(self, text):
            print(f"[MOCK] TTS: {text}")

        def getCallLog(self, _count=1):
            class Result:
                result = [{"type": 2}]  # 2 == treated as "answered" by this app

            return Result()

    droid = MockAndroid()
    print("androidhelper not found - running with a mock Android interface (no real calls will be placed).")

app = flask.Flask(__name__)
FLASK_SERVER = os.getenv("FLASK_SERVER", "http://127.0.0.1:5000")


def play_alert_beep():
    """Audible alert on the Android device right before the reminder call is placed."""
    droid.ttsSpeak("Beep. Beep. Medicine reminder call incoming.")


@app.route("/make_call", methods=["GET"])
def make_call():
    phone_number = request.args.get("phone")
    if not phone_number:
        return jsonify({"message": "Phone number missing"}), 400

    play_alert_beep()
    droid.phoneCall(phone_number)

    # Wait for call to complete
    time.sleep(2 if IS_MOCK else 30)

    # Check Call Status
    logs = droid.getCallLog(1).result
    if logs:
        last_call = logs[0]
        call_type = last_call["type"]
        status = "answered" if call_type == 2 else "rejected"

        # Send status to Flask
        requests.post(f"{FLASK_SERVER}/call_status", json={"phone": phone_number, "status": status}, timeout=5)

    return jsonify({"message": "Call initiated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5050")))
