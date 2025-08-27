
from core import Fixture, ColorGrab, Dmx


class GenericRGBDim(Fixture):
    """Generic 4 channel RGB and dimmer Fixture. The dimmer channel is always set to 255."""

    def __init__(self, start_address: int, position_x: float, position_y: float, deadzone: int = 0):
        """Creates a new GenricRGBDim Fixture at the given position and starting address.Color values below or equal to deadzone get clipped to 0."""
        self.start_address = start_address
        self.position_x = position_x
        self.position_y = position_y
        self.deadzone = deadzone

    def update(self, color_grab: ColorGrab, dmx: Dmx):
        (r, g, b) = color_grab.get_RGB(
            self.position_x, self.position_y, self.deadzone)

        dmx.set_data(self.start_address, r)
        dmx.set_data(self.start_address + 1, g)
        dmx.set_data(self.start_address + 2, b)
        dmx.set_data(self.start_address + 3, 255)
