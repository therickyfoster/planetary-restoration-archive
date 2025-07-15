"""
AeroHydra™ Mesh Controller
Controls humidity sensing and adaptive mesh behavior for optimal water harvesting.
"""

import time
import random

class MeshController:
    def __init__(self):
        self.humidity = 45  # Initial humidity %
        self.temperature = 27  # Celsius
        self.clean_cycle_active = False
        self.water_collected_ml = 0

    def read_sensors(self):
        # Simulate environmental fluctuations
        self.humidity += random.uniform(-2, 2)
        self.temperature += random.uniform(-0.5, 0.5)
        print(f"Humidity: {self.humidity:.1f}% | Temp: {self.temperature:.1f}°C")

    def regulate_mesh(self):
        if self.humidity > 40:
            water_yield = (self.humidity - 30) * 0.5
            self.water_collected_ml += water_yield
            print(f"Condensation active: {water_yield:.1f}ml collected")
        else:
            print("Humidity too low for effective harvesting.")

    def clean_mesh(self):
        self.clean_cycle_active = True
        print("Thermal cleaning pulse initiated...")
        time.sleep(1)  # Simulated delay
        self.clean_cycle_active = False
        print("Cleaning complete.")

    def log_status(self):
        return {
            "humidity": round(self.humidity, 1),
            "temperature": round(self.temperature, 1),
            "water_collected_ml": round(self.water_collected_ml, 1),
            "cleaning": self.clean_cycle_active
        }

    def run_cycle(self):
        self.read_sensors()
        self.regulate_mesh()
        if random.random() < 0.2:
            self.clean_mesh()
        return self.log_status()

# Example simulation loop
if __name__ == "__main__":
    controller = MeshController()
    for _ in range(3):
        result = controller.run_cycle()
        print(f"[LOG] {result}\n")
        time.sleep(2)
