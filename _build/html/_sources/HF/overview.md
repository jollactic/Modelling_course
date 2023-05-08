# ELECTRONIC STRUCTURE - Hartee-Fock (HF)
The Hartree-Fock method (HF) is a brute force way of solving the many-body electronic Schrödinger equation:

$$
\\
\widehat{H} \Psi(\mathbf{r}_\textup{1},\mathbf{r}_\textup{1},\cdots,\mathbf{r}_\textup{N}) = E \Psi(\mathbf{r}_\textup{1},\mathbf{r}_\textup{1},\cdots,\mathbf{r}_{\textup{N}})
\\
$$

by performing a number of approximations/simplifications. In the following we will go through all steps in this simplification process, but first we will have a look at the Schrödinger equation (SE) itself in a bit more detail.   

## The Born-Oppenheimer approximation
The Born-Oppenheimer approximation allows for the separation of the motion of atomic nuclei and electrons in a molecule.
The Born-Oppenheimer approximation is based on the observation that the mass of atomic nuclei is so much greater than that of the electrons, that the nuclei are so much slower compared the electrons that they can be considered as being fixed in relation to the electrons. This allows for the separation of the electronic and nuclear motion, and the electronic energy can be calculated while treating the nuclear positions as fixed. This approximation is justified by the adiabatic theorem, which states that if a system evolves slowly enough, its wave function will remain in the instantaneous eigenstate of the Hamiltonian. In the case of the Born-Oppenheimer approximation, the electronic motion is assumed to be fast enough that the wave function remains in the electronic ground state while the nuclear positions change slowly. Therefore, the electronic energy can be calculated independently of the nuclear positions, and the nuclear motion can be treated separately.

## The Schrödinger equation and the Hamiltonian

There are two central objects in the Schrödinger equation. i) The Hamlitonian $\widehat{H}$, and, ii) the wavefunction $\Psi$. The Hamiltonian describes all the interactions in the system. In our case, dealing with materials and molecules, these are: 

1. The kinetic energy of all the electrons, $\widehat{T}_e$
2. The electro-static (attractive) interaction between all nuclii and electrons, $\widehat{V}_{Ne}$
3. The electro-static (repulsive) interaction between all electrons, $\widehat{V}_{ee}$ (The real trouble-maker!)

Thus:

$$
\\
\widehat{H}= \widehat{T}_e + \widehat{V}_{Ne} + \widehat{V}_{ee}
\\
$$

with:

$$
\\
\widehat{T}_e = -\frac{1}{2}\sum_{i=1}^{N}\nabla^2_{i}
\\
\widehat{V}_{Ne}=-\sum_{j=1}^{M}\sum_{i=1}^{N} \frac{Z_j}{\left | \textbf{R}_\textup{j}-\textbf{r}_\textup{i} \right |}
\\
\widehat{V}_{ee}=\sum_{j=1}^{N}\sum_{i=1}^{N} \frac{1}{\left | \textbf{r}_\textup{j}-\textbf{r}_\textup{i} \right |}
\\
$$

M and N above refer to the number of nuclei and electrons, respectively. Although the equation is relatively easy to write down for a general system, it is very difficult or impossible to find the solution to the equation and obtain the wavefunction. The Hartree-Fock method is one way forward.


<video width="400" controls>
  <source src="..\_static\BO_SE.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

***Born-Oppenheimer approximation and the electronic Schrödinger equation.***



## The Hartree (without Fock) method and simplified notation

A major problem of the SE is the fact that the wavefunction (in general) has too many variables (we have three spacial variables per electron) and there is no simple way of separating them. In the Hartree (without Fock) method we allow for some separation of variables by restricting our wavefunction to be described as a product (Hartree-product) of one-electron wavefunctions (orbitals):

$$
\\
\Psi(\mathbf{r}_\textup{1},\mathbf{r}_\textup{1},\cdots,\mathbf{r}_{\textup{N}})=\chi_1(\mathbf{r}_\textup{1})\chi_2(\mathbf{r}_\textup{2})\cdots\chi_{\textup{N}}(\mathbf{r}_{\textup{N}})
\\
$$

 Note that this form for the wavefunction would be exact if electrons were not interacting with each other and if we disregard the fact that a wavefunction should be anti-symmetric (the sign of the wavefunction must change sign when two electrons are exchanged). Fock will fix the anti-symmetry problem, but first lets see how we could work with the Hartree (without Fock) method. 

### Energy of a Hartree product
The energy of a system described by a Hartree-product is:

$$
\\
E = \int\int\cdots \int \overline{\chi}_1(\mathbf{r}_\textup{1})\overline{\chi}_2(\mathbf{r}_\textup{2})\cdots\overline{\chi}_{\textup{N}}(\mathbf{r}_{\textup{N}}) \widehat{H}\chi_1(\mathbf{r}_\textup{1})\chi_2(\mathbf{r}_\textup{2})\cdots\chi_{\textup{N}}(\mathbf{r}_{\textup{N}}) d\mathbf{r}_{\textup{1}}d\mathbf{r}_{\textup{2}} \cdots d\mathbf{r}_{\textup{N}}
\\
$$

$\overline{\chi}_1(\mathbf{r}_\textup{1})$ refer to the complex conjugate. To make things tracable we need to use a better notation! Bra-ket notation will help us along. In this notation intergrals are replaced with $\left \langle   \right \rangle$ and wavefunctions are used refered to by their index.  With this notation we can write:

$$
\\
E = \left \langle 12\cdots N\left | \widehat{H} \right | 12\cdots N  \right \rangle
\\
$$

We will soon use the explicit form the of Hamiltonian with all the separate terms. Thus we also simplify the notation of the terms emerging there in the following way:

$$
\\
 \sum_{i=1}^{N}h_i=\widehat{T}_e + \widehat{V}_{Ne} = -\frac{1}{2}\sum_{i=1}^{N}\nabla^2_{i}-\sum_{j=1}^{M}\sum_{i=1}^{N} \frac{Z_j}{\left | \textbf{R}_\textup{j}-\textbf{r}_\textup{i} \right |}
\\
$$

and 

$$
\\
 \sum_{i=1}^{N}\sum_{j=1}^{N} r_{ij}^{-1} = \widehat{V}_{ee}=\sum_{j=1}^{N}\sum_{i=1}^{N} \frac{1}{\left | \textbf{r}_\textup{j}-\textbf{r}_\textup{i} \right |}
\\
$$

if we plug it all in we can write:

$$
\\
E = \left \langle 12\cdots N\left | \sum_{i=1}^{N}h(i) + \sum_{i=1}^{N}\sum_{j=1}^{N} r_{ij}^{-1} \right | 12\cdots N  \right \rangle = 
\\
=\sum_{i=1}^{N} \left \langle 12\cdots N\left |h(i) \right | 12\cdots N  \right \rangle + \sum_{i=1}^{N} \sum_{j=1}^{N}  \left \langle 12\cdots N \left | r_{ij}^{-1} \right | 12\cdots N  \right \rangle
\\
$$

Let't look at one of the terms in this expression:

$$
\\
\left \langle 12\cdots N\left |h(i) \right | 12\cdots N  \right \rangle 
= \left \langle 1 | 1 \right \rangle \left \langle 2 | 2 \right \rangle \cdots \left \langle i |h(i)| i \right \rangle \cdots \left \langle N-1 | N-1 \right \rangle \left \langle N | N \right \rangle 
= \left \langle i |h(i)| i \right \rangle
\\
$$

we have used the following basic rules for integrals in simpifying the expression:

$$
\\
\int \int [f(x)+g(y)]dxdy=\int f(x)dx + \int g(y)dy
\\
\\
\int \int f(x)g(y)dxdy=\int f(x)dx\int g(y)dy
\\
$$

togheter with the standard property of wavefunctions (and orbitals), namely that:

$$
\\
\left \langle i |i \right \rangle=1 
\\
$$

and

$$
\\
\left \langle i |j \right \rangle=0 \  (i \ne j) 
\\
$$

the simplification comes about. 

```{note}
When integrating over many variables, we can collect all functions that depend on the same variable and 'package' them togheter into many small integrals. Many of these integrals are equal to 1 which allow us to simplify intimidating expression emerging in the derivation of the HF method. 
```

We can also simplify the expressions inside the double sum as follows:

$$
\\
\left \langle 12\cdots N \left | r_{ij}^{-1} \right | 12\cdots N  \right \rangle
= \left \langle 1 | 1 \right \rangle \left \langle 2 | 2 \right \rangle \cdots \left \langle ij \left | r_{ij}^{-1} \right | ij \right \rangle \cdots \left \langle N-1 | N-1 \right \rangle \left \langle N | N \right \rangle 
= \left \langle ij \left | r_{ij}^{-1} \right | ij \right \rangle
\\
$$

The reason that we are left with a double integral is because we can not factorize the term $r_{ij}^{-1}$. 


```{note}
We can see that this should be so by comparing to:
$
\frac{1}{\left | x-y \right |}\neq f(x)g(y)
$
```

At last! We have a neat expression for the energy:

$$
\\
E =\sum_{i=1}^{N} \left \langle i \left |h(i) \right | i \right \rangle + \sum_{i=1}^{N} \sum_{j=1}^{N}  \left \langle  ij \left | r_{ij}^{-1} \right | ij  \right \rangle
\\
$$

### Minimizing the energy of a Hartree product

The true ground-state wavefunction of a system minimize the energy. We can therefore find the best approximation to the true wavefunction by minimizing the Hartree energy with respect to the orbitals:

$$
\\
\frac{\partial E}{\partial \chi_\textup{i}}=0
\\
$$

```{note}
When taking a partial derivative of a sum of functions, all functions not depending on the varialble of intersest dissapears. Eq:
$
\frac{\partial [f(x)+g(y)]}{\partial x}=\frac{df(x)}{dx}
$
```

With some algebra (omitted here) we arrive at:

$$
\\
f_\textup{i}\chi_\textup{i}=\varepsilon \chi_\textup{i}
\\
$$

with:

$$
\\
f_\textup{i} = h_\textup{i} + \sum_{j=1;j\ne i}^{N} \textbf{J}_j(\textbf{r}_\textup{i})
\\
$$

where $h_\textup{i}$ is the same as before and $\textbf{J}_j(\textbf{r}_\textup{i})$ is called a Coulomb operator and describes the average electrostatic field that electron $i$ experience from a second electron $j$. 

$$
\\
\textbf{J}_j(\textbf{r}_\textup{i}) = \int \chi_\textup{j}^*(\textbf{r}_\textup{j})r_{ij}^{-1} \chi_\textup{j}(\textbf{r}_\textup{j}) d\textbf{r}_\textup{j}
\\
$$

The Coulomb operator $\textbf{J}_j(\textbf{r}_\textup{i})$ is often written in a more condensed form as;

$$
\\
\textbf{J}_j(1) = \int \overline{\chi}_\textup{j}(2)r_{12}^{-1} \chi_\textup{j}(2) d\textbf{r}_\textup{2}
\\
$$

Note that $\overline{\chi}_\textup{j}(2)\chi_\textup{j}(2)$ correspond the probablity (electron) densisty of an electron.

Before we get too far, we should stop and fix a major flaw that is being overlooked in the Hartree (without Fock) approach. We therefore turn to the Hartree-Fock approach which deals with this flaw.

<video width="400" controls>
  <source src="..\_static\HwoF.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

***Hartree equation.***


## The Hartree-Fock equation

The problem with the Hartee approach is that the Hartree product do not fulfill the requirement that a wavefunction should be antisymmetric. Antisymmetry means that the wavefunction should change sign when two electrons are replaced. It is easy to verify that this is not the case for a Hartree product (Try it yourself!). A solution to this problem is to use a so-called Slater deteriminant:

$$
\\
\Psi= \frac{1}{\sqrt{N!}}\left | \begin{matrix}
\chi_\textup{1}(\textbf{r}_\textup{1}) & \chi_\textup{2}(\textbf{r}_\textup{1}) & \cdots & \chi_\textup{N}(\textbf{r}_\textup{1}) \\ 
\chi_\textup{1}(\textbf{r}_\textup{2}) & \chi_\textup{2}(\textbf{r}_\textup{2}) & \cdots & \chi_\textup{N}(\textbf{r}_\textup{2}) \\ 
\vdots  & \vdots  & \ddots  & \vdots \\ 
\chi_\textup{1}(\textbf{r}_\textup{N}) & \chi_\textup{2}(\textbf{r}_\textup{N}) & \cdots & \chi_\textup{N}(\textbf{r}_\textup{N}) 
\end{matrix} \right |
\\
$$

If we follow a similar proceedure as for the Hartree method we can eventually reach to a suprisingly simiar set of equations:

$$
\\
f_\textup{i}\chi_\textup{i}=\varepsilon \chi_\textup{i}
\\
$$

with:

$$
\\
f_\textup{i} = h_\textup{i} + \sum_{j=1}^{N} \left [  \textbf{J}_j(\textbf{r}_\textup{i})-\textbf{K}_j(\textbf{r}_\textup{i})\right ]
\\
$$

the new term $\textbf{K}_j(1)$ is called exchange and is given by:

$$
\\
\textbf{K}_j(1) \chi_i (1)= \left [ \int \chi_\textup{j}^*(2)r_{12}^{-1} \chi_\textup{i}(2) d\textbf{r}_\textup{2}   \right ]\chi_j(1)
\\
$$

the term looks horrid, and it is... It does not have a classical counter part and emerges as a result of the many permuation of orbital products in the Slater deterimant. We can note that $\mathbf{K}$ describe some an attractive electric field, a field that reduces the Coulomb repulsion between the electrons in our orbitals.

```{note}
Electrons in the real many-body system do only feel repulsive interactions between them. However, an average electric field would overestimate this repulsion since electrons could coordinate their movement to always stay rather far apart. We cannot describe such effects in our approach since our anzats is that our wavefunctions can be described with a construction that is only strictly valid if electrons do not interact.   
```

### Self Consistent Field

Since the Hartree operators $f_\textup{i}$ depend on $\chi$ which in turn should be found by solving an equation involving $f_\textup{i}$ we are trapped in a catch 22. In order to proceed we need to solve the equation iteratively. 

1. We start with an initial guesss for set of $\chi$
2. We calculate $f_i$ using the current set of $\chi$
3. We solve $f_\textup{i}\chi_\textup{i}=\varepsilon \chi_\textup{i}$ to get a new set of $\chi$
4. We repeat steps 2 and 3 until we get bask the same set as we put in. We have now found a set of $\chi$ that generates a Self Consistent Field (SCF).



```{note}
Self Consistent Field (SCF) is used to describe the whole approach given in list above.
```

<video width="400" controls>
  <source src="..\_static\HF.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

***Hartree-Fock equation.***

### Numerical solution (Roothan-Hall equations)

The SCF approach is a large step on the way to finding an approximation to the many electron wavefunction. However, solving equation involving both integrals and gradients it too though to be generally applicable. We therefore proceed with a numerical approach. We limit our choice for the unknown $\chi$ to functions that can be described as linear combinations of known functions. A reasonable choice is to use atomic orbitals (solutions to the Schrödinger equation where we only have one electron and a single nuclei). This approach is very intutive to a chemist and is the basis for molecular orbital theory. Thus we make the anzats:

$$
\\
\chi_\textup{i}= \sum_{a=1}^{N_{basis}}c_{ai}\phi_k 
\\
$$

if $\phi$ whould be atomic orbitals, this is a linear combination of atomic orbitals (LCAO). In practice we often use a simpler set of mathematical functions that are easier to work with. However, the functions are typically similar to real atomic orbitals and centered around the atoms.


We can re-write our analytical equations in terms of a liner algebra problem by first pluging in our linear combination in our equation for $f_\textup{i}\chi_\textup{i}=\varepsilon \chi_\textup{i}$ and then performing some clever manipulation including multiplications of $\phi_k$ and integration.

The key enabaler in this transformation is that integrals involving products of known functions (our basis-functions) and coeffencient $c_{ai}$ and $\phi_k$ can be written as constants time our coefficients. For example:

$$
\\
\int c_{ai} \phi_a (\textbf{r}_\textup{1})r_{12}^{-1} c_{ai}\phi_a(\textbf{r}_\textup{1}) d\textbf{r}_\textup{1} = c_{ai}c_{ai}\int  \phi_k (\textbf{r}_\textup{1})r_{12}^{-1} \phi_k(\textbf{r}_\textup{1}) d\textbf{r}_\textup{1}=c_{ai}c_{ai} \times \textup{Constant}
\\
$$

where the 'Constant' can be computed analytically or with numerical techniques. Before proceeding further we will stop for a little while and make another simplification. Electrons comes in two "flavours" spin up and spin down. If we assume that we can pair them up two have each orbital occupying we can "slash the problem in half". This is called restricted Hartree-Fock.

```{note}
In the restricted HF we only need to consider N/2 electrons. The other half is simply a mirror image but with spin down instead of spin up.
```


 In the end we arrive at the Roothan-Hall equations:

$$
\\
\mathbf{F}\mathbf{C}=\mathbf{S}\mathbf{C}\mathbf{E}
\\
$$

```{note}
A more complete derivation of the steps that takes us to the linear algebra equation can be found for example in Andrew R Leach book "Molecular modelling" or in the book by Szabo and Östlund called "Modern Quantum Chemistry". 
```

We will now look at the matrices one by one.

1. $\mathbf{C}$ is an $(N_{basis}\times N_{basis})$ matrix collecting all $c_{ij}$ coeffecients. These are our unknowns that we should find in order to present an approximation to the many electron wavefunction. Each column $i$ of $\mathbf{C}$ correspond to a $\chi_\textup{i}$.

2. $\mathbf{S}$ is an $(N_{basis}\times N_{basis})$ matrix called overlap matrix and collect integrals of the following type: 

$$
\\
\mathbf{S}_{ab}=\left \langle \phi_a|\phi_b  \right \rangle
\\
$$

Note that basis-functions have no requirements to be orthonormal.

3. $\mathbf{F}$ is an $(N_{basis}\times N_{basis})$ matrix corresponding to all term that we can trace to the original operators in our Hamiltonian, this is the really intersting term! In a sense, $\mathbf{F}$ is the "linear algebra" counter part of \widehat{H}.

Let's look a bit closer at $\mathbf{F}$ which can be written as:

$$
\\
\mathbf{F}_{ab}=\mathbf{T}_{ab}+\mathbf{V}_{ab}+ \sum_{j}^{N/2}\sum_{c}^{N_{basis}}\sum_{d}^{N_{basis}} c_{ci}c_{di}\left [  2\mathbf{J}_{abcd}-\mathbf{K}_{abcd} \right ]
\\
$$

The first term is related to kinetic energy and is given by:

$$
\\
\mathbf{T}_{ab}=-\frac{1}{2}\left \langle \phi_a|\nabla^2 |\phi_b  \right \rangle
\\
$$

The second term i related to electron-nuclei interaction and is given by:

$$
\\
\mathbf{V}_{ab}= \sum_{k}^{M} \left \langle   \phi_a \left |  \ \frac{Z_k}{\left | \textbf{R}_\textup{k}-\textbf{r} \right| }  \right | \phi_b \right \rangle  
\\
$$

The final term involves a sum of two electron integral, ${J}_{abcd}$ and ${K}_{abcd}$ , that builds up the average electric field that makes up the electron-electron interactions in our approximation.

$$
\\
\mathbf{J}_{abcd}= \int \int \phi_a(\textbf{r}_1)\phi_b(\textbf{r}_1) r_{12}^{-1} \phi_c(\textbf{r}_2)\phi_d(\textbf{r}_2) d\textbf{r}_1d\textbf{r}_2
\\
\\
\mathbf{K}_{abcd}= \int \int \phi_a(\textbf{r}_1)\phi_c(\textbf{r}_1) r_{12}^{-1} \phi_b(\textbf{r}_2)\phi_d(\textbf{r}_2) d\textbf{r}_1d\textbf{r}_2
\\
$$

these integrals are condensly written: $\left ( ab|cd \right )$. If we use a suitible choice of basis-functions, all of the intergrals above have analytical solutions. This is the case for Gaussians which are a popular choice in chemistry and used in our notebook example. Physicist prefer plane-waves which are more suited for periodic systems such a metals. 

We can simply a our exression by defining a new matrix $\mathbf{K}$ called density matrix which is defined as:

$$
\\
\mathbf{P}_{ab}=\sum_{j}^{N/2}2c_{aj}c_{bj} \ \ \textup{[Factor of 2 for spin up + spin down...]}
\\
$$

$$
\\
\mathbf{F}_{ab}=\mathbf{T}_{ab}+\mathbf{V}_{ab}+ \sum_{c}^{N_{basis}}\sum_{d}^{N_{basis}}  \mathbf{P}_{cd}\left [  \mathbf{J}_{abcd}-\frac{1}{2}\mathbf{K}_{abcd} \right ]
\\
$$

There are two small complications allowing us to readily solve the linear equation system. (i) the equation is not a proper eigenvalue problem $\mathbf{A}\mathbf{x}=\lambda\mathbf{x}$, and (ii) \mathbf{F}
depend on the unknown coeffecients $\mathbf{C}$. The first of these problem can be tackled using pure mathematics (a linear transformation) and second problem can be addessed using the SCF approach, i.e. guess $\mathbf{C}$ calculate $\mathbf{C}$ find new $\mathbf{C}$ calculate new $\mathbf{F}$ repeat.  

How do we make the transformation? 

We would like to write our problem as:

$$
\\
\mathbf{F}' \mathbf{C}'=\mathbf{C}'\mathbf{E}
\\
$$

This is possible if we use:

$$
\\
\mathbf{F}'=\mathbf{S}^{-\frac{1}{2}}\mathbf{F}\mathbf{S}^{-\frac{1}{2}}
\\
$$

and

$$
\\
\mathbf{C}'=\mathbf{S}^{\frac{1}{2}}\mathbf{C}  
\\
$$

The matrix $\mathbf{S}^{-\frac{1}{2}}$ is the diagonal matrix form from the inverse square root of eigenvalus of $\mathbf{S}$ (it sound hooribly complicated but it is simple task for a computer as we will see in our jupyter notebook example.)

The final numerical procedure is as follows:

1. Guess $\mathbf{C}$
2. Calculate $\mathbf{F}$ from $\mathbf{C}$
3. Make a linear transformation of $\mathbf{F}$ using $\mathbf{S}^{-\frac{1}{2}}$
4. Solve $\mathbf{F}' \mathbf{C}'=\mathbf{C}'\mathbf{E}$
5. Transform $\mathbf{C}'$ to $\mathbf{C}$, again using $\mathbf{S}^{-\frac{1}{2}}$
6. Calculate $\mathbf{F}$
7. Repeat steps 3-6 until we reach a self consistent field, i.e when $\mathbf{C}$ does not change anymore.

Now let's build our own code!

<a target="_blank" href="https://colab.research.google.com/github/jollactic/Modelling_course/blob/main/HF/HF_skeleton.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>



<div class="warning" style='padding:0.1em; background-color:#E9D8FD; color:#69337A'>
<span>
<p style='margin-top:1em; text-align:center'>
<b>Assignment:</b></p>
<p style='margin-left:1em;'>
Complete the code in the Jupyter note-book link provided above and return a commented version of the code or make a short recorded tutorial. You are free to explore as complicated molecules as you like but you should at-least consider the hydrogen atom.

<p style='margin-left:1em;'>
Tip 1 (Basic level): Consider the H-He<sup>+</sup> molecule which is a popular toy model in the literature. 
<p style='margin-left:1em;'>
Tip 2 (Advanced level) You can also explore H-Li<sup>2+</sup> and H-Be<sup>3+</sup> and consider both how your basis-set should be modified and degree of ioniziity in the binding. It is rather simple to compute the so-called Mulliken charges (see the appendix in this chapter) of the atoms which can tell how much electron transfer their is in the system.

<p style='margin-top:1em; text-align:center'>
<b>Submission instructions:</b></p>
<p style='margin-left:1em;'>

<p style='margin-left:1em;'>
Upload your commented version of the note-book to the studium page. 

</p></span>
</div>


## Appendix: Mulliken population

 The Mulliken population analysis is a method used to partition the electron density of a molecule into individual atomic contributions. It provides a way to determine how many electrons are associated with each atom in the molecule. The Mulliken population of an atom $i$ is defined as the sum of the electron density matrix elements between the atomic orbitals centered on atom $i$:

$$
\\
M_i = \sum_{a \in i} \sum_{b} \mathbf{P}_{ab} \mathbf{S}_{ab}
\\
$$

where $\mathbf{P}_{ab}$ is the density matrix element between atomic orbitals $a$ and $b$, and $\mathbf{S}_{ab}$ is the overlap matrix element between the same orbitals, as defined above. The summation over $a$ includes all atomic orbitals centered on atom $i$, and the summation over $b$ includes all atomic orbitals in the molecule.

The Mulliken charge of an atom $i$ is defined as:

$$
\\
q_i = Z_i - M_i
\\
$$

where $Z_i$ is the number of electrons in the isolated atom $i$, and $M_i$ is the Mulliken population of atom $i$ in the molecule. The Mulliken charge $q_i$ represents the deviation of the actual electron density around atom $i$ from that of an isolated atom with the same nuclear charge $Z_i$, and can be used to determine the charge distribution in the molecular system. If $q_i$ is positive, atom $i$ has lost electrons compared to its isolated state and has a net positive charge; if $q_i$ is negative, atom $i$ has gained electrons and has a net negative charge.


### Further reading:

[Chapter 2 in *Computational Chemistry of Solid State Materials : A Guide for Materials Scientists, Chemists, Physicists and Others* ](https://ebookcentral.proquest.com/lib/uu/reader.action?docID=481650#)

[Chapter 8 in *Atomistic Computer Simulations : A Practical Guide* by Veronika Brázdová and David R. Bowler](https://ebookcentral.proquest.com/lib/uu/reader.action?docID=1161544)




What is the role of the Slater determinant in this method?

What is the self-consistent field (SCF) procedure in the context of Hartree-Fock theory? How does it work and why is it necessary?

How does the choice of basis set affect the accuracy and efficiency of Hartree-Fock calculations? What are some common types of basis sets used in quantum chemistry?
