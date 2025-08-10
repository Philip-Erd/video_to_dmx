from core import Fixture, Dmx, ColorGrab
from pyglet.image import AbstractImage


class FixtureHandler:
    """Helper Class to update multiple fixtures and write the DMX data."""

    def __init__(self, dmx: Dmx):
        """Creates a new FixtureHandler, which writes the DMX data to the given interface."""
        self.fixtures = []
        self.dmx = dmx
        self.color_grab = ColorGrab()

    def addFixture(self, fixture: Fixture):
        """Add a new Fixture to the FixtureHandler."""
        self.fixtures.append(fixture)

    def update(self, image: AbstractImage):
        """Update all fixtures with the given image data. This also write out the data trough the DMX interface."""
        self.color_grab.grab_color(image)

        fixture: Fixture
        for fixture in self.fixtures:
            fixture.update(self.color_grab, self.dmx)
        self.dmx.write()
