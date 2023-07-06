# Dataset of Square Lattice Systems

This repository contains the dataset used in "Dynamical process of a bit-width reduced Ising model with simulated annealing".

## Dataset Structure 

The data format is a Python dictionary. The dataset is divided into two types: `ising_linear` and `ising_quad`.

**ising_linear**: The keys are strings representing spins, and the values are integers representing the coefficients of the magnetic field on the spins.

example:

```
ising_linear = {
  's0': 1, 's1': 1, 's2': -1, 's3': 1, 's4': 1, 's5': 1, 's6': -1, 
  's7': 1, 's8': -1, 's9': -1, 's10': -1, 's11': 1, 's12': -1, 
  's13': 1, 's14': 1, 's15': 1, 's16': -1, 's17': 1, 's18': 1, 
  's19': 1, 's20': 1, 's21': -1, 's22': -1, 's23': 1, 's24': -1
}
```

**ising_quad**: The keys are tuples of strings representing pairs of spins that interact with each other, and the values are the coefficients of the interaction.

example:

```
ising_quad = {
  ('s0', 's1'): 1, ('s0', 's5'): -1, ('s1', 's2'): -1, ('s1', 's6'): -1, 
  ('s2', 's3'): -1, ('s2', 's7'): 1, ('s3', 's4'): -1, ('s3', 's8'): -1, 
  ...
  ('s22', 's23'): -1, ('s22', 's2'): -1, ('s23', 's24'): -1, 
  ('s23', 's3'): -1, ('s24', 's20'): -1, ('s24', 's4'): 1
}
```

**Note**: The above examples are illustrative and do not represent the complete dataset.

## Python Code to Generate Dataset

This repository also includes Python code that we used to generate this dataset. 

## Citation

If you use this dataset or the accompanying Python code in your work, please cite the following papers

```
@article{kikuchi2023dynamical,
  title={Dynamical process of a bit-width reduced Ising model with simulated annealing},
  author={Kikuchi, Shuta and Togawa, Nozomu and Tanaka, Shu},
  journal={arXiv preprint arXiv:2304.12796},
  year={2023}
}
```
