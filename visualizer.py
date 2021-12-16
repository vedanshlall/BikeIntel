import numpy as np
import pandas as pd
import matplotlib.pyplot as plt, matplotlib.animation as animation

fig = plt.figure(figsize=(20,3))
plt.title("Rental forecasting | Memory offset = 7 D | Dynamic Adaptability | 2019-01-01 to 2020-05-31")
entries = 240
ax = fig.add_subplot(1,1,1)

f = open('./output/timeline_forecasts.csv','r').read()
t = open('./output/timeline_true_vals.csv','r').read()
linesf = f.split('\n')
linest = t.split('\n')
def animate(i):
    
    #lines = graph_data.split('\n')
    xf = []
    yf = []
    xt = []
    yt = []
    
    for linef, linet in zip(linesf[i+20:i+entries], linest[i:i+entries]):
                
        if len(linef) > 1:
            x, y = linef.split(',')
            xf.append(float(x))
            yf.append(float(y))
            
        if len(linet) > 1:
            x, y = linet.split(',')
            xt.append(float(x))
            yt.append(float(y))
            
    ax.clear()
    ax.plot(xt, yt, label = 'True Rentals')
    ax.plot(xf, yf, '--', label = "Forecast")
    ax.legend()
    plt.ylabel("No. of Rentals")
    plt.xlabel("Timeline-->")
ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()
