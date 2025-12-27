from flask import Flask
import time
import random

app = Flask(__name__)

@app.route("/courses")
def courses():
    time.sleep(random.uniform(0.15, 0.3))
    return "Course list returned\n"

@app.route("/health")
def health():
    return "OK\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
