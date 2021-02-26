# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:51:03 2021

@author: jyotm
"""


import numpy as np
from math import sqrt
import math

import warnings
warnings.filterwarnings("ignore")
test = True


#this is a continuation of programming drill exercises and quantum simulator of 4.2.1
#we are going to implement the list of eigen values of observable,
# the probability that state will transition to each one of the eigenstate



if test:
    numStates = 2
else:
    #take input from the user, number of discrete values or total states
    numStates = int(input("enter the total number of quantum system: "))


if test:
    # inputStates = [complex(-1,0), complex(-1,-1)]
    inputStates = [complex(1/np.sqrt(2),0), complex(0,1/sqrt(2))]

else:
    inputStates = []
    for ind in range(numStates):
        inputStates = complex(input(f"enter the amplitude associated with basis state x{ind} for start state"))
    

inputStates = np.array(inputStates).T
    
print(f"input states are {inputStates}")  


#input observable

#create matrix of appropriate size
A = np.zeros((numStates,numStates),dtype = complex)


if test:
    # A[0][0] = -1
    # A[0][1] = - 1j 
    # A[1][0] =  1j
    # A[1][1] = 1
    
    A[0][0] = 1
    A[0][1] =  -1j 
    A[1][0] =  1j
    A[1][1] = 2

    print(f'The observable matrix is \n {A} \n')
else:
    
    for i in range(numStates):
        for j in range(numStates):
            A[i][j] = complex(input(f"enter your Ovversation matrix value at {i} {j}"))
    
    
#check whether the matrix is hermitian or not 
#print(A,'\n',A.conj().T)
assert (A == A.conj().T).all()


#get the eigenvalues of corresponding observable
eigenstates = np.linalg.eigh(A)
eigenValues = eigenstates[0]
eigenVectors = eigenstates[1]
print(f"the eigenvalues of the observable is {eigenValues}")


#now we will find out the probability of collapsing input state into each eigenvectors,

probabilities = np.zeros((numStates))

for i in range(numStates):
    #probability of input state collapsing into eigen vector is the square of dot product of both (projection of input state in eigne vector)
    eigenVector = np.array(eigenVectors[:,i],dtype = complex)
    probabilities[i] = np.square(np.dot(inputStates,eigenVector))
print(f"the probability for each eigenvector measuring is: {probabilities}")