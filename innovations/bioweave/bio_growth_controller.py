"""
BioWeave™ Growth Controller
Controls moisture, temperature, and nutrient release for optimal mycelial growth within regenerative mesh structures.
"""

import time
import random

class BioGrowthController:
    def __init__(self):
        self.temperature = 24  # in Celsius
        self.humidity = 80     # in %
        self.nutrient_release = False
        self.status = "Idle"

    def monitor_environment(self):
        # Simulated sensor values
        self.temperature += random.uniform(-0.5, 0.5)
        self.humidity += random.uniform(-1, 1)
        print(f"Temp: {self.temperature:.2f}°C | Humidity: {self.humidity:.2f}%")

    def regulate_conditions(self):
        if self.temperature < 22 or self.humidity < 75:
            self.nutrient_release = True
            self.status = "Boosting growth"
            print("Conditions low — triggering nutrient capsule.")
        else:
            self.nutrient_release = False
            self.status = "Optimal"
            print("Conditions optimal — no action taken.")

    def log_status(self):
        log = {
            "temp": round(self.temperature, 2),
            "humidity": round(self.humidity, 2),
            "nutrient_release": self.nutrient_release,
            "status": self.status,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        print(f"[LOG] {log}")
        return log

    def run_cycle(self):
        print("Running growth controller cycle...")
        self.monitor_environment()
        self.regulate_conditions()
        return self.log_status()

# Example usage
if __name__ == "__main__":
    controller = BioGrowthController()
    for _ in range(3):
        controller.run_cycle()
        time.sleep(2)
