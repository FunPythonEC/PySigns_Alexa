from time import sleep
import imageio
import pyglet

def create_gif(filenames, duration):
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave("gif.gif", images, duration=duration)

msg="hola profesores"
msgtxt=msg.replace(" ", "_")
msgtxt
imsimage=[]
for i in msgtxt:
    nombre=i+".PNG"
    imsimage.append(nombre)

tiempo=len(imsimage)*0.1
create_gif(imsimage,tiempo)

# pick an animated gif file you have in the working directory
ag_file = "gif.gif"
animation = pyglet.resource.animation(ag_file)

win = pyglet.window.Window(fullscreen=True)
sprite = pyglet.sprite.Sprite(animation, x=win.width/2-250, y=win.height/2-250)
sprite.scale=min(3.0, 1000, 1000)
green = 0.25, 0.75, 1, 1
pyglet.gl.glClearColor(*green)

label = pyglet.text.Label(msg,
                          font_name='Times New Roman',
                          font_size=58,
                          x=750, y=75,
                          anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))

@win.event
def on_draw():
    win.clear()
    sprite.draw()
    label.draw()

def close(event):
    win.close()

pyglet.clock.schedule_once(close, 18)
pyglet.app.run()
