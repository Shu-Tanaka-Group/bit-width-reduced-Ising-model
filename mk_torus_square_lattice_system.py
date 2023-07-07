import random
import numpy as np

#Generate a torus ferromagnetic square L x L lattice system
def mk_torus_ferromagnetic(L):
    ising_quad = {}
    ising_linear = {}
    k = 0
    
    for i in range(L ** 2):
        if i == L ** 2 - 1:
            ising_quad["s{0}".format(k), "s{0}".format(k - (L - 1))] = 7
            ising_quad["s{0}".format(k), "s{0}".format(k - L * (L - 1))] = 7
        elif i % L == L - 1:
            ising_quad["s{0}".format(k), "s{0}".format(k - (L - 1))] = 7
            ising_quad["s{0}".format(k), "s{0}".format(k + L)] = 7
        elif i >= L * (L - 1):
            ising_quad["s{0}".format(k), "s{0}".format(k + 1)] = 7
            ising_quad["s{0}".format(k), "s{0}".format(k - L * (L - 1))] = 7
        else:
            ising_quad["s{0}".format(k), "s{0}".format(k + 1)] = 7
            ising_quad["s{0}".format(k), "s{0}".format(k + L)] = 7
        k += 1

        ising_linear['s{0}'.format(i)] = 7  
        
    return ising_quad, ising_linear

#Generate a torus random square L x L lattice system
def mk_torus_random(L):
    ising_quad = {}
    ising_linear = {}
    k = 0
    
    for i in range(L ** 2):
        #The coefficients of the interactions take integer values from [-7, 7], although 0 was excluded.
        while True:
            J1 = random.randint(-7, 7)
            J2 = random.randint(-7, 7) 
            #
            if J1 != 0 and J2 !=0:
                break
        if i == L ** 2 - 1:
            ising_quad["s{0}".format(k), "s{0}".format(k - (L - 1))] = J1
            ising_quad["s{0}".format(k), "s{0}".format(k - L * (L - 1))] = J2
        elif i % L == L - 1:
            ising_quad["s{0}".format(k), "s{0}".format(k - (L - 1))] = J1
            ising_quad["s{0}".format(k), "s{0}".format(k + L)] = J2
        elif i >= L * (L - 1):
            ising_quad["s{0}".format(k), "s{0}".format(k + 1)] = J1
            ising_quad["s{0}".format(k), "s{0}".format(k - L * (L - 1))] = J2
        else:
            ising_quad["s{0}".format(k), "s{0}".format(k + 1)] = J1
            ising_quad["s{0}".format(k), "s{0}".format(k + L)] = J2
        k += 1
        
        #The coefficients of the magnetic fields take integer values from [-7, 7]
        h = random.randint(-7, 7)
        ising_linear['s{0}'.format(i)] = h           
    
    return ising_quad, ising_linear

