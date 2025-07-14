# 🧰 HydroLoop™ – Maintenance & Safety Guide  
**File:** maintenance_guide.md  
**Version:** v1.0  
**Linked Files:** [materials_list.txt](./materials_list.txt) | [dao_integration.md](./dao_integration.md)

---

## 🧭 Overview  

This guide outlines daily, weekly, and monthly tasks required to keep HydroLoop™ operating efficiently and safely. Designed for **low-tech conditions**, **non-expert users**, and **off-grid resilience**.

---

## 🧽 Daily Routine (1–5 min)

| Task                            | Tool Needed         | Notes                                     |
|---------------------------------|---------------------|-------------------------------------------|
| Check water output clarity      | Glass jar           | Look for cloudiness or odor               |
| Confirm intake not blocked      | Visual check        | Ensure no debris in water intake hose     |
| Inspect condensate line         | Fingers only        | Feel for heat along coil path             |

✅ *Log into DAO (manual or auto) if enabled.*

---

## 🗓️ Weekly Tasks (5–15 min)

| Task                              | Tool                | Notes                                     |
|-----------------------------------|---------------------|-------------------------------------------|
| Flush greywater lines             | Inline valve        | Rotate to drain into greywater bin        |
| Wipe condensate coil              | Cloth + vinegar     | Prevent salt buildup on outer surface     |
| Inspect seals + joints            | Wrench or pliers    | Tighten loose fittings if found           |
| Dump and rinse filter bed        | Bucket + gloves     | Use clean water to flush sediment         |

> *Field agents should document events with timestamps in DAO logs (if used).*

---

## 📆 Monthly Deep Maintenance

| Task                              | Tool / Supply       | Notes                                     |
|-----------------------------------|---------------------|-------------------------------------------|
| Disassemble filter unit           | Screwdriver         | Check for clogs, organic residue          |
| Replace fiber/charcoal bed        | Filter media        | Use local materials where possible        |
| Clean solar collector surface     | Soft brush          | Avoid scratching, wipe with clean water   |
| Test sensor data accuracy         | Multimeter / script | Compare to known source or reset unit     |
| Inspect frame + housing           | Visual / light tap  | Look for corrosion, rust, or warping      |

---

## 🛠️ Common Issues + Fixes

| Symptom                     | Probable Cause           | Fix                                           |
|-----------------------------|---------------------------|-----------------------------------------------|
| Low water output            | Cloudy day / dirty coil   | Clean coil + check intake                     |
| Overflow in greywater tank  | Blocked loop or filter    | Drain loop + rinse filter bed                |
| Water smells / discolored   | Biofilm in greywater      | Full flush + charcoal refresh                 |
| Drip leak at T-junction     | Loose seal                | Tighten clamp / reseat gasket                 |
| DAO log not updating        | Sensor error              | Reset Termux script or reboot ESP32           |

---

## 🔐 Safety Checklist

✅ Use gloves when touching greywater unit  
✅ Never drink water from unverified loop directly  
✅ Label potable and greywater lines clearly  
✅ Include a **manual bypass valve** if DAO-controlled  
✅ Ensure kids or animals can't access exposed parts

---

## 📂 Files & Docs to Update (Monthly)

- [`dao_log.json`](./dao_log.json) – Operational metadata  
- [`sensor_diag.log`](./scripts/sensor_diag.log) – Optional CLI output  
- [`city-blueprint.yaml`](../cities/SampleCity/city-blueprint.yaml) – Integration ref

---

## 🧩 Recommended Spare Parts (per 6 months)

| Part                         | Quantity | Notes                                |
|------------------------------|----------|--------------------------------------|
| Silicone tubing (1m)         | 2x       | For emergency replacement            |
| Filter media (charcoal/fiber)| 1 set    | Locally sourced preferred            |
| Pipe sealant / gasket set    | 1x       | For emergency leak repair            |
| 9V battery or solar cell     | 1x       | If off-grid sensor module used       |
| Sensor board (ESP32 optional)| 1x       | Cheap to swap out if damaged         |

---

## 💬 Closing Note

HydroLoop™ is designed to run for **years**, not days — even with minimal upkeep.  
A few minutes of attention each week ensures your system stays clean, sovereign, and effective.

> “Prevent collapse by maintaining flow.”  
> — *The Steward*
