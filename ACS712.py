import time

class ACS712:
    def __init__(self, adc, volts=3.3, max_adc=1023, mv_per_ampere=100):
        self.adc = adc
        self.midpoint = max_adc//2
        self.mv_per_step = 1000.0 * volts / max_adc
        self.mv_per_ampere = mv_per_ampere
        self.max_adc = max_adc

    def calibrate_midpoint(self, samples=50):
        s = 0
        for _ in range(samples):
            s += self.adc.read()
            time.sleep_ms(1)
        self.midpoint = s // samples

    def read_dc_amps(self, samples=1):
        s = 0
        for _ in range(samples):
            s += self.adc.read()
        avg_adc = s / samples
        mv = (avg_adc - self.midpoint) * self.mv_per_step
        return mv / (self.mv_per_ampere * 1000)  # returns Amps

    def read_dc_ma(self, samples=1):
        s = 0
        for _ in range(samples):
            s += self.adc.read()
        avg_adc = s / samples
        mv = (avg_adc - self.midpoint) * self.mv_per_step
        return mv / self.mv_per_ampere  # returns mA