
##############################
#                            #
# Created by: Daniel Aguirre #
# Date: 2019/05/04           #
#                            #
##############################

# Imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# USER�s VARIABLES
resolution = 750

tini = 0.021501
tend = 0.029601
dt = 0.000005

# Equation definitions
def equations(x, y, t):
    x1 = -(t * t) - (x * y) + t
    y1 = -(x * y) + (x * t) + y + t
    return x1,y1

# Program variables
global x_n, y_n, t_n
x_n, y_n, t_n = [], [], []

fig, ax = plt.subplots()
sc = plt.scatter([],[],color="white",s=0.5)
legend = ax.legend(("Time: " + str(tini),))

# Initialize animation
def initPlot():
    ax.set_facecolor('black')
    ax.set_xlim(-0.4, 0.7)
    ax.set_ylim(-0.4, 0.7)
    return sc,

# Update animation plot
def updatePlot(frame):
    print("Iterations: " + str(frame))

    time = tini + dt*frame
    legendTxt = ("Time: " + str(time)[0:6],)
    plt.legend(legendTxt)
    xdata,ydata = iterateOverXY(time)
    sc.set_offsets(np.c_[xdata, ydata])
    return sc,

# Call to animation plot
def plotty():    
    anim = FuncAnimation(fig, updatePlot, frames=range(int((tend-tini)/dt+1)), init_func=initPlot, blit=False, repeat=False)
    plt.show()

# Recalculate the equation�s values
def iterateOverXY(t):
    x = [t,]
    y = [t,]
    for i in range(resolution):
        x1,y1 = equations(x[-1],y[-1],t)
        x.append(x1)
        y.append(y1)
    return x,y

# Calculate next iteration
def iterateOverTime(tini,tend,dt):
    t = tini    
    while t<tend:   
        print(t)        
        x,y = iterateOverXY(t)
        global x_n, y_n, t_n
        t_n.append(t)
        x_n.append(x)
        y_n.append(y)
        t = t +dt
    return t_n,x_n,y_n

# Save the generated data
def saveData():
    np.save("DataX", x_n)
    np.save("DataY", y_n)
    np.save("DataT", t_n)
    print("Data saved")

# Plots and saves the generated data
def main():
    print("Started")
    plotty()
    saveData()
    print("Finished")

# EXECUTE program
main()


