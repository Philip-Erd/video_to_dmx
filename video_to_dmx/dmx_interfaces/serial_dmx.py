import serial
import time
import numpy as np

from video_to_dmx.core import Dmx


class SerialDmx(Dmx):
    """Serial port based DMX interface. e.g. USB to RS485 converter based on ft232."""

    def __init__(self, port='/dev/ttyUSB0', number_of_channels=512):
        """Initializes a new SerialDMX interface on the given port (/dev/tty.. or COM..) with the given number of channels. This also opens the port."""
        self.number_of_channels = number_of_channels
        self.serial = serial.Serial(
            port, baudrate=250000, bytesize=8, stopbits=2)
        self.data = np.zeros([self.number_of_channels+1], dtype='uint8')
        self.data[0] = 0  # start byte

    def set_data(self, channel: int, value: int):
        self.data[channel] = value

    def write(self):

        # send break 88us
        self.serial.break_condition = True
        time.sleep(88.0/1000000.0)

        # send Mark after Break 8us
        self.serial.break_condition = False
        time.sleep(8/1000000.0)

        # send data, start byte is included in data
        self.serial.write(bytearray(self.data))

    def __del__(self):
        self.serial.close()
