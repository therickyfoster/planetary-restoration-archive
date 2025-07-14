# 👑 Swarm Leader Election Algorithm
# File: leader-election.py

"""
This script defines the swarm's decentralized leader election protocol
based on battery level, uptime, signal clarity, and fallback logic.
"""

import time
import random
from modules.state import DroneState
from modules.network import broadcast, receive

def elect_leader(drone_id, state: DroneState, peers):
    """
    Elects a leader from current swarm snapshot.
    Peers should be a list of dicts with: {id, battery, uptime, rssi}
    """

    candidates = peers + [{
        "id": drone_id,
        "battery": state.battery_level,
        "uptime": state.uptime,
        "rssi": state.signal_strength
    }]

    def score(peer):
        return (
            peer["battery"] * 0.4 +
            peer["uptime"] * 0.3 +
            peer["rssi"] * 0.3
        )

    sorted_candidates = sorted(candidates, key=score, reverse=True)
    leader = sorted_candidates[0]["id"]

    if leader == drone_id:
        state.is_leader = True
        broadcast({
            "type": "role-change",
            "leader": drone_id,
            "timestamp": int(time.time())
        })
        print(f"[LEADER] This drone ({drone_id}) elected as new leader.")
    else:
        state.is_leader = False
        state.current_leader = leader
        print(f"[FOLLOWER] Drone {drone_id} following {leader}.")

    return leader

# Example usage
if __name__ == "__main__":
    dummy_peers = [
        {"id": "drone-A1", "battery": 88, "uptime": 1200, "rssi": -67},
        {"id": "drone-B3", "battery": 91, "uptime": 900, "rssi": -70}
    ]

    my_state = DroneState()
    my_state.battery_level = 94
    my_state.uptime = 1500
    my_state.signal_strength = -62

    elect_leader("drone-Z9", my_state, dummy_peers)
