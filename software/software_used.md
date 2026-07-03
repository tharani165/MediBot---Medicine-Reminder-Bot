# Software Used

- Python 3.10+
- Flask 3.0 — web server and REST API
- Requests — HTTP calls between the Flask server and the Android device
- Jinja2 (bundled with Flask) — server-rendered HTML templates
- HTML5 / CSS3 / vanilla JavaScript — reminder dashboard UI
- SL4A (Scripting Layer for Android) `androidhelper` module — places calls and reads call logs on the Android device; a mock implementation is used automatically when SL4A isn't available (e.g. during local development)
