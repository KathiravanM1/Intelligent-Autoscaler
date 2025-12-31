from flask import Flask
import time
import logging
import sys

# Disable Flask / Werkzeug access logs
log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route("/seat")
def seat():
    start = time.time()

    # simulate slowness
    time.sleep(2)

    latency = time.time() - start

    print(f"[SEAT] latency={latency:.2f}s", flush=True)

    return "Seat allocated\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
