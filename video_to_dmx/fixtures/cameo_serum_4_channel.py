
from video_to_dmx.core import Fixture, ColorGrab, Dmx


class CameoSerum4Channel(Fixture):
    """Cameo Serum in 4 channel mode."""

    def __init__(self, start_address: int, position_x: float, position_y: float, deadzone: int = 0):
        """Creates a new Cameo Serum in 4 channel mode at the given position and starting address.Color values below or equal to deadzone get clipped to 0."""
        self.start_address = start_address
        self.position_x = position_x
        self.position_y = position_y
        self.deadzone = deadzone

    def update(self, color_grab: ColorGrab, dmx: Dmx):
        (r, g, b) = color_grab.get_RGB(
            self.position_x, self.position_y, self.deadzone)

        dmx.set_data(self.start_address, 255)
        dmx.set_data(self.start_address + 1, 0)
        dmx.set_data(self.start_address + 2, 0)
        dmx.set_data(self.start_address + 3, 128)

        if r > 127 and g > 127 and b > 127:
            # white
            dmx.set_data(self.start_address + 1, 255)
            dmx.set_data(self.start_address + 2, 64)
        elif r > 127 and g <= 127 and b <= 127:
            # red
            dmx.set_data(self.start_address + 2, 16)
        elif r <= 127 and g > 127 and b <= 127:
            # green
            dmx.set_data(self.start_address + 2, 32)
        elif r <= 127 and g <= 127 and b > 127:
            # blue
            dmx.set_data(self.start_address + 2, 48)
        elif r > 127 and g > 127 and b <= 127:
            # red green
            dmx.set_data(self.start_address + 2, 80)
        elif r > 127 and g <= 127 and b > 127:
            # red blue
            dmx.set_data(self.start_address + 2, 96)
        elif r <= 127 and g > 127 and b > 127:
            # green blue
            dmx.set_data(self.start_address + 2, 128)
