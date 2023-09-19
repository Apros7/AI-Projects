## Biology inspired reinforcement learning

The following must be specified upon initalization:
- DNA string length: number of bits in DNA string (throught to be proportional to initial complexity of models). Minimum is 100.
- Mutation risk: default is 1e-3

This is a project under development.

It currently creates the neural network and can mutate, but is does not train on anything and has no capability to improve through generations.

### Thoughts
I wanted to take the ability from biology, where 2 different functions are present:
- You get half the genome from each parent, making you get a unique combination, which could be even better
- Mutations allow for random changes in DNA to potentially create unique, random modifications

The DNA has the ability to change everything about the body. I thought this should also be implemented in code, so that the cell through mutation would be able to change things that the developer did not expect: this could be extremely interesting to watch unfold in an environment.

**Basic test scenario**
I wanted to basically just make a cell be able to navigate through a 2D space to find a reward at the end (see "motion planning simulations")

### 