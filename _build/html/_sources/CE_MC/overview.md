# Dealing with dissordered structures - Cluster expansion and Monte-Carlo sampling

## Cluster expansion (CE)
The cluster expansion method is a computational technique used to model the energetics of alloys. It is based on the idea that the total energy of an alloy can be written as a sum of the energies of individual clusters, or groups of atoms, within the alloy.
In this method we use lattice representaion of our system. The cluster expansion method is typically used to calculate the configurational entropy and to predict the stable structures of alloys.

In mathematical terms, the cluster expansion method can be represented as:

$$
\\
E = \sum_{i} c_{i}\Delta E_{i}
\\
$$

where $E$ is the total energy of the alloy, $\Delta E_{i}$ is the energy of the $i$th cluster, and $c_{i}$ is the concentration of the $i$th cluster within the alloy.

The cluster expansion method relies on two key assumptions. The first assumption is that the energetics of an alloy can be accurately described by considering only short-range interactions between atoms. The second assumption is that the energy of a cluster can be calculated as a sum of the energies of its constituent atoms, plus a term that accounts for the interactions between the atoms within the cluster.

The cluster expansion method is a powerful tool for predicting the properties of alloys, particularly in cases where experimental data is limited. However, it requires accurate knowledge of the energetics of individual clusters, which can be difficult to obtain. Additionally, the cluster expansion method is limited to systems in which the interactions between atoms can be accurately described by short-range potentials.


```
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Define lattice dimensions
nx, ny = 5, 5

# Define clusters and their coefficients
clusters = [    [[[0, 0], [1, 0]], 0.1],
    [[[0, 0], [0, 1]], 0.2],
    [[[0, 0], [1, 0], [0, 1]], -0.1],
]

# Define function to calculate the energy of a single cluster
def cluster_energy(cluster, coefficient, occupancy):
    energy = 0
    for c in cluster:
        cluster_energy = coefficient 
        for site in c:
            x, y = site
            if (x >= nx) or (y >= ny):
                cluster_energy = 0
                break
            if occupancy[x, y] == 0:
                cluster_energy = 0
                break
        energy += cluster_energy
    return energy

# Randomly set occupancy variables for each lattice site
occupancy = np.random.randint(0, 2, size=(nx, ny))

# Calculate the total energy and cluster energies
total_energy = 0
cluster_energies = []
for cluster, coefficient in clusters:
    energy = 0
    for i in range(nx):
        for j in range(ny):
            # Translate cluster to current position and calculate energy
            translated_cluster = [[np.array(site) + np.array([i, j]) for site in cluster]]
            energy += cluster_energy(translated_cluster, coefficient, occupancy)
    cluster_energies.append(energy)
    total_energy += energy

# Plot the lattice without clusters marked out
fig, ax = plt.subplots()
ax.set_aspect("equal")
ax.set_xticks([])
ax.set_yticks([])
for i in range(nx):
    for j in range(ny):
        xy = np.array([[i, j], [i + 1, j], [i + 1, j + 1], [i, j + 1]])
        color = "k" if occupancy[i, j] else "none"
        poly = Polygon(xy, facecolor=color, edgecolor="k")
        ax.add_patch(poly)
ax.set_xlim(0, nx)
ax.set_ylim(0, ny)
ax.set_title("A 2d alloy")
plt.show()

# Plot each cluster individually
for i, (cluster, coefficient) in enumerate(clusters):
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    for site in cluster:
        x, y = site[0]+nx/2.-1, site[1]+ny/2.-1
        xy = np.array([[x, y], [x + 1, y], [x + 1, y + 1], [x, y + 1]])
        color = "r"
        poly = Polygon(xy, facecolor=color, edgecolor="r")
        ax.add_patch(poly)
    ax.set_xlim(0, nx)
    ax.set_ylim(0, ny)
    ax.set_title("Cluster {} (coefficient {})".format(i+1, coefficient))
    plt.show()
print("The energy of the system is defined by the number of \n cluster of each type that you can fit over black pathes of the alloy.")

E_guess = input("What is the expected energy of the system?")


# Print total energy and cluster energies
print("True total energy: ", total_energy," Your guess?",E_guess)
for i, energy in enumerate(cluster_energies):
    print("Contribtion from cluster {} is {}".format(i+1, energy))
```


## Convex hull and phase-diagrams
Cluster expansions and convex hull can be used together to construct a simple phase diagram for a given alloy system. The basic idea is to use the cluster expansion to calculate the energies of different configurations of the alloy, and then use the convex hull construction to identify the lowest-energy configurations, or phases, at a given composition.

The convex hull construction is a geometric method that can be used to identify the most stable phases at a given composition, based on the calculated energies of different configurations. The method involves plotting the energies of all possible configurations of the alloy as a function of their compositions, and then drawing a convex hull around the lowest-energy configurations. The points on the convex hull correspond to the most stable phases at the given composition, and the lines connecting these points represent phase boundaries.

To construct a simple phase diagram using these methods, one can follow these steps:

1. Calculate the energies of different configurations of the alloy using the cluster expansion method.

2. Use the convex hull construction to identify the lowest-energy configurations, or phases, at a given composition.

3. Plot the energies of all possible configurations of the alloy as a function of their compositions.

4. Draw a convex hull around the lowest-energy configurations, and identify the points on the hull as the most stable phases at the given composition.

Connect the points on the convex hull with lines to represent the phase boundaries.

The resulting phase diagram shows the stable phases of the alloy at different compositions, and the transitions between them. This can be useful in predicting the behavior of the alloy under different conditions, such as changes in temperature or pressure. However, if we only consider total energies of static structures we are neglecting to role of configurational dissorder in the system. For a given composition we may have many configruations with similar energies. The system is therefor typically better represented by a weighted average over all these configuration, a so-called ensambe average. Monte-Carlo simulations can be used to rigoursly compute ensemble averages.

[ASE tutorial](https://wiki.fysik.dtu.dk/ase/tutorials/ga/ga_convex_hull.html)

## Metropolis Monte-Carlo (MC)

The Metropolis Monte Carlo simulation technique is a powerful computational method used to simulate the behavior of atoms or molecules in a system. It is commonly used in condensed matter physics, chemistry, and materials science.

The Metropolis Monte Carlo simulation technique works by randomly proposing new configurations of the system, and accepting or rejecting them based on their energy difference relative to the current configuration. The probability of accepting a new configuration is determined by the Metropolis criterion, which ensures that the simulation samples the correct thermodynamic ensemble.

The Metropolis criterion states that the probability of accepting a new configuration with energy difference $\Delta E$ is given by:

$$
\\
P(\Delta E) = min { e^{-\Delta E/k_BT}, 1 }
\\
$$

where $k_B$ is the Boltzmann constant, $T$ is the temperature, and $\Delta E$ is the energy difference between the proposed configuration and the current configuration. This means that, if the propsoed configuration has a lower energy it is always  
accepted. 

In practice, the Metropolis Monte Carlo simulation technique involves the following steps:

1. Choose a starting configuration for the system.

2. Randomly propose a new configuration by moving one or more atoms or molecules in the system.

3. Calculate the energy difference between the proposed configuration and the current configuration.

4. Determine whether to accept or reject the proposed configuration based on the Metropolis criterion.

5. Repeat steps 2-4 for a large number of iterations, allowing the simulation to explore the configuration space of the system.

Analyze the results of the simulation to calculate thermodynamic properties of the system, such as the heat capacity and free energy.

The Metropolis Monte Carlo simulation technique can be used to simulate a wide range of systems, including simple gases, liquids, and solids, as well as more complex systems such as polymers, and proteins. 

## Combining CE and MC
The combination of cluster expansion and Monte Carlo simulations can be used to study a wide range of properties of alloys, such as phase stability, order-disorder transitions, and defects such as vacancies or interstitials. It also a very powerful technique to simulate Li intercalation on cathode and anonde materials in the context of batteries (see e.g. [Ref.](https://iopscience.iop.org/article/10.1088/1361-648X/ab1bbc))

 The method can also be used to construct a phase diagram that shows the stable phases of the alloy as a function of temperature and composition.


<div class="warning" style='padding:0.1em; background-color:#E9D8FD; color:#69337A'>
<span>
<p style='margin-top:1em; text-align:center'>
<b>Assignment:</b></p>
<p style='margin-left:1em;'>



</p></span>
</div>