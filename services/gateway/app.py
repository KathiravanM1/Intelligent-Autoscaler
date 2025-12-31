from flask import Flask
import requests

app = Flask(__name__)

@app.route("/register")
def register():
    requests.get("http://auth-service/login")
    requests.get("http://course-service/courses")
    requests.get("http://seat-service/seat")
    return "Registration complete\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
