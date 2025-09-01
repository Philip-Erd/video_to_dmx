from video_to_dmx.core import ColorGrab, Dmx


class Fixture:
    """Fixture base class"""

    def update(self, color_grab: ColorGrab, dmx: Dmx):
        """Update the channel values in the given DMX interface with the data from the ColorGrab"""
        pass
