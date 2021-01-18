# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 21:53:21 2021

@author: jyotm
"""

#programming multiple slit experiment and simulating it after n time steps 

import numpy as np
test = False


if test:
    numSlits = 2
    slitProbabilities = [0.5,0.5]
else:
    #input the number of slits and their probabilities 
    numSlits = int(input("enter the number of slits: \n"))
    
    
    slitProbabilities = []
    for i in range(numSlits):
        #input ith slit probability, all probabilities should add up to 1
        slitProbability = float(input(f'enter the probability of slit {i}:\n'))
        slitProbabilities.append(slitProbability)

slitProbabilities = np.array(slitProbabilities)

#ensure it adds up to 1
assert(np.sum(slitProbabilities) == 1)
print(f'your slit probabilities are {slitProbabilities}')



if test:
    numTargets = 5
else:
    #input the number of targets
    numTargets = int(input("enter the number of Targets: \n"))


#define operation matrix as written in book (diagram 3.1, and graph 3.31)

#create matrix of size with number of nodes equal to slits + target + 1
matrixDimention = numSlits + numTargets + 1
matrixBullets = np.zeros((matrixDimention,matrixDimention))

#my implementation is different from the question as I have considered equal probability for each target from slit uniformly whease
#in question it was asked to take prob. from the user, which was really time consuming for the user, so instead I have 
#calculatated the probability distribution directly
for i in range(matrixDimention):
    #for first column which corresponds to starting node or firing node
    if i == 0:
        for j in range(1,numSlits + 1):
            matrixBullets[j,i] = slitProbabilities[j-1]
    elif i >= 1 and i < numSlits + 1:
        #find no of target per slit or occurrences of target per slit 
        unit = numTargets // numSlits  
        overlap = numTargets % numSlits
        occurrence = unit + overlap
        #failed attempt but still for ref.
        # print(unit,overlap, unit * i, 'occurences is : ' , occurrence)
        # print(numSlits+ 1 + unit * (i-1) - overlap, unit * i + overlap , unit * (i + 1) + overlap*2)
        # #for j in range(numSlits + 1+ unit * (i-1) - overlap  , unit * (i + 1) + overlap*2):
        #     #matrixBullets[j,i] = 0.33
        
        
        #get the starting point of column vector for each slit vertex of graph
        j = numSlits + 1 + (occurrence - overlap) * (i-1) 
        cnt = 0
        #change the probability of targets which are affected by that slit
        while cnt < occurrence:
            #set the probability equally for all target nodes from that slit 
            matrixBullets[j,i] = round(1/occurrence,2)
            cnt += 1
            j += 1
        
    elif i > numSlits:
        for j in range(matrixDimention):
            if i == j:
                #Bullet remains at target once it hits the target for infinite time
                matrixBullets[j,i] = 1
    else:
        print("something went wrong, check your code")


print(matrixBullets)

#input vector from the user , initial state of the marble

initialState = np.zeros((matrixDimention,))
if test:
    initialState[0] = 1
else:
    #input the probability from the user
    for i in range(matrixDimention):
        initialState[i] = float(input(f"enter the probability of marble at node {i} :\n"))
    
#check if probs. equal to 1
assert(np.sum(initialState) == 1)


if test:
    #the oepration after one time step is
    nthTime = 2
    print(matrixBullets.dot(initialState.T))
else:
    #nth power of operation matrix
    nthTime = int(input("enter number of time steps : \n"))
    matrixNthPow = np.linalg.matrix_power(matrixBullets,nthTime)
    #state after n time step
    marbleStates = matrixNthPow.dot(initialState.T)
    print(f'marble state after {nthTime} time steps is {marbleStates}')
