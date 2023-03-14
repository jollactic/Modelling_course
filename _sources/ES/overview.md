# ELECTRONIC STRUCTURE - Calculating electronic properties

Electronic simulations techniques allow us to compute electronic properties such as electronic band-gaps. In order to determine such properties we need to allow our simulations techniques

A brief overview is given in the following section. A more comprehensive summary can be found in the [excellent article by Hoffmann](https://onlinelibrary.wiley.com/doi/epdf/10.1002/anie.198708461).


## Bloch theorem
The Bloch theorem is a fundamental concept in the study of electronic properties of crystalline materials, which states that the wave function of an electron in a periodic potential can be written as a product of a plane wave and a periodic function. Mathematically, the Bloch theorem can be stated as:

$$\psi_{\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} u_{\mathbf{k}}(\mathbf{r})$$

where $\psi_{\mathbf{k}}(\mathbf{r})$ is the wave function of an electron with wave vector $\mathbf{k}$ in a crystal, $u_{\mathbf{k}}(\mathbf{r})$ is a periodic function with the same periodicity as the crystal lattice, and $e^{i\mathbf{k}\cdot\mathbf{r}}$ is a plane wave.

The Bloch theorem is a powerful tool for understanding the electronic properties of crystalline materials, as it allows for the systematic study of the behavior of electrons in periodic potentials. It forms the basis of many theoretical models used in condensed matter physics and materials science, including Density Functional Theory (DFT), which is widely used to study the electronic properties of materials.

## The hydrogen chain

One way to understand electronic bandstructure is through the example of the hydrogen chain.

The hydrogen chain consists of a linear chain of hydrogen atoms, where each atom is separated by a fixed distance. When the hydrogen atoms are far apart, each hydrogen atom has its own set of discrete energy levels, which are similar to the energy levels of a single hydrogen atom. However, as the atoms get closer together, their electron wavefunctions start to overlap, which creates new energy levels that are a combination of the individual energy levels of each atom. These new energy levels are called energy bands, and they can be described by a continuous range of allowed energies for electrons in the crystal.

The energy levels of a single hydrogen atom can be described by the Schrödinger equation:

$$\hat{H}\psi_n = E_n\psi_n$$

where $\hat{H}$ is the Hamiltonian operator, $\psi_n$ is the wavefunction of the nth energy level, and $E_n$ is the corresponding energy.

When multiple hydrogen atoms are brought together to form a crystal, their electron wavefunctions start to overlap, which leads to the formation of energy bands. The electronic bandstructure of the hydrogen chain can be described using the following equation:

$$\epsilon(k) = \epsilon_0 - 2t\cos(ka)$$

where $\epsilon(k)$ is the energy of an electron with momentum $k$, $\epsilon_0$ is the energy of the isolated hydrogen atom, $t$ is the hopping integral between adjacent atoms, $a$ is the distance between adjacent atoms, and $k$ is the wavevector of the electron.

### The first Brillouin zone for the hydrogen chain.

The first Brillouin zone is a concept in solid-state physics that represents the boundaries of the smallest possible repeating unit in the reciprocal lattice of a crystal. For a one-dimensional crystal like a hydrogen chain, the first Brillouin zone consists of a single interval in reciprocal space. The reciprocal lattice of the chain is given by a set of plane waves with wave vectors that are integer multiples of the fundamental wave vector "k" defined as:

$k = \frac{2\pi}{a}$

The first Brillouin zone is defined as the region of reciprocal space that is bounded by the planes that bisect the line connecting the origin (k = 0) to the first reciprocal lattice point. For a one-dimensional hydrogen chain, the first reciprocal lattice point is located at k = ±k, where k is the fundamental wave vector defined above.

Therefore, the first Brillouin zone for a hydrogen chain is simply the interval between -k and k in reciprocal space, which is a segment of length 2k. In other words, any wave vector in the first Brillouin zone can be written as:

$k_1 = \pm k + \delta$

where $\delta$ is a wave vector that lies within the first Brillouin zone.

## Band-structure of solids

In the discussion of the electronic bandstructure of simple solids, it is important to consider the contribution of different types of atomic orbitals, including s-, p-, and d-orbitals. The electronic bandstructure of a solid is determined by the interaction between the electrons and the crystal lattice potential, which is affected by the shape and orientation of the atomic orbitals.

In general, s-orbitals are more isotropic, meaning they have a more symmetric distribution of electron density around the nucleus, while p- and d-orbitals are more anisotropic, meaning they have a directional preference for electron density. This difference in symmetry affects how the orbitals interact with each other and with the crystal lattice potential, which in turn affects the electronic bandstructure of the material.

In a simple metal, such as copper, the valence band is composed primarily of s-orbitals, which are delocalized throughout the crystal lattice. This delocalization allows electrons to move freely through the material and conduct electricity. In a semiconductor or insulator, the valence band is typically composed of a combination of s- and p-orbitals, while the conduction band is composed of unoccupied p- and d-orbitals that are able to participate in conduction when excited.

The energy levels of the different orbitals can also affect the electronic bandstructure. For example, in a semiconductor, the energy levels of the s- and p-orbitals can be tuned by doping the material with impurities, which can shift the location of the Fermi level and affect the conductivity of the material. In a material with a large number of d-electrons, such as a transition metal oxide, the d-orbitals can also contribute to the electronic bandstructure and play a role in the material's electronic and magnetic properties.

In summary, the contribution of different types of atomic orbitals, including s-, p-, and d-orbitals, is an important factor in determining the electronic bandstructure of simple solids. The symmetry and energy levels of the orbitals affect how they interact with each other and with the crystal lattice potential, which in turn determines the electrical and optical properties of the material.

### First Brillouin zone revisted

The concept of the first Brillouin zone applies to any periodic solid in three dimensions, not just one-dimensional hydrogen chains.

In a three-dimensional solid, the first Brillouin zone is a polyhedron in reciprocal space that is bounded by the planes that bisect the lines connecting the origin (k = 0) to the reciprocal lattice points closest to the origin. These reciprocal lattice points are the nearest neighbors of the origin, and the first Brillouin zone represents the region of reciprocal space that is closest to the origin.

The shape of the first Brillouin zone depends on the crystal structure of the solid. For example, in a simple cubic lattice, the first Brillouin zone is a cube centered at the origin, with each face of the cube corresponding to a reciprocal lattice plane. In a face-centered cubic lattice, the first Brillouin zone is a truncated octahedron, while in a body-centered cubic lattice, the first Brillouin zone is a rhombic dodecahedron.

The first Brillouin zone is important in the study of the electronic and vibrational properties of solids. In particular, the band structure of solids, which describes the allowed energy levels of electrons in the crystal, is typically plotted over the first Brillouin zone. The shape of the Brillouin zone affects the density of states, the effective mass of electrons, and other electronic properties of the solid.


## Denisty of states
The density of states (DOS) is a function that describes the number of states available at each energy level in a solid. It is closely related to the band structure of the solid, which is a graph of the allowed energy levels for electrons in the solid. The band structure and DOS are related through the following equation:

\begin{equation}
D(E) = \frac{1}{V}\sum_{i=1}^{N}\delta(E - E_i)
\end{equation}

where $D(E)$ is the density of states at energy $E$, $V$ is the volume of the solid, $N$ is the total number of energy levels in the solid, and $\delta$ is the Dirac delta function. The energy levels $E_i$ are obtained from the band structure calculation.

The above equation states that the density of states at an energy level $E$ is proportional to the number of energy levels that have an energy equal to $E$. In other words, the DOS gives the number of available energy states at a given energy level. The band structure, on the other hand, provides information about the allowed energy levels in the solid, and the corresponding energy ranges where electrons can exist.

In summary, the band structure and density of states are intimately connected, with the band structure providing information on the allowed energy levels and the density of states providing information on the number of available energy states at each energy level.

### Note-book
<a target="_blank" href="https://colab.research.google.com/github/jollactic/Modelling_course/blob/main/ES/Tutorial.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


<div class="warning" style='padding:0.1em; background-color:#E9D8FD; color:#69337A'>
<span>
<p style='margin-top:1em; text-align:center'>
<b>Assignment:</b></p>
<p style='margin-left:1em;'>
Go through the jupyter note-book and consider the example for TiO<sub>2</sub> provided at the 'DFTB+ recipies' <a href="https://dftbplus-recipes.readthedocs.io/en/latest/basics/bandstruct.html">page</a>. Reproduce their results using the functions and proceduers detailed in the our note-book. Maks sure to address the questions in the notebook.

<p style='margin-top:1em; text-align:center'>
<b>Submission instructions:</b></p>
<p style='margin-left:1em;'>

<p style='margin-left:1em;'>
Upload your commented version of the note-book to the studium page. 


</p></span>
</div>

### Further reading:

1. [*How Chemistry and Physics Meet in the Solid State* By Roald Hoffmann](https://onlinelibrary.wiley.com/doi/epdf/10.1002/anie.198708461)

2. [Chapter 2 and 3 in *Computational Chemistry of Solid State Materials : A Guide for Materials Scientists, Chemists, Physicists and Others* Computational Chemistry of Solid State Materials : A Guide for Materials Scientists, Chemists, Physicists and Others](https://ebookcentral.proquest.com/lib/uu/reader.action?docID=481650#)
