# ⚠️ Failsafe Monitor
# File: failsafe-monitor.py

"""
Monitors critical safety thresholds and hardware anomalies.
Triggers emergency fallback procedures or soft shutdowns.
"""

import time
from modules.state import DroneState
from modules.fallback import engage_emergency_mode
from modules.sensors import read_sensor

CHECK_INTERVAL = 1  # seconds

def failsafe_monitor():
    state = DroneState()

    print("[FAILSAFE] Starting monitor...")

    while True:
        # Check battery
        if state.battery_level < 10:
            print("[FAILSAFE] Battery critically low.")
            engage_emergency_mode(state, reason="low_battery")
            continue

        # Sensor fault detection
        failed_sensors = []
        for sensor in ["gps", "imu", "pm25", "pm10"]:
            if not read_sensor(sensor):
                failed_sensors.append(sensor)

        if len(failed_sensors) >= 2:
            print(f"[FAILSAFE] Multiple sensor failures: {failed_sensors}")
            engage_emergency_mode(state, reason="sensor_failure")

        # Altitude ceiling
        if state.altitude > 300:
            print("[FAILSAFE] Altitude above safe threshold.")
            engage_emergency_mode(state, reason="altitude_limit")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    failsafe_monitor()
