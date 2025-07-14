# 🤖 Model Inference Loop
# File: model-inference-loop.py

"""
Runs onboard AI inference using a preloaded TinyML or Edge TPU model
to determine target behavior based on live sensor inputs.
"""

import time
import numpy as np
from modules.state import DroneState
from modules.model import load_model, infer_action

class InferenceLoop:
    def __init__(self):
        self.model = load_model()
        self.state = DroneState()
        self.last_action = None

    def preprocess_inputs(self):
        inputs = [
            self.state.environment["pm25"] / 200,
            self.state.environment["pm10"] / 200,
            self.state.environment["temperature"] / 50,
            self.state.environment["humidity"] / 100,
            self.state.environment["wind_speed"] / 20,
            self.state.battery_level / 100,
        ]
        return np.array(inputs).reshape(1, -1)

    def run_loop(self):
        if not self.model:
            print("No model loaded. Skipping inference.")
            return "idle-hold"

        inputs = self.preprocess_inputs()
        prediction = infer_action(self.model, inputs)

        # Convert model output to task label
        task_map = {
            0: "idle-hold",
            1: "filter-zone-scan",
            2: "recharge-dock-seek",
            3: "swarm-formation",
            4: "air-column-hold",
            5: "emergency-fallback"
        }

        task = task_map.get(prediction.argmax(), "idle-hold")
        self.last_action = task
        return task

# Example usage
if __name__ == "__main__":
    loop = InferenceLoop()
    while True:
        task = loop.run_loop()
        print(f"🧠 Inference chose: {task}")
        time.sleep(2)
