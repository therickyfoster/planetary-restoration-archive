# 🔄 Swarm Behavior Synchronization
# File: behavior-sync.py

"""
Handles real-time coordination of drone behavior across the swarm.
Ensures consistency of formation, task execution, and fallback triggers.
"""

import time
from modules.network import broadcast, listen_for
from modules.state import DroneState

SYNC_INTERVAL = 5  # seconds

def sync_behavior(state: DroneState):
    message = {
        "type": "task-declare",
        "id": state.drone_id,
        "task": state.active_task,
        "pos": state.position,
        "timestamp": int(time.time())
    }
    broadcast(message)

def update_from_peers(state: DroneState):
    peer_messages = listen_for(timeout=2)
    for msg in peer_messages:
        if msg.get("type") == "task-declare":
            peer_id = msg.get("id")
            task = msg.get("task")
            state.swarm_tasks[peer_id] = {
                "task": task,
                "timestamp": msg.get("timestamp")
            }

def behavior_sync_loop(state: DroneState):
    while True:
        sync_behavior(state)
        update_from_peers(state)
        print(f"[SYNC] Active task: {state.active_task}, Swarm: {state.swarm_tasks}")
        time.sleep(SYNC_INTERVAL)

# Example usage
if __name__ == "__main__":
    drone_state = DroneState()
    drone_state.drone_id = "drone-Z9"
    drone_state.active_task = "filter-zone-scan"
    behavior_sync_loop(drone_state)
