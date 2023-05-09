# ELECTRONIC STRUCTURE - Density Functional Theory (DFT)
Density Functional Theory (DFT) is a quantum mechanical modeling technique used to calculate the electronic structure of materials. It is based on the concept of the electron density, which is the probability of finding an electron at a particular point in space.

DFT allows for the calculation of a material's electronic properties by solving the Schrödinger equation using the electron density instead of the wave function. This greatly simplifies the calculation, making it more computationally efficient than other methods.

The main idea behind DFT is to approximate the unknown functional dependence of the electron density on the external potential, by using an approximate exchange-correlation functional. This functional accounts for the repulsive interactions between electrons and the attractive interactions between electrons and the positively charged atomic nuclei.

DFT has become an essential tool in materials science, chemistry, and physics, and has been used to study a wide range of systems, including atoms, molecules, surfaces, and bulk materials.

## Thomas-Fermi theory
Consider a system of electrons in a uniform, positively charged background potential $V(r)$. We assume that the electrons are free to move in three dimensions but are confined to a box of volume $V$. The wavefunction of the particle is given by:

\begin{equation}
\psi_{n_x,n_y,n_z}(x,y,z) = \sqrt{\frac{8}{L_x L_y L_z}} \sin\left(\frac{n_x \pi x}{L_x}\right) \sin\left(\frac{n_y \pi y}{L_y}\right) \sin\left(\frac{n_z \pi z}{L_z}\right),
\end{equation}

where $n_x$, $n_y$, and $n_z$ are non-negative integers associated with the three dimensions of the box.

The allowed energies of the particle are given by:

\begin{equation}
E_{n_x,n_y,n_z} = \frac{\hbar^2\pi^2}{2m}\left(\frac{n_x^2}{L_x^2} + \frac{n_y^2}{L_y^2} + \frac{n_z^2}{L_z^2}\right),
\end{equation}

where $m$ is the mass of the particle.

We can count the number of states with energy less than or equal to $E$ by considering the volume of momentum space that corresponds to those states. Specifically, the volume of momentum space corresponding to energies less than or equal to $E$ is the volume of a sphere of radius $p$ in momentum space, where $p$ is related to $E$ through:

\begin{equation}
E_{n_x,n_y,n_z} = \frac{p^2}{2m}.
\end{equation}

Solving for $p$ in terms of $E$ yields:

\begin{equation}
p = \sqrt{2mE}.
\end{equation}

The volume (in the first octant) of the sphere in momentum space is then given by:

$$
V_{\mathrm{sphere}} = \frac{1}{8}\frac{4}{3}\pi p^3 = \frac{1}{8}\frac{4}{3}\pi\left(\frac{2mE}{\hbar^2}\right)^{3/2}.
$$
To count the number of states in this volume, we need to take into account the non-negativity of the quantum numbers. Specifically, we only need to count one octant of the momentum space, corresponding to the positive values of $n_x$, $n_y$, and $n_z$. 

Taking into account this restriction on the quantum numbers, the density of states at given energy as:

$$
g(E) = \frac{dN}{dE} = \frac{1}{8}\frac{4\pi}{(2\pi/L)^3} \left(\frac{2mE}{\hbar^2}\right)^{3/2} = \frac{V_{box}}{16\pi^2} \left(\frac{2m}{\hbar^2}\right)^{3/2} E^{1/2},
$$

where $V_{box}=L_x L_y L_z$ is the volume of the box.

Finally, we can use the density of states $g(E)$ to calculate the total number of states $N$ with energy less than or equal to $E$:

$$
N(E) = \int_0^E g(E') dE' = \frac{V}{16\pi^2} \left(\frac{2m}{\hbar^2}\right)^{3/2} \int_0^E E'^{1/2} dE' = \frac{V}{16\pi^2} \left(\frac{2m}{\hbar^2}\right)^{3/2} \frac{2}{5}E^{5/2}.
$$

![DOS](dos_animation.gif)
***Figure.*** *Illustration showing the relation between quantum numbers and denisty of states.*


The total number of electrons in the system is given by:

$$
N = \int_{0}^{E_F} g(E) dE,
$$

From which we can write:

$$
N = \frac{V}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{1/2} \int_{0}^{E_F} E^{1/2}  dE.
$$

We have assumed that the termperature is small eneough that we can ignore the fact that electrons should occupied in accorande with the Fermi distribution.

With these assumptions, we can evaluate the integral and find an expression for the electron density $\rho(r)$ as a function of the local potential $V(r)$:

$$
\rho(r) = \frac{m}{3\pi^2\hbar^3} (E_F - V(r))^{3/2}.
$$

This is the Thomas-Fermi equation, which relates the electron density to the local potential in the system. It can be used to calculate the electron density and potential in a wide range of systems, including atoms, molecules, and solids. However, the method is not very accurate.

<video width="400" controls>
  <source src="..\_static\TF.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

***Thomas-Fermi theory.***


## Kohn-Sham DFT (KS-DFT)

Kohn-Sham Density Functional Theory (KS-DFT) is a variant of Density Functional Theory that was developed by Walter Kohn and Pierre Hohenberg in 1964. It is based on the idea of mapping the many-body Schrödinger equation for a system of interacting electrons onto a set of non-interacting electrons in a self-consistent potential.

In KS-DFT, the total energy of the system is expressed as a functional of the electron density, similar to other DFT methods. However, instead of using a single electron density for the whole system, KS-DFT employs a set of auxiliary non-interacting electrons, known as Kohn-Sham orbitals, that satisfy an auxiliary set of equations. The electron density is then calculated from the Kohn-Sham orbitals.

KS-DFT has several advantages over the Hartree-Fock (HF) method, another popular method for calculating electronic structures. Firstly, KS-DFT accounts for electron correlation effects, which are not included in the HF method. This makes KS-DFT more accurate for systems with strongly correlated electrons, such as transition metal complexes or systems with strong electron-electron interactions.

Secondly, KS-DFT is computationally more efficient than HF, as it does not require the calculation of two-electron integrals, which can be very expensive for larger systems. Finally, KS-DFT is capable of accurately describing the properties of a wide range of materials, including metals, insulators, and semiconductors, whereas HF is generally limited to describing non-metallic systems.

Overall, KS-DFT has become one of the most widely used methods for calculating electronic structures, due to its accuracy and efficiency for a wide range of systems.


The key equations for Kohn-Sham Density Functional Theory (KS-DFT) are:

The Kohn-Sham equations:

$$\left[ -\frac{\hbar^2}{2m}\nabla^2 + V_{\text{ext}}(\mathbf{r}) + V_{\text{Hxc}}[\rho(\mathbf{r})] \right] \phi_i(\mathbf{r}) = \epsilon_i \phi_i(\mathbf{r})$$

where $\phi_i(\mathbf{r})$ are the Kohn-Sham orbitals, $\epsilon_i$ are the corresponding eigenvalues, $m$ is the electron mass, $V_{\text{ext}}(\mathbf{r})$ is the external potential, and $V_{\text{Hxc}}[\rho(\mathbf{r})]$ is the Hartree-exchange-correlation potential, which depends on the electron density $\rho(\mathbf{r})$.

The electron density:

$$\rho(\mathbf{r}) = \sum_{i=1}^N |\phi_i(\mathbf{r})|^2$$

where $N$ is the number of electrons in the system.

The total energy:

$$E_{\text{KS}}[\rho(\mathbf{r})] = T_{\text{s}}[\rho(\mathbf{r})] + E_{\text{ext}}[\rho(\mathbf{r})] + E_{\text{H}}[\rho(\mathbf{r})] + E_{\text{xc}}[\rho(\mathbf{r})]$$

where $T_{\text{s}}[\rho(\mathbf{r})]$ is the kinetic energy of the non-interacting Kohn-Sham electrons, $E_{\text{ext}}[\rho(\mathbf{r})]$ is the external potential energy, $E_{\text{H}}[\rho(\mathbf{r})]$ is the Hartree energy due to electron-electron repulsion, and $E_{\text{xc}}[\rho(\mathbf{r})]$ is the exchange-correlation energy, which accounts for the effects of electron correlation.


The self-consistent field (SCF) procedure is used to solve the Kohn-Sham equations iteratively until the electron density and total energy converge to a self-consistent solution.


## Functionals 

![MinImage](LDA_Dens2Pot.png)
***Figure.*** *The connection between electron density and exchange-correlation potential in the Local Density Approximation (LDA). For each volume element of the density we mapp from local potential to local denisty. In each mapping, we treat the system as being a homogenous system with a uniform denisty $\mathbf{\rho}(r')$. *

Density Functional Theory (DFT) functionals are mathematical expressions that describe the exchange-correlation energy of a system in terms of the electron density. There are many different types of functionals, each with its own set of strengths and weaknesses.

Two of the most commonly used functionals are the Local Density Approximation (LDA) and the Perdew-Burke-Ernzerhof (PBE) functional.

LDA is a simple functional that assumes that the exchange-correlation energy depends only on the local electron density at each point in space. This makes LDA computationally efficient, but it can lead to inaccuracies in describing certain electronic properties, such as band gaps and magnetic properties.

PBE, on the other hand, is a more sophisticated functional that includes both local and non-local contributions to the exchange-correlation energy. This makes PBE more accurate than LDA for a wider range of electronic properties, but also more computationally expensive.

Overall, the choice of functional depends on the specific system being studied and the level of accuracy required. LDA may be sufficient for some applications, while PBE may be necessary for others. Other functionals, such as hybrid functionals, are also available and can provide an even higher level of accuracy in some cases.


The Local Density Approximation (LDA) and Perdew-Burke-Ernzerhof (PBE) functionals are expressed in terms of the electron density, $\rho(\mathbf{r})$. The key equations for LDA and PBE are:

LDA functional:

$$E_{\text{xc}}^{\text{LDA}}[\rho(\mathbf{r})] = \int \rho(\mathbf{r}) \epsilon_{\text{xc}}^{\text{LDA}}(\rho(\mathbf{r})) d\mathbf{r}$$

where $\epsilon_{\text{xc}}^{\text{LDA}}(\rho(\mathbf{r}))$ is the exchange-correlation energy density at each point in space, which is a function of the local electron density.

PBE functional:

$$E_{\text{xc}}^{\text{PBE}}[\rho(\mathbf{r})] = \int \rho(\mathbf{r}) \epsilon_{\text{xc}}^{\text{PBE}}(\rho(\mathbf{r}), \nabla \rho(\mathbf{r})) d\mathbf{r}$$

where $\epsilon_{\text{xc}}^{\text{PBE}}(\rho(\mathbf{r}), \nabla \rho(\mathbf{r}))$ is the exchange-correlation energy density, which depends not only on the electron density, but also on its gradient.

In practice, the exchange-correlation energy density is typically approximated using various forms of parameterization or interpolation, based on experimental data or computational simulations. The resulting functional is then used to calculate the total energy of the system and optimize the electron density self-consistently.

## Reduced density gradient ($s$)

The reduced density gradient is a concept used in Density Functional Theory (DFT) to describe the local kinetic energy density of electrons in a system. It is defined as:

$$s = \frac{\left| \nabla \rho \right|}{2\rho^{4/3}}$$

where $\rho$ is the electron density and $\left| \nabla \rho \right|$ is the magnitude of its gradient. The reduced density gradient provides a measure of the electron density's curvature and how quickly it changes in space.

The reduced density gradient has been shown to be useful in predicting various molecular properties, including reactivity, aromaticity, and stability. It is often used in conjunction with DFT functionals, such as the Perdew-Burke-Ernzerhof (PBE) functional, to improve the accuracy of calculations.

Overall, the reduced density gradient is a powerful tool for analyzing and predicting the behavior of electrons in molecular systems, and it is an important concept in the field of computational chemistry.

### Expressing the PBE functional using $s$

The Perdew-Burke-Ernzerhof (PBE) functional can be written in terms of the reduced density gradient, $s$, as:

$$E_{\text{xc}}^{\text{PBE}}[\rho(\mathbf{r})] = \int \rho(\mathbf{r}) \epsilon_{\text{xc}}^{\text{PBE}}(\rho(\mathbf{r}), s(\mathbf{r})) d\mathbf{r}$$

where $\epsilon_{\text{xc}}^{\text{PBE}}(\rho(\mathbf{r}), s(\mathbf{r}))$ is the exchange-correlation energy density, which depends not only on the electron density, but also on its reduced density gradient.

The PBE functional takes into account both local and non-local contributions to the exchange-correlation energy, which makes it more accurate than the Local Density Approximation (LDA) for a wider range of electronic properties. The inclusion of the reduced density gradient in the PBE functional further improves its accuracy by capturing the non-local behavior of electrons in a system.


<video width="400" controls>
  <source src="..\_static\DFT.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

***Density Functional Theory***

## Tutorial

Basic tutorial: 

<a target="_blank" href="https://colab.research.google.com/github/jollactic/Modelling_course/blob/main/DFT/Tutorial_1.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

In this tutorial orginally written by Ask Hjorth Larsen and Keenan Lyon at DTU we consider a simple DFT code for a 1D system. The example represent a grid-based approach were we do not use analytical basis-functions.

Advanced tutorial:

In this tutorial we follow closely the presentation in Chapter 2 in the thesis entitled [Transition metal and alloy catalysts
in the light of computational materials modelling](https://www.diva-portal.org/smash/get/diva2:1598427/FULLTEXT01.pdf) by Ageo Meier De Andrade. The thesis (Chapter 2 in particular) give an excellent overview of DFT in the cotext of materials science, it is must-read!

<a target="_blank" href="https://colab.research.google.com/github/jollactic/Modelling_course/blob/main/DFT/Tutorial_2.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


<div class="warning" style='padding:0.1em; background-color:#E9D8FD; color:#69337A'>
<span>
<p style='margin-top:1em; text-align:center'>
<b>Assignment:</b></p>
<p style='margin-left:1em;'>
Write a short (maximum 2-pages) summary that includes:

<p style='margin-left:1em;'>
1. A brief overview of the concept of the `Jacob’s ladder of density functional approximations`.


<p style='margin-left:1em;'>
2. A case study comparing LDA and PBE in terms of how they describe the lattice constant and cohesive energies of simple monatomic solids. Relate you findings to the reduced gradient distribution of the atom and the solid. The advanced tutorial includes a comparison of LDA and PBE for diamond. 


<p style='margin-left:1em;'>
Note that parameters like basis-set quality and k-point sampling in the tutorial have not been fully optimized in the example. Results could therefore be at variance with reference values in the literature. The general behvaiour in terms of the LDA and PBE behaviour is still well captured. 


</p></span>
</div>

### Further reading:

1. [Chapter 2 in *Computational Chemistry of Solid State Materials : A Guide for Materials Scientists, Chemists, Physicists and Others* Computational Chemistry of Solid State Materials : A Guide for Materials Scientists, Chemists, Physicists and Others](https://ebookcentral.proquest.com/lib/uu/reader.action?docID=481650#)

2. [*Nobel Lecture: Electronic structure of matter—wave functions and density functionals* by Walter Kohn](https://journals.aps.org/rmp/pdf/10.1103/RevModPhys.71.1253)

3. [*Transition metal and alloy catalysts in the light of computational materials modelling* Ageo Meier De Andrade](https://www.diva-portal.org/smash/get/diva2:1598427/FULLTEXT01.pdf)

4. [Chapter 9 in *Atomistic Computer Simulations : A Practical Guide* by Veronika Brázdová and David R. Bowler](https://ebookcentral.proquest.com/lib/uu/reader.action?docID=1161544)