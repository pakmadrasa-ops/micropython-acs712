import time
import machine
import math

class ACS712:
    def __init__(self, pin, mode='AC', sensitivity=0.185):
        self.pin = machine.ADC(pin)
        self.mode = mode
        self.sensitivity = sensitivity
        self.offset = self.calibrate_midpoint()

    def read_voltage(self):
        raw_value = self.pin.read()
        voltage = (raw_value / 1024) * 3.3
        return voltage

    def calibrate_midpoint(self):
        samples = 1000
        total = 0
        for _ in range(samples):
            total += self.read_voltage()
            time.sleep(0.01)
        return total / samples

    def read_current(self):
        voltage = self.read_voltage() - self.offset
        current = voltage / self.sensitivity
        return current

    def average_current(self, samples=10):
        total_current = 0
        for _ in range(samples):
            total_current += self.read_current()
            time.sleep(0.1)
        return total_current / samples

    def read_ac_dc(self, duration=1):
        if self.mode == 'AC':
            samples = int(duration * 1000)  # 1000 samples per second
            total = 0
            for _ in range(samples):
                total += self.read_current() ** 2
                time.sleep(0.001)
            rms_current = math.sqrt(total / samples)
            return rms_current
        else:
            return self.read_current()