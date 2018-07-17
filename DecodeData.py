import matplotlib.pyplot as plt
 
x = range(0,38)
y = range(0,38)
 
line, = plt.plot(x,y,"-")
plt.ion()
plt.show()
plt.draw()
 
 
x = range(0,38)
line.set_xdata(x)
val = "c000389c27708dce3738c427188c6e31380000" # hex val
hex_list = list(val)
y = []
for hl in hex_list:
	y.append(int(hl,16))
line.set_ydata(y)
plt.draw()