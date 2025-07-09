# 🧠 Logic Core Initialization Script
# File: logic-core-init.py

"""
This script initializes all AI-related modules, sensors, and state management
for the Atmospheric Filtration Drone’s AI logic core. Should run at boot time.
"""

import time
import logging
from modules.sensor import init_sensors
from modules.network import init_network
from modules.model import load_model
from modules.state import DroneState

# -------------------------------------------------------
# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("logic-init")

# -------------------------------------------------------
# Initialize global drone state
state = DroneState()

def startup_sequence():
    logger.info("=== AI Logic Core Booting ===")

    logger.info("Initializing sensors...")
    if init_sensors(state):
        logger.info("Sensors initialized successfully.")
    else:
        logger.error("Sensor initialization failed. Entering safe mode.")
        state.safe_mode = True

    logger.info("Loading AI model...")
    model = load_model()
    if model:
        logger.info("AI model loaded.")
        state.model = model
    else:
        logger.warning("Failed to load AI model. Continuing in fallback mode.")
        state.model = None
        state.safe_mode = True

    logger.info("Establishing network links...")
    if init_network(state):
        logger.info("Network link established.")
    else:
        logger.warning("Network not found. Operating in solo mode.")
        state.network_connected = False

    logger.info("Startup sequence complete.")
    return state

if __name__ == "__main__":
    state = startup_sequence()
    logger.info(f"Drone State: {state.to_json()}")
