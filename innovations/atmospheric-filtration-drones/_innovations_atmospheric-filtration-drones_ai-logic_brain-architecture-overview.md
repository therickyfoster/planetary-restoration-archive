# 🧠 AI Logic Core — Brain Architecture Overview

This document outlines the neural and rules-based decision architecture powering the Atmospheric Filtration Drone Swarm's autonomous operation, coordination, and emergency fallback logic.

---

## 🧩 Architecture Overview

The drone AI is based on a hybrid **neuro-symbolic architecture**:

```
                    +-----------------------+
                    |  Sensor Fusion Layer  |
                    +-----------------------+
                                |
                   +--------------------------+
                   | Preprocessing + Filtering |
                   +--------------------------+
                                |
               +---------------------------------+
               | Neural Inference Core (TinyML) |
               +---------------------------------+
                                |
            +----------------------------------------+
            | Behavior Selector + Task Scheduler     |
            +----------------------------------------+
                                |
          +----------------------------------------------+
          | Low-Level Control / Swarm Coordination Logic |
          +----------------------------------------------+
                                |
                   +------------------------+
                   | Actuator + System I/O |
                   +------------------------+
```

---

## ⚙️ Core Modules

- **Sensor Fusion Layer**  
  Combines GPS, barometer, air quality (PM2.5/PM10), wind, temp, and internal telemetry into a unified state vector.

- **Preprocessing**  
  Smooths sensor input, filters noise, and encodes data for neural input or symbolic evaluation.

- **Neural Inference Core**  
  A small edge-optimized neural net (e.g. TinyML or Edge TPU) for tasks like:
  - Anomaly detection
  - Filtration target classification
  - Predictive pathing
  - Atmospheric pattern recognition

- **Behavior Selector**  
  Chooses between defined high-level behaviors:
  - `filter-zone-scan`
  - `air-column-stabilization`
  - `recharge-dock-seek`
  - `swarm-coordination`
  - `hold-position`
  - `emergency-recovery`

- **Swarm Coordination Layer**  
  Uses basic consensus protocols, line-of-sight clustering, and signal strength triangulation to coordinate swarm movements.

- **Fallback Ruleset (Failsafe AI)**  
  When the neural core fails, symbolic rules take over:
  - `if battery < 10% → land_safe_zone()`
  - `if comms_lost > 15s → return_to_base()`
  - `if smoke_detected → ascend_to_clear_altitude()`

---

## 🧠 Model Type

- TinyML (quantized 8-bit) LSTM model for air quality predictions.
- Optional: Edge TPU model for high-speed multi-label classification.

---

## 🧪 Training Sources

- Real-time drone-collected datasets (uploaded nightly)
- Public urban AQI datasets
- Localized PM distribution heatmaps

---

**Author:** Planetary Restoration OS  
**License:** CC BY-NC-SA 4.0  
