# Super Conductor Simulation
This is a visual representation of the quantum phase states of the cooper bair bonding present within a typeI super conductor.
I learned all the physics present within this simulation while there. 
This particular simulation uses the XY monte carlo random sampling method to get a running time that is reasonable on a modern pc. Running a perfet simulation of a type I superconductor without this statistical approximation would require the computing strength of a super computer. For this reason the monte carlo random sampling algorith is a very  powerfull tool as it allows semi accurate approximations that can help develop an intuition for what is occuring physicaly.
This would not have been possible to make without the incredible mentorship given to me at the ISSYP summer camp. 

### Runnning Instructions:
1. Ensure that python3 is installed
2. Ensure that matplotlib is installed
3. make sure that numpy is installed
4. run the python file with python3

<iframe src="https://giphy.com/embed/2ifUHBli1b1HpRr3Ii" width="478" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

## What is Super Conductivity?
Superconductivity is a state that certain materials can take where they 
have zero electrical resistance. This has some weird side effects, the 
most prominent being that superconductors repel magnetic fields.
These superconducting states are normally achieved at super low 
temperatures.
The holy grail of superconductivity would be a room-temperature 
superconductor. This would have applications in almost all aspects of 
day to day life.

## How are Super Conductors described?
Type I super conductors are described using the BCS thoery model, first 
proposed in 1957. It won the Nobel prize in physics in 1972. In BCS 
theory, the material is modeled as a lattice of positive ions with a sea 
of free electrons. As an electron moves though this lattice, it attracts 
the positive ions towards it. This region of higher positive charge can 
have a delayed atractive effect on another electron. Thus, these two 
electrons can have an indirect "attraction". This pairing is called a 
cooper pair; a quasi particle. Because pairs are continually 
interchanged, the energy required to break any one cooper pair is the 
energy required to brea all of the pairs. Electrons on their own are 
fermions, and obey the pauli exclusion principle. As such, electrons 
cannot normally share quantum states. A cooper pair on the other hand, 
is a boson, and can form a bose einstein condensate. This state of 
matter allows for the sharing of quantum states, and in this case 
facilitates the co-existence of all of the cooper pairs in the lowest 
quantum energy state.

![Alt text](img/bcs.png "Cooper Pair Formation")

## 