# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 17:47:02 2021

@author: jyotm
"""


import numpy as np
from math import sqrt
import math
test = True

# this is an exercise which simulates simple quantum system 
# Imagine the system as a particle in a straight line of discrete points
# so, the possible states show its state vector and thus simulating n state quantum system
# we continue our simulation including one observable to our system


#this program is continuation of our implementation of quantum system from 4.1.1


if test:
    numStates = 2
else:
    #take input from the user, number of discrete values or total states
    numStates = int(input("enter the total number of quantum system: "))


if test:
    inputStates = [complex(-1,0), complex(-1,-1)]

else:
    inputStates = []
    for ind in range(numStates):
        inputStates = complex(input(f"enter the amplitude associated with basis state x{ind} for start state"))
    

inputStates = np.array(inputStates).T
    
print(f"input states are {inputStates}")  


        
def calculateNorm(inputVector):
    return sqrt(np.sum(np.square(list(map(abs,inputVector)))))


normOfComplexAmplitudes = calculateNorm(inputStates)

#input hermitian matrix and check whether its hermitian 
#we can check from the fact that for a hermitian matrix ==> A = A^H(conjugate A)

#create matrix of appropriate size
A = np.zeros((numStates,numStates),dtype = complex)


if test:
    A[0][0] = -1
    A[0][1] = - 1j 
    A[1][0] =  1j
    A[1][1] = 1

    print(A)