# 🌐 Sensor Fusion Engine
# File: sensor-fusion-engine.py

"""
Combines multiple onboard sensor streams into a single fused environmental state.
Used by AI core, decision logic, and swarm coordination layers.
"""

import numpy as np
import time

class SensorFusion:
    def __init__(self):
        self.state = {
            "pm25": None,
            "pm10": None,
            "temperature": None,
            "humidity": None,
            "altitude": None,
            "gps": None,
            "wind_speed": None,
            "battery": None,
            "timestamp": None
        }

    def read_all_sensors(self):
        # Mock sensor values – replace with hardware interfaces
        self.state["pm25"] = self.mock_sensor("pm25", 40, 10)
        self.state["pm10"] = self.mock_sensor("pm10", 50, 15)
        self.state["temperature"] = self.mock_sensor("temperature", 24, 2)
        self.state["humidity"] = self.mock_sensor("humidity", 45, 5)
        self.state["altitude"] = self.mock_sensor("altitude", 150, 5)
        self.state["gps"] = {"lat": 49.28, "lon": -123.12}
        self.state["wind_speed"] = self.mock_sensor("wind", 5, 2)
        self.state["battery"] = self.mock_sensor("battery", 78, 1)
        self.state["timestamp"] = time.time()
        return self.state

    def mock_sensor(self, name, base, noise):
        return round(np.random.normal(base, noise), 2)

    def get_fused_state(self):
        self.read_all_sensors()
        return self.state

# Example usage
if __name__ == "__main__":
    fusion = SensorFusion()
    state = fusion.get_fused_state()
    for k, v in state.items():
        print(f"{k}: {v}")
