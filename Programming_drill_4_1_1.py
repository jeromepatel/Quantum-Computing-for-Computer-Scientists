# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 21:00:24 2021

@author: jyotm
"""

import numpy as np
from math import sqrt
import math
test = True

# this is an exercise which simulates simple quantum system 
# Imagine the system as a particle in a straight line of discrete points
# so, the possible states show its state vector and thus simulating n state quantum system

if test:
    numStates = 4
else:
    #take input from the user, number of discrete values or total states
    numStates = int(input("enter the total number of quantum system: "))

#assign its ket notation or state vector, I am  taking this as an input from user, as it is difficult to enter square root and complex numbers,
#I will simply initiate matrix as of now

if test:
    inputStates = [complex(-3,-1), complex(0,-2), complex(0,1),complex(2,0)]

#the complex amplitudes show a column vector which is n-dimentional 
#each of its entry represents a complex amplitude associated with corresponding basis vector

#for eg. |W} = C0|x0} + C1|x1} + C2|x2} 
#here |x0} = [1 0 0].T 

else:
    inputStates = []
    for ind in range(numStates):
        inputStates = complex(input(f"enter the amplitude associated with basis state x{ind}"))
    
print(f"input states are {inputStates}")  
#get position for which we want to calculate probility of occuring a particle after measurement     
if test:
    findProbatState = 2
else:
    findProbLoc = int(input("enter position or state to calculate probability of particle being there(obvio after measurement): \n"))
    if findProbatState >= numStates or findProbatState < 0:
        print("please enter values between 0 to n, coz its just index and states locations")
        raise ValueError
#so x0, x1 and x2 are 3 states at which a particle can be found and the probability of finding it at x0 can be calculated as
# p(x0) = |c0|^2/(|c0|^2 + |c1|^2 + |c2|^2) 
#we are dividing the sum to normalize the vector 
#so, ||W}| =sum of magnitude squares of all complex amplitudes (|c0|^2 + |c1|^2 + |c2|^2 )


normOfComplexAmplitudes = sqrt(np.sum(np.square(list(map(abs,inputStates)))))

print(f'the norm of particle states is {normOfComplexAmplitudes}')

probOfStatek = np.square(abs(inputStates[findProbatState])) / np.square(normOfComplexAmplitudes)

print(f'Probability of particle at state {findProbatState} is {probOfStatek}')



#second part is getting transition state from one state(or system) to another quantum state(or system)

