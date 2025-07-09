# ⏱️ Task Scheduler for Drone AI Logic
# File: task-scheduler.py

"""
Schedules high-level drone behaviors based on priority, sensor input,
battery levels, and mission objectives. Executes one task at a time per loop.
"""

from modules.state import DroneState
from modules.behaviors import (
    execute_filter_scan,
    execute_air_column_hold,
    execute_recharge_seek,
    execute_swarm_formation,
    execute_idle_hold,
    execute_emergency_fallback
)

# Task priority (lower = higher priority)
TASK_PRIORITY = {
    "emergency-fallback": 0,
    "recharge-dock-seek": 1,
    "filter-zone-scan": 2,
    "air-column-hold": 3,
    "swarm-formation": 4,
    "idle-hold": 5,
}

def choose_next_task(state: DroneState) -> str:
    if state.safe_mode or state.emergency_triggered:
        return "emergency-fallback"
    if state.battery_level < 12:
        return "recharge-dock-seek"
    if state.environment["pm25"] > 90:
        return "filter-zone-scan"
    if state.environment["wind_speed"] > 8:
        return "air-column-hold"
    if not state.is_leader:
        return "swarm-formation"
    return "idle-hold"

def run_task_loop(state: DroneState):
    while True:
        task = choose_next_task(state)
        state.active_task = task

        if task == "filter-zone-scan":
            execute_filter_scan(state)
        elif task == "air-column-hold":
            execute_air_column_hold(state)
        elif task == "recharge-dock-seek":
            execute_recharge_seek(state)
        elif task == "swarm-formation":
            execute_swarm_formation(state)
        elif task == "idle-hold":
            execute_idle_hold(state)
        elif task == "emergency-fallback":
            execute_emergency_fallback(state)
        else:
            print(f"Unknown task: {task}")

        # Simulated loop delay
        state.sync_status()
        state.log_frame()
