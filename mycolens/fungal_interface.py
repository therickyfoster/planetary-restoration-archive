"""
MycoLens™ Fungal Interface
Translates analog signals from fungal networks into digital patterns for analysis.
"""

import time
import random

class FungalSignalProcessor:
    def __init__(self):
        self.baseline_voltage = 0.05  # Simulated mV base from healthy mycelium
        self.signal_threshold = 0.12  # Activation threshold in mV
        self.signal_log = []

    def read_voltage(self):
        # Simulate bioelectric fluctuation
        voltage = round(self.baseline_voltage + random.uniform(-0.02, 0.1), 4)
        print(f"Signal voltage: {voltage} mV")
        return voltage

    def interpret_signal(self, voltage):
        if voltage > self.signal_threshold:
            print("↯ High signal spike detected – possible stress or toxin")
            return "ALERT"
        elif voltage < 0:
            print("↓ Abnormal drop detected – network instability")
            return "DROP"
        else:
            print("✓ Normal fluctuation")
            return "NORMAL"

    def log_signal(self, voltage, status):
        entry = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "voltage_mV": voltage,
            "status": status
        }
        self.signal_log.append(entry)
        print(f"[LOG] {entry}")
        return entry

    def run_cycle(self):
        voltage = self.read_voltage()
        status = self.interpret_signal(voltage)
        return self.log_signal(voltage, status)

# Example simulation
if __name__ == "__main__":
    interface = FungalSignalProcessor()
    for _ in range(5):
        interface.run_cycle()
        time.sleep(2)
