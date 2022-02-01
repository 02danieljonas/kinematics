from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

t = [0, 1]
s = [0,1]
fig, ax = plt.subplots()
ax.plot(t, s)

def reload():
    ax.cla()
    ax.plot(t, s)

def update(xmouse, ymouse):
    global t, s
    if xmouse>1:
        xmouse=.999
    if xmouse<0:
        xmouse=.001
    if ymouse>1:
        ymouse=.999
    if ymouse<0:
        ymouse=.001
    t = [0, 1, xmouse]
    s = [0, 1, ymouse]



def on_move(event):
    global t, s
    # get the x and y pixel coords
    x, y = event.x, event.y
    if event.inaxes:
        ax = event.inaxes  # the axes instance
        update(event.xdata, event.ydata)
        reload()
        print('data coords %f %f' % (event.xdata, event.ydata))

def on_click(event):
    reload()

binding_id = plt.connect('motion_notify_event', on_move)

plt.show()