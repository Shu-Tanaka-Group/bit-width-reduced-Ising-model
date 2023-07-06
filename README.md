# Dataset of square lattice systems

This repository contains the dataset used in "Dynamical process of a bit-width reduced Ising model with simulated annealing".

## Dataset Structure 

The data format is a Python dictionary. The dataset is divided into two types: `ising_linear` and `ising_quad`.

**ising_linear**: The keys are strings representing spins, and the values are integers representing the coefficients of the local magnetic field.

**ising_linear** data example:

```
ising_linear = {
  's0': 1, 's1': 1, 's2': -1, 's3': 1, 's4': 1, 's5': 1, 's6': -1, 
  's7': 1, 's8': -1, 's9': -1, 's10': -1, 's11': 1, 's12': -1, 
  's13': 1, 's14': 1, 's15': 1, 's16': -1, 's17': 1, 's18': 1, 
  's19': 1, 's20': 1, 's21': -1, 's22': -1, 's23': 1, 's24': -1
}
```

**ising_quad**: The keys are tuples of strings representing pairs of spins that interact with each other, and the values are the coefficients of the interaction.
