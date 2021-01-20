# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:48:17 2021

@author: jyotm
"""


#programming multiple slit experiment and simulating it after n time steps 
#with complex numbers as we are simulating a quantum system

import numpy as np
from math import sqrt
test = True


if test:
    numSlits = 2
    #they are actually slit amplitudes rather than slit probabilities 
    slitAmplitudes = [1/sqrt(2),1/sqrt(2)]
else:
    #input the number of slits and their probabilities 
    numSlits = int(input("enter the number of slits: \n"))
    
    
    slitAmplitudes = []
    for i in range(numSlits):
        #input ith slit probability, all probabilities should add up to 1
        slitWeight = complex(input(f'enter the probability of slit {i}:(in complex no form)\n'))
        slitAmplitudes.append(slitWeight)

slitAmplitudes = np.array(slitAmplitudes)

#ensure its squares adds up to 1
assert(round(np.sum(np.square(slitAmplitudes)),4) == 1)
print(f'your slit probabilities are {np.square(slitAmplitudes)}')



if test:
    numTargets = 5
else:
    #input the number of targets
    numTargets = int(input("enter the number of Targets: \n"))


#define operation matrix as written in book (diagram 3.1, and graph 3.31)

#create matrix of size with number of nodes equal to slits + target + 1
matrixDimention = numSlits + numTargets + 1
matrixBullets = np.zeros((matrixDimention,matrixDimention)) * complex(0)

#my implementation is different from the question as I have considered equal probability for each target from slit uniformly whease
#in question it was asked to take prob. from the user, which was really time consuming for the user, so instead I have 
#calculatated the probability distribution directly

if test:
    x = 1/sqrt(6)
    y = 1/sqrt(2)
    experiment=[[0., 0.                 , 0.               , 0. ,  0. ,  0. ,  0. ,  0.   ],
                [y , 0.                 , 0.               , 0. ,  0. ,  0. ,  0. ,  0.  ],
                [y , 0.                 , 0.               , 0. ,  0. ,  0. ,  0. ,  0.  ],
                [0.  , x *complex(-1,1) , 0.               , 1. ,  0. ,  0. ,  0. ,  0.  ],
                [0.  , x*complex(-1,-1) , 0.               , 0. ,  1. ,  0. ,  0. ,  0.  ],
                [0.  , x*complex(1,-1)  , x*complex(-1,1)  , 0. ,  0. ,  1. ,  0. ,  0.  ],
                [0.  , 0.               , x*complex(-1,-1) , 0. ,  0. ,  0. ,  1. ,  0.  ],
                [0.  , 0.               , x*complex(1,-1)  , 0. ,  0. ,  0. ,  0. ,  1.  ]]
    matrixBullets = np.array(experiment)
    
else:
    #ask from user
    for i in range(matrixDimention):
        #for first column which corresponds to starting node or firing node
        
        #i represents slit no. and j representes target number except in last elif it doesnt matter 
        if i == 0:
            for j in range(1,numSlits + 1):
                matrixBullets[j,i] = slitAmplitudes[j-1]
        elif i >= 1 and i < numSlits + 1:
            #find no of target per slit or occurrences of target per slit 
            unit = numTargets // numSlits  
            overlap = numTargets % numSlits
            occurrence = unit + overlap
         
            #get the starting point of column vector for each slit vertex of graph
            j = numSlits + 1 + (occurrence - overlap) * (i-1) 
            cnt = 0
            #change the probability of targets which are affected by that slit
            while cnt < occurrence:
                #input the probability from the user
                matrixBullets[j,i] = complex(input(f'enter the matrix weight from slit {i} to target{j}:(in complex no form)\n'))
                cnt += 1
                j += 1
            
        elif i > numSlits:
            for j in range(matrixDimention):
                if i == j:
                    #Bullet remains at target once it hits the target for infinite time
                    matrixBullets[j,i] = 1
        else:
            print("something went wrong, check your code")


print("operation matrix is ", matrixBullets)

#input vector from the user , initial state of the marble

initialState = np.zeros((matrixDimention,)) * complex(0)
if test:
    initialState[0] = 1
else:
    #input the probability from the user
    for i in range(matrixDimention):
        initialState[i] = float(input(f"enter the probability of marble at node {i} :\n"))
    
#check if probs. equal to 1
assert(np.sum(np.square(initialState)) == 1)


test = False

if test:
    #the oepration after one time step is
    nthTime = 1
    #print(matrixBullets.dot(initialState.T))
else:
    #nth power of operation matrix
    nthTime = int(input("enter number of time steps : \n"))
    complexMatrixNthPow = np.linalg.matrix_power(matrixBullets,nthTime)
    #check for interference 
    #we will check the nth power of modulus square of initial matrix operation and compare with nth power of initial matrix operation
    #if some element is non-zero in nth power mod and zero in nth power normal matrix then
    #we can conclude that it may have been cancelled out by interference during second time 
    
    
    #first find modulus square of initial matrix (element wise mod square of complex matrix) corresponds to B in 3.2.2
    #modMatrixOperation = np.zeros((matrixDimention,matrixDimention))
    modSquareMatrixOperation = abs(matrixBullets)**2
    #we can also interpret this as probability matrix of operation

    #find mod of nth power matrix corresponds to B^n in 3.2.2
    nthPowmodSqMatrixClassical = np.linalg.matrix_power(modSquareMatrixOperation,nthTime)
    
    
    #the logic is that the modulus square of complex matrix is exactly the same as float or fractinal counter part in 
    #3.2.2 (if we assume uniform and equal probabilities of all target states from slits,with some constrains)
    #so we find nth power of mod matrix and we know that the classical matrix can't do interference 
    #we then compare it with complex or quantum matrix (nth power), if some element is zero in quantum matrix then we can safely say that 
    #it is ZERO due to intereference
    
    
    #we compare nth pow mod Square matrix(classical nth power) with mod square of nth power quantum matrix (complex matrix)
    modSquareNthpowQuantum =  np.around(abs(complexMatrixNthPow)**2,5)             #can also be interpreted as probability matrix of nth operation
    
    interferenceResults = []
    for i in range(matrixDimention):
        for j in range(matrixDimention):
            if nthPowmodSqMatrixClassical[i,j] == 0:
                continue
            elif modSquareNthpowQuantum[i,j] == 0:
                interferenceResults.append((i,j))
    
    print(f"intereference occurred at : {interferenceResults}")
    
    #state after n time step
    marbleStates = complexMatrixNthPow.dot(initialState.T)
    print(f'marble state after {nthTime} time steps is {marbleStates}')