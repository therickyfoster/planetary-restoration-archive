# 🌡️ Part: Climate Telemetry Pod v1

Self-contained payload module for capturing localized weather and environmental telemetry including temperature, humidity, barometric pressure, and wind.

## Features

- Integrated mounts for:
  - BME280 / BMP388 (pressure/temp)
  - DHT22 / SHT31 (humidity/temp)
  - Optional anemometer or thermal IR port
- Shielded top cap with vent channels
- Detachable base for battery or LoRa/WiFi uplink

## Print Guidelines

- Material: PETG or ASA
- Orientation: Upright
- Infill: 30–40%
- Wall Count: 3–4
- Supports: Yes (under vent overhangs and cap lip)

## Assembly

- Install sensors to internal tray
- Connect signal lines to telemetry harness
- Optionally mount wireless transmitter to underside
- Attach pod to top rail, boom, or payload bay

Outputs:
- Temperature (°C)
- Relative Humidity (%)
- Barometric Pressure (hPa)
- Optional: Wind speed or surface temp
