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
        inputStates = complex(input(f"enter the amplitude associated with basis state x{ind} for start state"))
    
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

def calculateNorm(inputVector):
    return sqrt(np.sum(np.square(list(map(abs,inputVector)))))


normOfComplexAmplitudes = calculateNorm(inputStates)

print(f'the norm of particle states is {normOfComplexAmplitudes}')

probOfStatek = np.square(abs(inputStates[findProbatState])) / np.square(normOfComplexAmplitudes)

print(f'Probability of particle at state {findProbatState} is {probOfStatek}')

#instead of dividing we could have normalized the whole input state otherwise like this

normlizedInputstates = np.array(inputStates)/normOfComplexAmplitudes

#second part is getting transition state from one state(or system) to another quantum state(or system)

#take input from user whether to calculate transition state and its probability or not 

if test:
    value = 'yes'

else:
    value = input("Do you want to calculate transition amplitudes, enter yes or no :\n")

if value[0].lower() == 'y':
    getTransitionAmplitudes = True
elif value[0].lower() == 'n':
    getTransitionAmplitudes = False
else:
    print("please enter valid choice : run code next time ")
        
    
if getTransitionAmplitudes:
    
    
    #input second ket notation or state
    
    if test:
        endStates = [complex(-4,1), complex(1,2), complex(4,-1),complex(-2,1)]
        
    else: 
        endStates = []
        for ind in range(numStates):
            endStates = complex(input(f"enter the amplitude associated with basis state x{ind} for End state: "))
            
    #print(endStates)
    #the transition is carried out between inputstates and endstates
    #to calculate the transition we need two things, bra vector and ket vector and then
    #we can take inner product of both to get, bra-ket or bra(c)ket value
    
    #bra vector can be calculated as complex conjugate of second state or end state
    conjEndStates = np.conjugate(endStates)
    
    #calculate normalized end state, we achieve this by dividing the norm of end states
    normEndstates = calculateNorm(conjEndStates)
    normConjEndStates = conjEndStates / normEndstates
    
    #print(normConjEndStates)
    
    #calculate inner product 
    innerProduct = normConjEndStates.dot(normlizedInputstates.T)
    print(f'the inner product or transition value is : {innerProduct}')
    
    #the probability is just the square of product as defined below
    probEndState = np.square(abs(innerProduct))
    print(f'the probability of transitioning into end state after measurement has been made is {probEndState}')
    
    #to find probability of basis state bi after measurement has been made, we need {bi|W}
    #which is ----> bi = {bi|W}, or P(bi) = |bi|^2 so, square of innerproduct gives that probability of ending up in that state
    
    #for eg. we need prob at occuring b1 after measurement 
    
    basisState = np.zeros((numStates,)) * complex(0)
    basisState[1] = complex(1,0)
    
    #calculate inner product, no need to cal norm as, norm of basis states are always 1
    innerProdBasis = basisState.dot(normlizedInputstates.T)
    
    #print(normlizedInputstates, innerProdBasis)
    
    probBasis = np.square(abs(innerProdBasis))
    print(f'the prob of ending up at b1 state is {probBasis}')
    