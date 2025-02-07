import pyglet


from core import FixtureHandler
from dmx_interfaces import SerialDmx
from fixtures import GenericRGBW


dmx = SerialDmx(port="/dev/ttyUSB0", number_of_channels=16)

fixture_handler = FixtureHandler(dmx=dmx)

fixture_handler.addFixture(GenericRGBW(1, 0.5, 0.5))
fixture_handler.addFixture(GenericRGBW(5, 0.0, 0.5))
fixture_handler.addFixture(GenericRGBW(9, 0.5, 0.0))
fixture_handler.addFixture(GenericRGBW(13, 0.0, 0.0))


# options.headless = True

window = pyglet.window.Window(resizable=True)
player = pyglet.media.Player()

source = pyglet.media.load("test_film/1.mp4")
player.queue(source)
player.loop = True
player.play()


fps_display = pyglet.window.FPSDisplay(window=window)


def update_dmx(dt):
    image = player.texture.get_image_data()

    fixture_handler.update(image)


pyglet.clock.schedule_interval(update_dmx, 1.0/30)


@window.event
def on_draw():
    window.clear()

    # center texture
    x = (window.width - player.texture.width) / 2
    y = (window.height - player.texture.height) / 2

    player.texture.blit(x, y)

    fps_display.draw()
    pass


pyglet.app.run()
