# 📡 Group Communication Utilities
# File: group-comms.py

"""
Utility functions and lightweight messaging framework to allow
peer-to-peer and broadcast messaging between swarm members.
"""

import json
import socket
import threading
import time

MULTICAST_ADDR = "239.255.0.1"
PORT = 5007
BUFFER_SIZE = 1024

class SwarmComms:
    def __init__(self, drone_id):
        self.drone_id = drone_id
        self.running = False
        self.received = []

    def start_listener(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("", PORT))
        mreq = socket.inet_aton(MULTICAST_ADDR) + socket.inet_aton("0.0.0.0")
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        self.running = True
        threading.Thread(target=self.listen_loop, daemon=True).start()

    def listen_loop(self):
        while self.running:
            try:
                data, _ = self.sock.recvfrom(BUFFER_SIZE)
                msg = json.loads(data.decode("utf-8"))
                if msg.get("id") != self.drone_id:
                    self.received.append(msg)
            except Exception as e:
                print(f"[COMM ERROR] {e}")

    def send(self, message_dict):
        message_dict["id"] = self.drone_id
        message = json.dumps(message_dict).encode("utf-8")
        self.sock.sendto(message, (MULTICAST_ADDR, PORT))

    def stop(self):
        self.running = False
        self.sock.close()

# Example
if __name__ == "__main__":
    drone_id = "drone-X7"
    comms = SwarmComms(drone_id)
    comms.start_listener()
    comms.send({"type": "hello", "msg": "Ready"})
    time.sleep(3)
    print("[RECEIVED]", comms.received)
