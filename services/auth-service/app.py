from flask import Flask
import time
import random

app = Flask(__name__)

@app.route("/login")
def login():
    time.sleep(random.uniform(0.1, 0.25))
    return "Login successful\n"

@app.route("/health")
def health():
    return "OK\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
