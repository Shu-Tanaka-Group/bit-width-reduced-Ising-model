# Dataset of Square Lattice Systems

This repository contains the dataset used in "Dynamical process of a bit-width reduced Ising model with simulated annealing".

## Dataset Structure 

The data format is a Python dictionary. The dataset is divided into two types: `ising_linear` and `ising_quad`.

**ising_linear**: The keys are strings representing spins, and the values are integers representing the coefficients of the magnetic field on the spins.

example:

```
ising_linear = {
   's0': 7, 's1': 3, 's2': -1, 's3': 6, 's4': -7, 's5': 3, 's6': -3,
   's7': 0, 's8': -1, 's9': 3, 's10': -7, 's11': 7, 's12': -7,
   's13': -7, 's14': 0, 's15': 6, 's16': 7, 's17': -2, 's18': 6,
   's19': 6, 's20': 6, 's21': 3, 's22': 2, 's23': 5, 's24': 1
}
```

**ising_quad**: The keys are tuples of strings representing pairs of spins that interact with each other, and the values are the coefficients of the interaction.

example:

```
ising_quad = {
  ('s0', 's1'): 3, ('s0', 's5'): 4, ('s1', 's2'): 3, ('s1', 's6'): -2, 
  ('s2', 's3'): -5, ('s2', 's7'): 3, ('s3', 's4'): -7, ('s3', 's8'): -3, 
  ...
  ('s22', 's23'): -4, ('s22', 's2'): -2, ('s23', 's24'): 7, 
  ('s23', 's3'): 6, ('s24', 's20'): 1, ('s24', 's4'): -1
}
```

**Note**: The above examples are illustrative and do not represent the complete dataset.

## Python Code to Generate Dataset

This repository also includes Python code that we used to generate this dataset. 

## License

This dataset is released under the MIT License. 

## Citation

If you use this dataset or the accompanying Python code in your work, please cite the following papers ([S. Kikuchi, N. Togawa, and S. Tanaka, 2023](https://arxiv.org/abs/2304.12796))

```
@article{kikuchi2023dynamical,
  title={Dynamical process of a bit-width reduced Ising model with simulated annealing},
  author={Kikuchi, Shuta and Togawa, Nozomu and Tanaka, Shu},
  journal={arXiv preprint arXiv:2304.12796},
  year={2023}
}
```
