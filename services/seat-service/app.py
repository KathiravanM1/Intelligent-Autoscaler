from flask import Flask
import time
import random

app = Flask(__name__)

@app.route("/seat")
def seat():
    time.sleep(random.uniform(5, 10))
    return "Seat registered\n"

@app.route("/health")
def health():
    return "OK\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
