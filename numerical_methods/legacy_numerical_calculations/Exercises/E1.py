import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from IPython.display import HTML
from IPython.display import display
from matplotlib.animation import FuncAnimation, PillowWriter

"""
# Plot1 : Lecture2-Plotting-MachinePrecision.pdf, Page 4
# Goal : Show Sin(x) for 11 points in range 0 to 10

# Creat list of x
numpoints = 11
X = np.linspace(0, 10, numpoints)

# Creat list of sin(x)
Y = np.sin(X)

# Creat plot for data
plt.scatter(X, Y, color="blue", alpha=1)

# Label the axis
plt.xlabel("x")
plt.ylabel("sin(x)")

# Make limit for x and y axis for better view
plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5)

# Show the Plot
plt.show()
"""

"""
# Plot2 : Lecture2-Plotting-MachinePrecision.pdf, Page 5
# Goal : Show Sin(x) for 100 points in range 0 to 10

# Creat list of x
numpoints = 100
X = np.linspace(0, 10, numpoints)

# Creat list of sin(x)
Y = np.sin(X)

# Creat plot for data
plt.scatter(X, Y, color="blue", alpha=1, s=1.5)

# Label the axis
plt.xlabel("x")
plt.ylabel("sin(x)")

# Make limit for x and y axis for better view
plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5)

# Show the Plot
plt.show()
"""

"""
# Plot3 : Lecture2-Plotting-MachinePrecision.pdf, Page 6
# Goal : Show Sin(x) for 100 points in range 0 to 10 and line them

# Creat list of x
numpoints = 100
X = np.linspace(0, 10, numpoints)
# Creat list of sin(x)
Y = np.sin(X)

# Creat line plot for data
plt.plot(X, Y, color="red")

# Creat scatter plot for data
plt.scatter(X, Y, color="blue", alpha=1, s=6)

# Label the axis
plt.xlabel("x")
plt.ylabel("sin(x)")

# Make limit for x and y axis for better view
plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5)

# Show the Plot
plt.show()
"""

"""
# Plot4 : Lecture2-Plotting-MachinePrecision.pdf, Page 7
# Goal : Creat line Plot Sin(x) for 100 points in range 0 to 10

# Creat list of x
numpoints = 100
X = np.linspace(0, 10, numpoints)
# Creat list of sin(x)
Y = np.sin(X)

# Creat line plot for data
plt.plot(X, Y, color="red")

# Label the axis
plt.xlabel("x")
plt.ylabel("sin(x)")

# Make limit for x and y axis for better view
plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5)

# Show the Plot
plt.show()
"""

"""
# Plot5 : Lecture2-Plotting-MachinePrecision.pdf, Page 8
# Goal : Creat Plot Sin(x) and cos(x) for 100 points in range 0 to 10

# Creat list of x
numpoints = 100
X = np.linspace(0, 10, numpoints)
# Creat list of sin(x)
sin = np.sin(X)
cos = np.cos(X)

# Creat line plot for data
plt.plot(X, sin, color="red", label="sin(x)", linestyle="-")
plt.plot(X, cos, color="blue", label="cos(x)", linestyle="--")
plt.legend()

# Label the axis
plt.xlabel("x")
plt.ylabel("y")

# Make limit for x and y axis for better view
plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5)

# Show the Plot
plt.show()
"""

"""
# Plot6 : Lecture2-Plotting-MachinePrecision.pdf, Page 12
# Goal : Creat scatter Plot for star brightness-surface temperature pair from file

# Load the star data
# in my PC i shuld redirect the path to find stars.txt with import os
data = np.loadtxt("stars.txt", float)

# mining Temperature from data
x = data[:, 0]  # the 1st column from data

# mining Magnitude from data
y = data[:, 1]  # the 2nd column from data

# Creat the Plot
plt.scatter(x, y, color="blue", alpha=0.25)

# Label the x axis
plt.xlabel("Temperature")

# Label the y axis
plt.xlabel("Magnitude")

# Make limit for x and y axis for better view
plt.xlim(0, 13000)
plt.ylim(-5, 20)

# Show the Plot
plt.show()
"""

"""
# Plot7 : Lecture2-Plotting-MachinePrecision.pdf, Page 13
# Goal : Creat scatter Plot for random items!

# Fixing random seed
np.random.seed(945335)

# Creat random list for x and y for N pionts
N = 50
x = np.random.rand(N)
y = np.random.rand(N)

# Creat random color
colors = np.random.rand(N)

# Creat random size
sizes = (30 * np.random.rand(N)) ** 2

# Creat Plot
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)
plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(0, 1)
plt.ylim(0, 1)

# Show the plot
plt.show()
"""

"""
# Plot8 : Lecture2-Plotting-MachinePrecision.pdf, Page 14
# Goal : Creat a plot to show fields

# Grid of points
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)

# Meshgrid
X, Y = np.meshgrid(x, y)

# Locations of the poles
x1, y1 = -2, 0.
x2, y2 = 2., 0.

# Electric potentail of a dipole
Vdip = 1./np.sqrt((X-x1)**2 + (Y-y1)**2) - 1./np.sqrt((X-x2)**2 + (Y-y2)**2)

# Contour plot (lines only)
plt.title("Electric Potential of a dipole")
plt.xlabel("x")
plt.ylabel("y")
CS = plt.contour(X, Y, Vdip, levels=np.linspace(-0.5, 0.5, 11))
plt.clabel(CS)
plt.show()
"""

"""
# Plot9 : Lecture2-Plotting-MachinePrecision.pdf, Page 15
# Goal : Creat a plot to show fields

# Grid of points
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)

# Meshgrid
X, Y = np.meshgrid(x, y)

# Locations of the poles
x1, y1 = -2, 0.
x2, y2 = 2., 0.

# Electric potentail of a dipole
Vdip = 1./np.sqrt((X-x1)**2 + (Y-y1)**2) - 1./np.sqrt((X-x2)**2 + (Y-y2)**2)

# Contour plot (lines only)
plt.title("Electric Potential of a dipole")
plt.xlabel("x")
plt.ylabel("y")
CS = plt.contour(X, Y, Vdip, levels=np.linspace(-0.5, 0.5, 11))
plt.clabel(CS)

# Density plot (filled)
fig2, ax2 = plt.subplots(constrained_layout=True)
ax2.set_title("Electric potentioal of a dipole")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
CS2 = ax2.contourf(CS, levels=np.linspace(-0.5, 0.5, 11))
fig2.colorbar(CS2)
plt.show()
"""

"""
# Plot10 : Lecture2-Plotting-MachinePrecision.pdf, Page 16
# Goal : Creat a plot to show fields

# Grid of points
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)

# Meshgrid
X, Y = np.meshgrid(x, y)

# Locations of the poles
x1, y1 = -2, 0.
x2, y2 = 2., 0.

# Electric potentail of a dipole
Vdip = 1./np.sqrt((X-x1)**2 + (Y-y1)**2) - 1./np.sqrt((X-x2)**2 + (Y-y2)**2)

# Another example using imshow (good for interpolating colors)
plt.title("Electric potentioal of a dipole")
plt.xlabel("x")
plt.ylabel("y")
CS3 = plt.imshow(Vdip, vmax=1.5, vmin=-1.5,
                 origin="lower", extent=[-5, 5, -5, 5])
plt.colorbar(CS3)
plt.show()
"""

"""
# Plot11 : Lecture2-Plotting-MachinePrecision.pdf, Page 17
# Goal : Creat an animation
fig, ax = plt.subplots()
pos, = ax.plot(0, 0, "o")
ax.set_xlim(0, 1)
ax.set_ylim(-1, 1)

v0 = 3
theta = 60. * np.pi / 180.
g = 9.8


def pos_x(t):
    return (v0 * np.cos(theta) * t)


def pos_y(t):
    return (v0 * np.sin(theta) * t - g*(t**2)/2)


dt = 0.01

l1x = [0]
l1y = [0]
line, = ax.plot(l1x, l1y)

total_frames = 70


def animate(frame):
    tx, ty = pos_x(frame*dt), pos_y(frame*dt)
    pos.set_data([tx], [ty])
    if len(l1x) < total_frames:
        l1x.append(tx)
    if len(l1y) < total_frames:
        l1y.append(ty)
    line.set_data(l1x, l1y)
    return pos, line


anim = animation.FuncAnimation(
    fig=fig, func=animate, frames=total_frames, interval=30)
plt.close()
display(HTML(anim.to_jshtml()))
anim.save("my_animation.gif", writer=PillowWriter(fps=20))

# it dident Work !
"""
