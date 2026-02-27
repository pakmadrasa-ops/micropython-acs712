# MicroPython ACS712 Driver

Minimal MicroPython driver for the ACS712 current sensor on ESP8266.

- DC and AC current reading.
- Simple calibration.
- Designed for memory-limited devices.

## Usage Example

```python
from machine import ADC
from ACS712 import ACS712

adc = ADC(0)
sensor = ACS712(adc, volts=3.3, max_adc=1023, mv_per_ampere=100)
sensor.calibrate_midpoint(50)
print(sensor.read_dc_amps(10))
```

## Sensor Versions
- 5A: 185 mV/A
- 20A: 100 mV/A
- 30A: 66 mV/A

## License
MIT

## Credits
Adapted from Rob Tillaart's Arduino ACS712 library.