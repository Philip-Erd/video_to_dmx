# video_to_dmx
Play a video back and write pixel data to DMX output.

## Motivation

Controlling DMX lights with videos instead of using specific programs and their effects, has a couple of benefits. First of all it makes it really easy to share light shows with others and adapt them to your setup. It also makes it really easy to sync the lights to music, because the audio is already embedded in the video file. Light shows can be created with all kinds of video editing software and apps. You may even use real video footage and map your lights to it.
Mapping the lights to a video only really works for simple colored lights. For more complex fixtures like moving heads it does nor work that well, because you can't map the pixel color to an axis postion directly. You may use an additional video containing directional data (similar to normal map) and map it the axis of moving heads to achieve control, but this is not part of this project. So this approach is best suited for matrix effects.

I intend to use this to light rooms, so I imagine the video to be a top down view of the room. The center of action, where, for example, the DJ or band is, is at the bottom center. Then I create my effects and shows according to this layout. Then I map my fixtures to the x and y position. This does not give you the ability to make effects in the hight direction (floor to ceiling), but this isn't necessary for me, because I usually have the fixtures mounted at the ceiling pointing down.

![example layout](doc/img/mapping.svg)

You can, of course, come up with your own layouts, e.g. locking at the stage from the front or mapping it to the surface of a 3 dimensional object, like a building or sphere.

## About this project

This project demonstrates how to playback a video and map specific pixelpositions to DMX lights. For video playback it uses pyglet. It provides a Srial DMX interface to use with generic USB to RS485 adapters. It also comes with fixture profiles for a generic RGB and a generic RGBW fixture.

### dependencies

This project only depends on `pyglet`, `serial`, `numpy` and  `time`.

### running the project

simply run `main.py` with python


#### specify your serial port and number of channels

Change `/dev/ttyUSB0` to your port. For Windows, change it to a `COM` port.
The number of channels can also be specified, when creating the interface.

`dmx = SerialDmx(port="/dev/ttyUSB0", number_of_channels=16)`

#### FixtureHandler

The `FixtureHandler` helps to group multiple fixtures together and update them all at once.

### Position the fixtures

The position you can set on the fixtures is **not** the physical position. It is the position on the provided video/image/texture that the fixture will read the color from. The position in each axis is given as a float in the range from 0 to approaching 1. The position will wrap around, so e.g. 0, 1 and 2 will be the same position. The position is relative to the size of the video. The left side is always 0 and near 1 is to the right. The bottom side is 0 and near 1 is the top. This is true regardless of the aspect ratio of the video.

### video compression

Due to video compression the colors may be a bit of, from what you originally intended. This is especially for the edges of the video. I recommend not placing fixtures directly on the edge of the video, but rather use a few pixels of margin around the edges. Also black video isn't always black. Some lights may act a bit weird, when they get small values and glow dimly. To prevent glowing you can add a deadzone for each fixture. Every color value below or equal the deadzone will be clipped to 0.


