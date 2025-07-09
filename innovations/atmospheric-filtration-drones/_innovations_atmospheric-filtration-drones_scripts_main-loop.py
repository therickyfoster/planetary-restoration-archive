# 🔁 Main Drone Execution Loop
# File: main-loop.py

"""
Central runtime that manages AI decisions, swarm sync, task switching,
and battery-aware behaviors. Runs continuously until interrupted.
"""

import time
from modules.state import DroneState
from modules.model import load_model, infer_action
from modules.swarm import sync_status, update_peers
from modules.mission import execute_task, fallback_check

LOOP_INTERVAL = 2  # seconds

def main_loop():
    print("[MAIN LOOP] Starting execution loop...")

    # Initialize state
    state = DroneState()
    model = load_model()

    if not model:
        print("[MAIN LOOP WARNING] AI model failed to load. Fallback mode only.")

    # Main loop
    while True:
        if fallback_check(state):
            print("[MAIN LOOP] Fallback mode engaged.")
            continue  # Fallback script handles decision

        if model:
            action = infer_action(model, state.get_inputs())
            state.active_task = action
            execute_task(action, state)
        else:
            execute_task("idle-hold", state)

        sync_status(state)
        update_peers(state)

        print(f"[MAIN LOOP] Task: {state.active_task}, Battery: {state.battery_level:.1f}%")
        time.sleep(LOOP_INTERVAL)

if __name__ == "__main__":
    main_loop()
