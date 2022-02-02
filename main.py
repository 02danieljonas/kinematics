from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

fig, ax = plt.subplots()

def setUp():
    ax.plot([0, 1, 3], [0, 1, 3], color="white")

def update():
    plt.cla()

    setUp()
    ax.plot(xSegment, ySegment)
    plt.show()

setUp()




xSegment = [1.5, 1.5]
ySegment = [0, 2]
ax.plot(xSegment, ySegment)

def withinBounds(xPosition, yPositon):
    if xPosition > 2.99999:
        xPosition = 2.99999
    elif xPosition <.00001:
        xPosition = .00001

    if yPositon > 2.99999:
        yPositon = 2.99999
    elif yPositon < .00001:
        yPositon = .00001

    return xPosition, yPositon



def on_move(data):
    if data.xdata is not None:
        xdata=data.xdata
    if data.ydata is not None:
        ydata=data.ydata

    xSegment[1], ySegment[1] = withinBounds(xdata, ydata)
    update()


binding_id = plt.connect('motion_notify_event', on_move)
plt.show()