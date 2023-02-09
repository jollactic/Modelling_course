Computation of mechanical properties does not require explicit description of electrons. All methods on the electronic-atomistic ladder can therefore be used here.

# Geometry optimization

A central concept in chemistry and physics is the so-called potential energy surface (PES). The PES is the continuous surface that specifies the energy of system as a function of the atom coordinates. THe surface typically contains a number of local minima, a single global minima, saddle points and maxima. With geometry optimization we can identify local minima. Thus, given a starting goemetry defining the positions of all atoms in our system and a computational protocol, we search for closest local minima on the potential energy surface. There are numerous techniques availble to us. Conseptually, the simplest is the steepest descent (ro gradient descent) algorithm which will be our leading example.

The gradient descent algorithm describes an intertive to find local minima in a highdimesional space. Lets say we are at position $\textbf{r}_{i}^{N}$ in our high-dimesional space where $\textbf{r}_{i}^{N}$ describes the position (x,y,z coordinates) of ALL nucleous of our system. If we take a sufficiently small step $\alpha$ along the gradient $\triangledown E(\textbf{r}_{i}^{N})$ we should en up a point lower in energy. We can write the following recursive formula where we find the minima as $i\rightarrow \infty$:

$$
\\
\textbf{r}_{i+1}^{N}=\textbf{r}_{i}^{N} -\alpha \triangledown E(\textbf{r}_{i}^{N})
\\
$$

Note that since the negative of the gradient to the energy is the force, $F(\textbf{r}_{i}^{N})$, we can write:

$$
\\
\textbf{r}_{i+1}^{N}=\textbf{r}_{i}^{N} +\alpha F(\textbf{r}_{i}^{N})
\\
$$

Note that $F(\textbf{r}_{i}^{N})$ collects the force along x,y,z for ALL nucleus. Thus if we know how to compute forces we can implement a steepest descent algorithm. Forces is a standard output for most computational methods such as HF and DFT. 

Further reading: https://en.wikipedia.org/wiki/Gradient_descent

Jupyter notebook.

# Equation of State

The equation of state in the context of solids relates volume, energy and pressure. These relations are ideal to explore using computional techniques.

Jupyter notebook.

# Surface energies

Surface energy is another property that lends it self very well for simulations. We can compute surface energies using the so-called slab model

Jupyter notebook.

### Particle shapes using Wulff construction

From computed surface energies we can predict particle shapes using the Wulff construction. Forming a surface cost energy solids therefore strive to minimize surface area. However, since different surface terminations may have very different surface energies this area minimization has some constraints. Area should be minimized while at the same time exposing as little as possible of high energy surface terminations. For a given volume of material there is a unique shape such that this condition is met. This is called the Wulff shape and can be obtained from a rather simple algorithm.

1. Calcuate the surface energy of relevant surfaces. 
[We are getting into a bit of truble all-ready! The set should at-least include all low-index surfaces, and this often gives a very good idea of the shape. High index surfaces with conpeting surface energy can also be included. This is obviously not trivial do since we need to calculate many different termination. However, since a higher index often means higher surface energy one can systematically include more surfaces with higher and higher index until the surface energy reach a certain threshold.]

2. Define an origi for you particle.

3. For each surface termination, place a plane perpendicular to its normal (pointing away from origo) at an distance that is proportional to it's surface normal.

4. Extract the particle shape from the space encapsulated by the planes placed in step 3.

Jupyter notebook.
