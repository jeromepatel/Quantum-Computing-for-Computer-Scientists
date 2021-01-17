# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 19:11:17 2021

@author: jyotm
"""

#implementation of probablistic matrix operation in time scale

import numpy as np

#check for the code logic if true then it will take default values 
test = True

#testing 
if test:
    num = 3
else:
    #input number of nodes in graph
    num = int(input("enter the number of locations/vertices:\n"))


#input the initial states of marbles at each vertex( starting point/input state)
inputState = []

#testing 
if test:
    inputState = [0.2, 0.5, 0.3]
else:  
    for i in range(num):
        #now floats allowed
        numMarbles = float(input(f'enter number of marbles at {i}: \n'))
        inputState.append(numMarbles)

inputState = np.array(inputState)
print(f'input/initial state of marbles is {inputState}')


#initialize the operation array with zeros
matrixOperation = np.zeros((num,num))


#testing
if test:
    matrixOperation = np.array(
    [[0.5 ,0.5, 0.],
     [0.5, 0.3 ,0.2],
     [0., 0.2, 0.8]])
    
else: 
    #the operation only allows doubly stochastic matrix, so we input that from user
    for i in range(num):
        for j in range(num):
            value = float(input(f'enter vertex number which is connnected to {i}:'))
            if value > 1 :
                print(f"please enter valid vertex number in [0,1]")
                break
            matrixOperation[j,i] = value

#check if matrix operation is doubly stochastic
for k in range(num):
    if np.sum(matrixOperation[:,k]) != 1 or np.sum(matrixOperation[k,:]) != 1:
        raise ValueError


print('the operation matrix is: \n')
print(matrixOperation)
        
if test:
    #the oepration after one time step is
    nthTime = 1
    print(matrixOperation.dot(inputState.T))
else:
    #nth power of operation matrix
    nthTime = float(input("enter n dimention : \n"))
    matrixNthPow = np.linalg.matrix_power(matrixOperation,nthTime)
    #state after n time step
    marbleStates = matrixNthPow.dot(inputState.T)
    print(f'marble states after {nthTime} time steps is {marbleStates}')
   