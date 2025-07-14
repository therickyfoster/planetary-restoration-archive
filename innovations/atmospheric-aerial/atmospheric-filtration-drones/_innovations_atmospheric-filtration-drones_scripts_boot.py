# 🚀 Drone Boot Initialization Script
# File: boot.py

"""
Executed at power-on. Handles self-diagnostics, environment readiness,
connection to swarm, and safe activation of AI and motion systems.
"""

import time
from modules.state import DroneState
from modules.network import connect_to_swarm
from modules.diagnostics import run_self_test

def initialize_system():
    print("[BOOT] Starting boot sequence...")

    # Step 1: Run self-check
    test_result = run_self_test()
    if not test_result["passed"]:
        print("[BOOT ERROR] Self-test failed.")
        print(" -", test_result["error"])
        return False

    # Step 2: Load drone state
    state = DroneState()
    state.load()

    # Step 3: Connect to swarm
    connected = connect_to_swarm(state)
    if not connected:
        print("[BOOT WARNING] Swarm connection failed. Entering solo mode.")
        state.solo_mode = True
    else:
        print("[BOOT] Swarm connection successful.")

    # Step 4: Activate system
    state.ready = True
    print("[BOOT] System initialized. AI control loop ready.")
    return True

# Entry point
if __name__ == "__main__":
    success = initialize_system()
    if not success:
        print("[BOOT] Shutting down or retrying as per policy...")
    else:
        print("[BOOT COMPLETE] Drone is ready for AI engagement.")
