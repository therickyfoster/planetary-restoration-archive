# 📡 Swarm Coordination Protocol Specification

This document defines the communication and behavior protocol used by drones in the Atmospheric Filtration Swarm to maintain cohesion, share environmental intelligence, and execute distributed operations.

---

## 🌐 Communication Protocol

**Transport Layer:**  
- LoRa Mesh (primary, up to 10km LOS)
- 5.8GHz short-range mesh (secondary, up to 800m)
- Backup: Wi-Fi direct broadcast (up to 200m)

**Message Format (JSON):**

```json
{
  "id": "drone-AX21",
  "type": "status-update",
  "pos": [49.28, -123.12, 155],
  "battery": 78,
  "pm25": 96,
  "task": "filter-zone-scan",
  "leader": "drone-AX20",
  "timestamp": 1723759200
}
```

---

## 🤝 Message Types

| Type               | Description                          |
|--------------------|--------------------------------------|
| `status-update`    | Heartbeat with all telemetry         |
| `task-declare`     | Announces drone's self-assigned task |
| `role-change`      | Leader change, backup notice         |
| `formation-call`   | Group maneuver request               |
| `ack`              | Acknowledgment of command            |
| `emergency-ping`   | Failsafe beacon                      |

---

## 🧠 Coordination Logic

- Drones broadcast `status-update` every 3–5 seconds.
- If no update is received from a neighbor after 15 seconds, the drone marks that neighbor as "offline".
- Nearest drone with >70% battery becomes fallback leader if leader lost.
- Formations are chosen based on:
  - Wind
  - Density of PM2.5
  - Number of drones in zone

---

## 🧬 Mesh Layer Protocol

- LoRa mesh uses dynamic routing tables
- Routing prioritizes lowest signal loss path
- Each drone has a unique ID and `trusted` key

---

## 🔒 Security & Resilience

- All packets signed with a swarm certificate
- Backup memory stores last 5 minutes of swarm messages
- Auto-drop malformed or spoofed messages

---

**Version:** 1.0  
**Author:** Planetary Restoration OS  
**License:** CC BY-NC-SA 4.0  
