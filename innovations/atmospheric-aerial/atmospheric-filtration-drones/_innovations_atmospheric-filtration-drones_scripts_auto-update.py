# 🔄 Drone Auto-Update Script
# File: auto-update.py

"""
Checks for updates over secure channel, downloads new script packs, and
applies patch if integrity verified. Can update over Wi-Fi, LoRa, or USB.
"""

import os
import json
import time
import hashlib
from modules.network import check_for_update, download_patch
from modules.system import apply_patch, verify_signature

UPDATE_CHECK_INTERVAL = 3600  # 1 hour

def get_current_version():
    try:
        with open("/etc/drone_version.json") as f:
            return json.load(f).get("version", "0.0.0")
    except:
        return "0.0.0"

def auto_update_loop():
    print("[AUTO-UPDATE] Starting update monitor...")
    current_version = get_current_version()

    while True:
        print("[AUTO-UPDATE] Checking for updates...")
        update_info = check_for_update(current_version)
        if not update_info:
            print("[AUTO-UPDATE] No update available.")
        else:
            patch_url = update_info["url"]
            expected_hash = update_info["sha256"]
            print(f"[AUTO-UPDATE] New version found: {update_info['version']}")
            patch_file = download_patch(patch_url)

            if not patch_file:
                print("[AUTO-UPDATE] Patch download failed.")
            elif verify_signature(patch_file, expected_hash):
                apply_patch(patch_file)
                print("[AUTO-UPDATE] Patch applied successfully.")
                current_version = update_info["version"]
            else:
                print("[AUTO-UPDATE] Patch failed verification.")

        time.sleep(UPDATE_CHECK_INTERVAL)

if __name__ == "__main__":
    auto_update_loop()
