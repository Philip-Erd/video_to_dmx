from pyglet.image import ImageData, AbstractImage


class ColorGrab:
    """Object to help grab the pixel color at a specific location of an image."""

    def __init__(self):
        """Initializes a new ColorGrab object with empty image data."""
        self.data: ImageData = None
        self.width = 0
        self.height = 0

    def grab_color(self, image: AbstractImage):
        """Read the image data from the given image and save it internally for faster access."""
        self.width = image.width
        self.height = image.height

        self.data = image.get_data("RGBA", 4 * self.width)

    def get_RGB(self, position_x: float, position_y: float, deadzone: int = 0) -> tuple[int, int, int]:
        """Get the RGB value of the pixel at the defined position. Color values below or equal to deadzone get clipped to 0."""
        if self.data is None:
            return (0, 0, 0)

        # zero point top left
        pixel_x = round(self.width * position_x) % self.width
        pixel_y = (
            round(self.height * position_y) % self.height
        )

        pos = (self.width * pixel_y + pixel_x) * 4
        r = self.data[pos]
        g = self.data[pos + 1]
        b = self.data[pos + 2]

        r = r if r > deadzone else 0
        g = g if g > deadzone else 0
        b = b if b > deadzone else 0

        return (int(r), int(g), int(b))

    def get_RGBW(self, position_x: float, position_y: float, deadzone: int = 0) -> tuple[int, int, int, int]:
        """Get the RGBW value of the pixel at the defined position. Color values below or equal to deadzone get clipped to 0."""

        (r, g, b) = self.get_RGB(position_x=position_x,
                                 position_y=position_y, deadzone=deadzone)

        min_component = min(r, min(g, b))
        w = 0

        if min_component <= 84:
            w = 3 * min_component
            r = r - min_component
            g = g - min_component
            b = b - min_component
        else:
            w = 255
            w3 = w/3

            r = r - w3
            g = g - w3
            b = b - w3

        return (int(r), int(g), int(b), int(w))
