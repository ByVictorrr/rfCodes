#!/usr/bin/python

import matplotlib.pyplot as plt
import scipy as sp


val = "80000008c06002487f06c060c7c19f063e1cfe7c18f873e0c780f9cf80c63c6307f0633e007f318319f07f003f9f060c783e701fce7301fc1f3873e738339f398c18f1831fc18cf80e7c073e63e1c3e73e60f9f060fe007f38739f381f38"# hex val


x = range(0,len(val))
y = range(0,len(val))

line, = plt.plot(x,y,"-")
plt.ion()
plt.show()
plt.draw()




x = range(0,len(val))

line.set_xdata(x)

hex_list = list(val)
y = []
for hl in hex_list:
	y.append(int(hl,16))
line.set_ydata(y)
plt.draw()
