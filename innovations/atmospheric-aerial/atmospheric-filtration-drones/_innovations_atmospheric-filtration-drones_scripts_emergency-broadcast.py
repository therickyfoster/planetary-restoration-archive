# 📣 Emergency Beacon Broadcast
# File: emergency-broadcast.py

"""
Standalone script to trigger an emergency broadcast to the swarm and optionally
ground station if available. Used during hardware failure, isolation, or distress.
"""

import json
import socket
import time
from modules.state import DroneState

MULTICAST_ADDR = "239.255.0.1"
PORT = 5007

def send_emergency_broadcast(drone_id, reason="unknown"):
    message = {
        "id": drone_id,
        "type": "emergency-ping",
        "reason": reason,
        "timestamp": int(time.time())
    }

    encoded = json.dumps(message).encode("utf-8")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    sock.sendto(encoded, (MULTICAST_ADDR, PORT))

    print(f"[EMERGENCY BROADCAST] Sent by {drone_id}: {reason}")

if __name__ == "__main__":
    state = DroneState()
    send_emergency_broadcast(state.drone_id, reason="manual_trigger")
