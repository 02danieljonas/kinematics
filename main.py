from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import numpy as np
import matplotlib


segmentLength =0.5
fig, ax = plt.subplots()

def setUp():
    ax.plot([0, 1, 3], [0, 1, 3], color="white")

def updateScreen():
    plt.cla()

    setUp()
    ax.plot(xSegmentList, ySegmentList)
    plt.show()

setUp()




xSegmentList = [1.5, 1.5]
xdata=1.5
ySegmentList = [0, 2]
ydata=2
ax.plot(xSegmentList, ySegmentList)

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

def withinSegmentBounds(xPosition, yPosition):
    pass


def on_move(data):
    global xdata, ydata
    if data.xdata is not None:
        xdata=data.xdata
    if data.ydata is not None:
        ydata=data.ydata

    xSegmentList[1], ySegmentList[1] = withinBounds(xdata, ydata)
    xSegmentList[0], ySegmentList[0] = withinBounds(xdata-segmentLength, ydata-segmentLength)

    updateScreen()


binding_id = plt.connect('motion_notify_event', on_move)
plt.show()