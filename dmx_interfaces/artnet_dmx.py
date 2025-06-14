import asyncio
import numpy as np
from pyartnet import ArtNetNode


from core import Dmx


class ArtnetDmx(Dmx):
    """Serial port based DMX interface. e.g. USB to RS485 converter based on ft232."""

    def __init__(self, ip="127.0.0.1", port=6454, max_fps = 25, number_of_channels=512):
        """Initializes a new SerialDMX interface on the given port (/dev/tty.. or COM..) with the given number of channels. This also opens the port."""
        self.data = [0] * number_of_channels
        asyncio.run(self.run(ip,port,max_fps, number_of_channels))

    async def run(self, ip:str, port:int, max_fps:int, number_of_channels:int):
        self.node = ArtNetNode(ip=ip, port=port, max_fps=max_fps)
        self.universe = self.node.add_universe(0)
        self.channel = self.universe.add_channel(1, number_of_channels)

    def set_data(self, channel: int, value: int):
        self.data[channel-1] = value

    def write(self):
        self.channel.set_values(self.data)

    def __del__(self):
        pass

