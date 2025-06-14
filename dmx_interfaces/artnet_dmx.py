from stupidArtnet import StupidArtnet


from core import Dmx


class ArtnetDmx(Dmx):
    """Artnet based DMX interface."""

    def __init__(self, ip="127.0.0.1", port=6454, number_of_channels=512):
        """Initializes a new ArtnetDmx interface on the given ip and port with the given number of channels."""
        self.data = bytearray(number_of_channels)	
        self.artnet = StupidArtnet(ip, 0, number_of_channels, port=port)


    def set_data(self, channel: int, value: int):
        self.data[channel-1] = value


    def write(self):
        self.artnet.set(self.data)
        self.artnet.show()

    def __del__(self):
        pass

