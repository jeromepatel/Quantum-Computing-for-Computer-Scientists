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
    # inputStates = [complex(-1,0), complex(-1,-1)]
    inputStates = [complex(1/np.sqrt(2),0), complex(0,1/sqrt(2))]

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
    # A[0][0] = -1
    # A[0][1] = - 1j 
    # A[1][0] =  1j
    # A[1][1] = 1
    
    A[0][0] = 1
    A[0][1] =  -1j 
    A[1][0] =  1j
    A[1][1] = 2

    #print(f'The observable matrix is \n {A} \n')
else:
    
    for i in range(numStates):
        for j in range(numStates):
            A[i][j] = complex(input(f"enter your Ovversation matrix value at {i} {j}"))
    
    
#check whether the matrix is hermitian or not 
#print(A,'\n',A.conj().T)
assert (A == A.conj().T).all()

#now its time to calculate mean of obervable on the given input state

def calculate_mean(observable,inputVector):
    '''
    We need to calcuate {AW,W}
    which is just inner product of {AW| and |W}
    where {AW| is bra of product A|W} (complex conjugate transpose)

    Parameters
    ----------
    observable : Oversvation matrix
    inputVector : Input State vector
    Returns
    -------
    Expected value of Observable at input state

    '''
    #find bra vector first 
    ObseProduct = observable.dot(inputVector).conj().T
    #now we find inner product of modified state of input vector with itself 
    ExpectedValue = ObseProduct.dot(inputVector)
    
    #print(ExpectedValue)
    return np.round(ExpectedValue,4)
    

mean = calculate_mean(A,inputStates)

#this is also refered to as mean vector, simply just product of mean with identity matrix
A_Omega =  np.identity(numStates,dtype = complex) * mean


# print("mean value of A is ",mean)

#now we calcuate demeaned version of observable A, It is essential to find this Delta_A as it will further help us 
#to calculate variance of A

def calculate_variance(A,A_mean,inputVector):
    '''
    We will calcuate variance first by finding demeaned version of A
    i.e, deltaA = A - A_mean
    then use that  to find square of deltaA,
    the expected value of square of deltaA on input state is the variance of A
    mathematically, {DelA.DelA.W|W}
    where DelA = A - {AW|W}I
    
    Parameters
    ----------
    A : Observable matrix
    A_mean : Mean of observable matrix
    inputVector : Input state vector
    Returns
    -------
    Variance of A on Input state

    '''
    
    delta_A = A - A_mean
    
    square_del_A = delta_A.dot(delta_A)
    
    #print(A,'\n',A_mean)
    # print("------------------------")
    # print(delta_A,'\n', square_del_A)
    
    variance_A  = calculate_mean(square_del_A,inputVector)
    return np.round(variance_A,4)
    
varianceOfA = calculate_variance(A,A_Omega,inputStates)

print(f' the mean & variance of Observable \n {A} \n is {mean}, {varianceOfA}')