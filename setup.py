from setuptools import setup, find_packages

setup(
    name='video_to_dmx',
    version='0.2.0',
    url='https://github.com/Philip-Erd/video_to_dmx',
    author='Philip Erdelhoff',
    author_email='philip.erdelhoff@gmail.com',
    description='Read dmx data from video files-',
    packages=find_packages(),
    install_requires=['pyglet >= 2.0.15',],
)
