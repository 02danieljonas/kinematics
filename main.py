from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

fig, ax = plt.subplots()
def setUp():
    ax.plot([0, 1, 3], [0, 1, 3], color="white")

def update():
    setUp()
    plt.cla()
    plt.show()

setUp()

xSegment = [1.5, 1.5]
ySegment = [0, 2]
ax.plot(xSegment, ySegment)

def withinBounds(xposition, ypositon):
    if xposition is not None:
        if xposition > 2.99999:
            xposition = 2.99999
        elif xposition <.00001:
            xposition = .00001

    if ypositon is not None:
        if ypositon > 2.99999:
            ypositon = 2.99999
        elif ypositon < .00001:
            ypositon = .00001
    return xposition, ypositon

def on_move(data):
    xdata=data.xdata
    ydata=data.ydata

    xSegment[1], ySegment[1] = withinBounds(xdata, ydata)

    print(xSegment,ySegment)

    plt.cla()

    setUp()
    ax.plot(xSegment, ySegment)

    plt.show()


binding_id = plt.connect('motion_notify_event', on_move)
plt.show()