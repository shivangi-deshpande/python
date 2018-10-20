import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from pylab import *
import numpy as np

fig = plt.figure()
cpu_total = psutil.cpu_count()
subplots_adjust(hspace=0.000)
number_of_subplots=cpu_total
x_total = 60

x = [i for i in range(x_total)]
ylist =[[0]*x_total for i in range(number_of_subplots)]

linelist=[]
for i,v in enumerate(range(number_of_subplots)):
    ax1 = subplot(number_of_subplots,1,v+1) # v+1 plots start with 1
    ax1.set_ylim([0, 100])
    ax1.grid()
    line, = ax1.plot(x, ylist[v])
    linelist.append(line)
plt.grid(True)

def cpumonitor(i):
    interval = None
    cpu_perc= psutil.cpu_percent(interval, percpu=True)
    if len(x)>=x_total:
        for yitem in ylist:
            yitem.pop(0)
    else:
        x.append(i)
    for item in range(number_of_subplots):
        ylist[item].append(cpu_perc[item])
    for i,v in enumerate(range(number_of_subplots)):
        linelist[v].set_ydata(ylist[v])
    fig.canvas.draw()
    fig.canvas.flush_events()

ani = animation.FuncAnimation(fig, cpumonitor)
plt.show()