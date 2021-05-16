# -*- coding: utf-8 -*-

import smbus
# import sys
import time


class EPS:
    address = 0x18

    def __init__(self):
        self.device = smbus.SMBus(1)

    def read_byte(self, register):
        return self.device.read_byte_data(self.address, register)

    def write_byte(self, byte):
        self.device.write_byte(self.address, byte)

    # getters
    def get_batteryVoltage(self):
        return self.read_byte(self.ReadComands.batteryVoltage) * 0.0023394775

    def get_softwareVersion(self):
        return self.read_byte(self.ReadComands.softwareVersion)

    # ------------------ Comands -------------------
    class ReadComands:
        batteryVoltage = 0x01
        softwareVersion = 0x42

    class WriteComands:
        testvar = "testvar"


if __name__ == "__main__":
    eps = EPS()
    while True:
        print(eps.get_batteryVoltage())
        time.sleep(0.5)

