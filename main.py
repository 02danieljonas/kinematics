from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import numpy as np

segmentLength =0.5
fig, ax = plt.subplots()

def updateScreen():
    plt.cla() #this clears the screen, so make sure it is first

    ax.set_xlim(0,3)
    ax.set_ylim(0,3)
    ax.plot(xSegmentList, ySegmentList)
    plt.show()

ax.set_xlim(0,3)
ax.set_ylim(0,3)
xSegmentList = [1.5, 1.5]
ySegmentList = [0, 2]
ax.plot(xSegmentList, ySegmentList)

def on_move(data):
    
    xSegmentList[1], ySegmentList[1] = data.xdata, data.ydata
    xSegmentList[0], ySegmentList[0] = data.xdata-segmentLength, data.ydata-segmentLength

    updateScreen()

binding_id = plt.connect('motion_notify_event', on_move)
plt.show()