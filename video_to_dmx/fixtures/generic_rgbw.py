
from video_to_dmx.core import Fixture, ColorGrab, Dmx


class GenericRGBW(Fixture):
    """Generic 4 channel RGBW Fixture"""

    def __init__(self, start_address: int, position_x: float, position_y: float, deadzone: int = 0):
        """Creates a new GenricRGBW Fixture at the given position and starting address.Color values below or equal to deadzone get clipped to 0."""
        self.start_address = start_address
        self.position_x = position_x
        self.position_y = position_y
        self.deadzone = deadzone

    def update(self, color_grab: ColorGrab, dmx: Dmx):
        (r, g, b, w) = color_grab.get_RGBW(
            self.position_x, self.position_y, self.deadzone)

        dmx.set_data(self.start_address, r)
        dmx.set_data(self.start_address + 1, g)
        dmx.set_data(self.start_address + 2, b)
        dmx.set_data(self.start_address + 3, w)
