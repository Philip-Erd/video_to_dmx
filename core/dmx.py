
class Dmx:
    """DMX interface base class."""

    def set_data(self, channel: int, value: int):
        """Sets the value for the specified channel."""
        pass

    def write(self):
        """Write the channel data to the fixtures."""
        pass
