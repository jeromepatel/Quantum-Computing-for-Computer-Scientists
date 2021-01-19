# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:33:04 2021

@author: jyotm
"""
import numpy as np
from math import sqrt

#continuation of 3.2.1 with some updates

#quantum probabilistic system (time scaled matrix operation)
#for forward in time from t --------> t + 1 we use U.X = Y
#for backward in time t + 1 --------> t, we use U`(dagger).Y = X


#some exp
#a = complex(input("enter your complex no here: "))
#enter a + bj as complex number
# print(a *( 5 + 7j))
# print('mag = ', abs(a))
# print('angle = ', np.angle(a, deg=True))


#implementation of quantum matrix operation in time scale


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
    inputState = [1.0, 0.0 ,0.0]
else:  
    for i in range(num):
        #now floats allowed
        numMarbles = complex(input(f'enter number of marbles at {i}(in complex no form): \n'))
        inputState.append(numMarbles)

inputState = np.array(inputState)
print(f'input/initial state of marbles is {inputState}')

#to check if only 1 marble state is entered, comment this line if you need to enter more than 1 marble
assert(np.sum(np.square(inputState)) == 1)
#initialize the operation array with zeros


matrixOperation = np.zeros((num,num)) * complex(0)


#testing
if test:
    x = 1/sqrt(2)
    #print(x)
    matrixOperation = np.array(
    [[x ,x, 0.],
      [x, x ,0],
      [0., 0., 1]])
 #    matrixOperation = np.array([[0.707106+0.j, 0.707106+0.j ,0.      +0.j],
     # [0.707106+0.j, 0.707106      +0.j, 0.      +0.j],
     #[0.      +0.j, 0.      +0.j, 1.      +0.j]])
    
    
else: 
    #the operation matrix doesnt need to be doubly stochastic matrix(but its square needs to be), so we input that from user
    for i in range(num):
        for j in range(num):
            value = complex(input(f'enter vertex probability of path from {i} to {j}(in complex no form):'))
            #no need to check for value as its complex,
            matrixOperation[j,i] = value

print(matrixOperation)
#check whether matrix operation square is doubly stochastic
for k in range(num):
    #print(round(np.sum(np.square(matrixOperation[:,k])), 3), "asaagsggg")
    if round(np.sum(np.square(matrixOperation[:,k])), 3) != complex(1) or round(np.sum(np.square(matrixOperation[k,:])),3) != complex(1):
        print("Please check your operation matrix again, make sure its row and column add up to 1")
        raise ValueError


print('the operation matrix is: \n')
print(matrixOperation)
        
if test:
    #the oepration after one time step is
    nthTime = 1
    marbleStates = matrixOperation.dot(inputState.T)
    print(f'marble state after {nthTime} time steps is {marbleStates}')
else:
    #nth power of operation matrix
    nthTime = int(input("enter number of time steps : \n"))
    matrixNthPow = np.linalg.matrix_power(matrixOperation,nthTime)
    #state after n time step
    marbleStates = matrixNthPow.dot(inputState.T)
    print(f'marble state after {nthTime} time steps is {marbleStates}')