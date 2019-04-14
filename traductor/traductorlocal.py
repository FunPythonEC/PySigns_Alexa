from time import sleep
from random import uniform
import paho.mqtt.client as paho
import os
import socket
import ssl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.image as mpimg
import sys
import datetime
import imageio
import pyglet

def create_gif(filenames, duration):
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave("gif.gif", images, duration=duration)

def on_connect(client, userdata, flags, rc):
    global connflag
    connflag = True

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def cb(topic, msg):
	imsimage=[]
    if msg!=b'':
    	msg=str(msg)
    	for i in msg:
    		nombre=i+".PNG"
    		imsimage.append(nombre)

		tiempo=len(imsimage)*1
		create_gif(imsimage,tiempo)

	ag_file = "gif.gif"
	animation = pyglet.resource.animation(ag_file)

	win = pyglet.window.Window(fullscreen=True)
	sprite = pyglet.sprite.Sprite(animation, x=win.width/2-250, y=win.height/2-250)
	sprite.scale=min(3.0, 1000, 1000)
	blue = 0.25, 0.75, 1, 1
	pyglet.gl.glClearColor(*blue)

	label = pyglet.text.Label(msg,
                          	font_name='Times New Roman',
                          	font_size=58,
                          	x=200, y=75,
                          	anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))

	@win.event
	def on_draw():
    	win.clear()
    	sprite.draw()
    	label.draw()

	def close(event):
    	win.close()

	pyglet.clock.schedule_once(close, (tiempo*2+2))
	pyglet.app.run()
    	
     
connflag = False

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

awshost = "endpoint.iot.us-east-1.amazonaws.com"
awsport = 8883
clientId = "Traductor"
thingName = "Traductor"
caPath = "cert/root_ca.pem"
certPath = "cert/cert.pem.crt"
keyPath = "cert/private.pem.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)
mqttc.setcallback(cb)
connection.subscribe(b'Traductor')

while True:
	try:
		mqttc.wait_msg()
    except Exception:
    	pass
