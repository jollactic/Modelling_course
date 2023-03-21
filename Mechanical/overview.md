# MECHANICAL PROPERTIES

Computation of mechanical properties does not require explicit description of electrons. All methods on the electronic-atomistic ladder can therefore be used here.

The only thing we need to know at this stage, regarding electronic and atomistic simulation tools are that they will allow us to i) calculate the total energy of system, and ii) calculate the forces acting on each atom (or nuclii) in the system.  

## Geometry optimization

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

## Equation of State

In condensed matter physics, the equation of state is a mathematical expression that relates the pressure, volume, and temperature of a material. It is an essential tool for understanding the thermodynamic behavior of solids under different conditions. There are several equations of state available for solids, each with its own set of assumptions and limitations. In this answer, we will provide an overview of the Birch-Murnaghan equation of state.

The Birch-Murnaghan equation of state is a widely used equation of state for solids that was first proposed by J. D. Birch in 1947 and later extended by F. D. Murnaghan in 1944. The equation relates the pressure (P) and volume (V) of a solid to its equilibrium volume (V0), bulk modulus (K0), and its derivative with respect to pressure (K'0). The equation is given by:

$$
\\
P = \frac{3K_0}{2} \left[\left(\frac{V_0}{V}\right)^{7/3}-\left(\frac{V_0}{V}\right)^{5/3}\right]\left[1+\frac{3}{4}(K_0^{'}-4)\left[\left(\frac{V_0}{V}\right)^{2/3}-1\right]\right]
\\
$$

where K0 is the bulk modulus at equilibrium volume V0, and K'0 is the first derivative of the bulk modulus with respect to pressure. The equation has two parameters, K0 and K'0, which can be determined experimentally or theoretically.

The Birch-Murnaghan equation of state has some advantages over other equations of state, such as its ability to accurately describe the behavior of solids over a wide range of pressures and volumes. However, it has some limitations, such as its inability to accurately describe the behavior of solids at extreme pressures and temperatures.

In summary, the equation of state is an important tool for understanding the thermodynamic behavior of solids. The Birch-Murnaghan equation of state is a widely used equation of state for solids that relates the pressure and volume of a solid to its equilibrium volume, bulk modulus, and its derivative with respect to pressure. The equation has some advantages over other equations of state, but also has some limitations.

These relations are ideal to explore using computional techniques.

## Surface energies

Surface energy is a fundamental property of materials that plays a crucial role in a wide range of phenomena, including adhesion, catalysis, and crystal growth. It is defined as the excess energy per unit area of a material's surface, relative to the energy of the bulk material. The slab model is a widely used computational method for calculating the surface energy of materials.

The slab model involves constructing a thin slab of the material of interest, with one or more exposed surfaces. The slab is typically modeled as a periodic array of atoms or molecules, with the exposed surfaces parallel to the x-y plane. By computing the total energy of the slab using a computational method such as density functional theory (DFT), one can determine the surface energy of the material.

The key idea behind the slab model is that the surface energy of a material can be computed as the difference in energy between the slab and the bulk material, per unit surface area. The bulk material is typically modeled as an infinite crystal lattice, with periodic boundary conditions in all directions. By computing the total energy of both the bulk and slab models using the same computational method, one can determine the difference in energy between the two models, which corresponds to the surface energy of the material.

There are several factors that can affect the accuracy of surface energy calculations using the slab model, including the size and shape of the slab, the choice of computational method, and the treatment of long-range interactions. To minimize these errors, it is important to use large enough slabs to minimize finite-size effects, and to use high-quality computational methods that are capable of accurately describing the electronic and geometric properties of the material.

In summary, the slab model is a powerful computational method for calculating the surface energy of materials. By constructing a thin slab of the material of interest and computing its total energy using a computational method such as DFT, one can determine the surface energy of the material as the difference in energy between the slab and the bulk material, per unit surface area. Careful attention to the choice of computational method and the treatment of finite-size effects is critical to obtaining accurate results.

The surface energy of a material can be calculated using the following equation in the slab model:

$$
\\
\gamma_{\rm{surf}} = \frac{1}{2A} [E_{\rm{slab}} - N_{\rm{atoms}}E_{\rm{bulk}}]
\\
$$

where $\gamma_{\rm{surf}}$ is the surface energy per unit area, $A$ is the surface area of the slab, $E_{\rm{slab}}$ is the total energy of the slab with exposed surfaces, $N_{\rm{atoms}}$ is the number of atoms in the slab, and $E_{\rm{bulk}}$ is the total energy per atom of the bulk crystal. The factor of 1/2 is included to account for the fact that each atom at the surface contributes to the surface energy, but is shared between two surface areas.

### Particle shapes using Wulff construction

From computed surface energies we can predict particle shapes using the Wulff construction. Forming a surface cost energy solids therefore strive to minimize surface area. However, since different surface terminations may have very different surface energies this area minimization has some constraints. Area should be minimized while at the same time exposing as little as possible of high energy surface terminations. For a given volume of material there is a unique shape such that this condition is met. This is called the Wulff shape and can be obtained from a rather simple algorithm.

1. Calcuate the surface energy of relevant surfaces. 
[We are getting into a bit of truble all-ready! The set should at-least include all low-index surfaces, and this often gives a very good idea of the shape. High index surfaces with conpeting surface energy can also be included. This is obviously not trivial do since we need to calculate many different termination. However, since a higher index often means higher surface energy one can systematically include more surfaces with higher and higher index until the surface energy reach a certain threshold.]

2. Define an origi for you particle.

3. For each surface termination, place a plane perpendicular to its normal (pointing away from origo) at an distance that is proportional to it's surface normal.

4. Extract the particle shape from the space encapsulated by the planes placed in step 3.

### Tutorial

<a target="_blank" href="https://colab.research.google.com/github/jollactic/Modelling_course/blob/main/Mechanical/Tutorial.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


<div class="warning" style='padding:0.1em; background-color:#E9D8FD; color:#69337A'>
<span>
<p style='margin-top:1em; text-align:center'>
<b>Assignment:</b></p>
<p style='margin-left:1em;'>

1. Complete the code for geometry optimization in the jupyter note-book. 
2. Choose of of the metals compatible with <a href="https://wiki.fysik.dtu.dk/ase/ase/calculators/emt.html#ase.calculators.emt.EMT">EMT</a> method and find the equlibrium cell volume and bulk modulus.
3. Use the optimized cell volume to figure out the optimum lattice constant of your metal. Use this lattice constant to calculate the surface energy for at-least one surface termination. Explore how the surface energy vary with the number of layers, at what point does the energy seem to change insignificantly when adding more layers to the slab?
4. (Optional) Use the <a href="https://wiki.fysik.dtu.dk/ase/ase/cluster/cluster.html#wulff-construction">Wulff construction</a> routine with your own calculated surface eneries as input to generate the expected equilibrium shape of a particle made from your choosen metal. 

<p style='margin-top:1em; text-align:center'>
<b>Submission instructions:</b></p>
<p style='margin-left:1em;'>

<p style='margin-left:1em;'>
Upload your commented version of the note-book to the studium page. 


</p></span>
</div>

### Further readin
1. [Gradient descent at Wikipedia](Further reading: https://en.wikipedia.org/wiki/Gradient_descent)

2. [Chapter 5 *Atomistic Computer Simulations : A Practical Guide* by Veronika Brázdová and David R. Bowler](https://ebookcentral.proquest.com/lib/uu/reader.action?docID=1161544)