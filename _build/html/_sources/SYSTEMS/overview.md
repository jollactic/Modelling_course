# Atomistic represenation

## Periodic Boundary Conditions (PBC)

Periodic boundary conditions (PBCs) are a mathematical tool used to simulate an infinite system by using a finite simulation cell. This technique is widely used in many areas of physics and chemistry, including molecular dynamics simulations and condensed matter physics.

In PBCs, the edges of the simulation cell are identified with each other, meaning that when a particle exits the simulation cell on one edge, it reenters the cell from the opposite edge as shown in figure below:

![PBC](PBC.gif)


 Mathematically, this can be represented by the following equations:

$$
\\
x_i + L_x &= x_i \\
y_i + L_y &= y_i \\
z_i + L_z &= z_i
\\
$$

where $x_i$, $y_i$, and $z_i$ are the coordinates of particle $i$ in the simulation cell, and $L_x$, $L_y$, and $L_z$ are the lengths of the simulation cell in each direction. These equations state that a particle's position plus the length of the simulation cell in a given direction is equivalent to its position in that direction.

PBCs are particularly useful when studying systems that exhibit periodicity, such as crystals or periodic arrays of particles. By using PBCs, researchers can simulate a small part of the system and extrapolate its behavior to the entire system. However, PBCs do have limitations, such as the inability to accurately model surface effects and other non-periodic phenomena.

The code to generate the animation is provide below:

```
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Set up simulation parameters
L = 2.0   # Length of simulation box
N = 30    # Number of particles
T = 400    # Number of time steps
dt = 0.01   # Time step size

# Initialize particle positions and velocities
pos = L*np.random.rand(N,2)
vel = L*2.0*(np.random.rand(N,2)-0.5)

# Define function to apply periodic boundary conditions
def apply_pbc(pos,L):
    """Apply periodic boundary conditions to positions"""
    pos[pos > L] -= L
    pos[pos < 0] += L

# Define function to update plot
def update_plot(frame):
    global pos
    # Apply periodic boundary conditions
    apply_pbc(pos,L)

    # Update particle positions
    pos += vel*dt

    # Clear plot and plot particle positions
    ax.clear()
    ax.scatter(pos[:,0],pos[:,1])
    ax.scatter(pos[0,0],pos[0,1],color='red')
    ax.set_xlim(0,L)
    ax.set_ylim(0,L)
    ax.set_title('Time Step: {}'.format(frame))
    ax.set_aspect('equal')
    
# Create plot
fig, ax = plt.subplots()

# Create animation
animation = FuncAnimation(fig, update_plot, frames=T, interval=50)

# Display animation
HTML(animation.to_jshtml())
```

```{html}
HTML(animation.to_jshtml())
```

Further reading: [PBC at python in plain english](https://python.plainenglish.io/molecular-dynamics-periodic-boundary-conditions-21f957bbb294)

## Lattice models
In three dimensions, a lattice can be defined as a regular arrangement of points in three-dimensional space, where each point has identical surroundings and the arrangement repeats itself periodically in all directions. More formally, a lattice in three dimensions can be defined as a set of points of the form $\vec{r} = n_1\vec{a}_1 + n_2\vec{a}_2 + n_3\vec{a}_3$, where $\vec{a}_1$, $\vec{a}_2$, and $\vec{a}_3$ are three linearly independent vectors called the lattice vectors, and $n_1$, $n_2$, and $n_3$ are integers.

The lattice vectors $\vec{a}_1$, $\vec{a}_2$, and $\vec{a}_3$ are chosen such that they form a parallelepiped that contains all the lattice points. This parallelepiped is called the unit cell of the lattice, and it represents the repeating pattern of the lattice.


![PBC](lattice.png)

The figure illustrates a 2d lattice with the unit cell marker out.

There are many types of lattices in three dimensions, each with different symmetry properties. Some common examples include the simple cubic lattice, the face-centered cubic lattice, and the body-centered cubic lattice. The simple cubic lattice is the most basic type of lattice, where each lattice point is at the corner of a cube. The face-centered cubic lattice has additional lattice points at the center of each face of the cube, while the body-centered cubic lattice has an additional lattice point at the center of the cube.

We can sometimes use a lattice in simulations. We will see an example of that when we consider the cluster expansion method.