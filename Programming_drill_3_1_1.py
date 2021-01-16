# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 17:55:06 2021

@author: jyotm
"""

import numpy as np

#check for the code logic if true then it will take default values 
test = False

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
    inputState = [2, 1, 3]
else:  
    for i in range(num):
        numMarbles = int(input(f'enter number of marbles at {i}: \n'))
        inputState.append(numMarbles)

inputState = np.array(inputState)
print(f'input/initial state of marbles is {inputState}')


#initialize the operation array with zeros
matrixOperation = np.zeros((num,num))


#testing
if test:
    matrixOperation = np.array(
    [[0. ,0., 0.],
     [0., 0. ,1.],
     [1., 1., 0.]])
    
else: 
    #the operation only allows one outgoing edge from a vertex, we can use this to iterate columnwise
    i = 0
    while i < num:
        #for eg. if 0 -----------> 3 -------> 2 ----------> 3, 1 -----------> 0 then enter 3 for 0th vertex
        j = int(input(f'enter vertex number which is connnected to {i}:'))
        if j >= num:
            print(f"please enter valid vertex number in range 0 to {num}")
            continue
        matrixOperation[j,i] = 1
        i += 1



print('the operation matrix is: \n')
print(matrixOperation)
        
if test:
    #the oepration after one time step is
    print(matrixOperation.dot(inputState.T))
else:
    #nth power of operation matrix
    nthTime = int(input("enter n dimention : \n"))
    matrixNthPow = np.linalg.matrix_power(matrixOperation,nthTime)
    #state after n time step
    marbleStates = matrixNthPow.dot(inputState.T)
    

print(f'marble states after {nthTime} time steps is {marbleStates}')
   