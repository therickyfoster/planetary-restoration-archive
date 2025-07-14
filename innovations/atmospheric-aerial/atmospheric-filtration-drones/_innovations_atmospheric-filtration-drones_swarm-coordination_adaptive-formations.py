# 🧭 Adaptive Swarm Formation Logic
# File: adaptive-formations.py

"""
Determines optimal spatial formations for the swarm based on environmental
conditions, drone count, and task goals. Ensures safe distance and coverage.
"""

import math
from modules.state import DroneState

def compute_formation(drone_count, mode="grid", radius=30):
    positions = []

    if mode == "circle":
        for i in range(drone_count):
            angle = 2 * math.pi * i / drone_count
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            positions.append((x, y))
    elif mode == "v":
        offset = radius / 2
        for i in range(drone_count):
            x = i * offset
            y = abs(i - drone_count // 2) * offset
            positions.append((x, y))
    elif mode == "line":
        for i in range(drone_count):
            positions.append((i * radius, 0))
    else:  # grid (default)
        side = int(math.sqrt(drone_count)) + 1
        for i in range(drone_count):
            x = (i % side) * radius
            y = (i // side) * radius
            positions.append((x, y))

    return positions

def assign_formation(state: DroneState, neighbors):
    count = len(neighbors) + 1
    mode = "grid"

    if state.environment["wind_speed"] > 10:
        mode = "v"
    elif state.environment["pm25"] > 100:
        mode = "circle"

    formation = compute_formation(count, mode=mode)
    return formation

# Example usage
if __name__ == "__main__":
    state = DroneState()
    state.environment["pm25"] = 115
    state.environment["wind_speed"] = 4
    result = assign_formation(state, neighbors=["A1", "B2", "C3", "D4"])
    for i, pos in enumerate(result):
        print(f"Drone {i+1}: Position {pos}")
