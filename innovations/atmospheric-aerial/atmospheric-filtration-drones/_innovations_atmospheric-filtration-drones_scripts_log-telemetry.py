# 📊 Drone Telemetry Logger
# File: log-telemetry.py

"""
Collects, timestamps, and stores telemetry from sensors, AI state, and swarm data.
Supports optional uplink and IPFS persistence.
"""

import json
import os
import time
from datetime import datetime
from modules.state import DroneState
from modules.ipfs import upload_log

LOG_DIR = "/data/telemetry"
UPLOAD_INTERVAL = 300  # seconds

def ensure_log_dir():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

def write_log_entry(state: DroneState):
    now = datetime.utcnow().isoformat()
    entry = {
        "timestamp": now,
        "drone_id": state.drone_id,
        "position": state.position,
        "battery": state.battery_level,
        "task": state.active_task,
        "pm25": state.environment["pm25"],
        "altitude": state.altitude
    }
    filename = f"{LOG_DIR}/{state.drone_id}_{int(time.time())}.json"
    with open(filename, "w") as f:
        json.dump(entry, f)
    return filename

def log_loop():
    state = DroneState()
    ensure_log_dir()
    print("[LOGGER] Telemetry logging started...")

    while True:
        file_path = write_log_entry(state)
        print(f"[LOGGER] Wrote {file_path}")
        time.sleep(UPLOAD_INTERVAL)
        upload_log(file_path)

if __name__ == "__main__":
    log_loop()
