import paho.mqtt.client as paho
import os
import socket
import ssl
from time import sleep
from random import uniform
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.image as mpimg
import sys
import datetime
import imageio
import pyglet

msg="ab"
imsimage=[]
for i in msg:
    nombre=i+".PNG"
    imsimage.append(nombre)
    print(imsimage)


tiempo=len(imsimage)*1
create_gif(imsimage,tiempo)

# pick an animated gif file you have in the working directory
ag_file = "gif.gif"
animation = pyglet.resource.animation(ag_file)

win = pyglet.window.Window(fullscreen=True)
sprite = pyglet.sprite.Sprite(animation, x=win.width/2-250, y=win.height/2-250)
sprite.scale=min(3.0, 1000, 1000)
green = 0.25, 0.75, 1, 1
pyglet.gl.glClearColor(*green)

label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=58,
                          x=200, y=75,
                          anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))
@win.event
pyglet.clock.schedule_once(close, 2.0)
pyglet.app.run()