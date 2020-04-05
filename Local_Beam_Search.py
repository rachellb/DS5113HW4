# -*- coding: utf-8 -*-

#basic hill climbing search provided as base code for the DSA/ISE 5113 course
#author: Charles Nicholson

#NOTE: YOU MAY CHANGE ALMOST ANYTHING YOU LIKE IN THIS CODE.  
#However, I would like all students to have the same problem instance, therefore please do not change anything relating to:
#   random number generation
#   number of items (should be 150)
#   random problem instance
#   weight limit of the knapsack

#------------------------------------------------------------------------------

#Student name: Rachel Bennett
#Date: April 5, 2020


#need some python libraries
import copy
from random import Random   #need this for the random number generation -- do not change
import numpy as np


#to setup a random number generator, we will specify a "seed" value
#need this for the random number generation -- do not change
seed = 5113
myPRNG = Random(seed)

#to get a random number between 0 and 1, use this:             myPRNG.random()
#to get a random number between lwrBnd and upprBnd, use this:  myPRNG.uniform(lwrBnd,upprBnd)
#to get a random integer between lwrBnd and upprBnd, use this: myPRNG.randint(lwrBnd,upprBnd)

#number of elements in a solution
n = 150

#create an "instance" for the knapsack problem
value = []
for i in range(0,n):
    value.append(round(myPRNG.triangular(5,1000,200),1))
    
weights = []
for i in range(0,n):
    weights.append(round(myPRNG.triangular(10,200,60),1))
    
#define max weight for the knapsack
maxWeight = 1500

#change anything you like below this line ------------------------------------

#monitor the number of solutions evaluated
solutionsChecked = 0
penalty = max(weights)                # To penalize the solutions with total weight over the max weight 
 

searches = 3    # Number of parellel searches that will occur

#function to evaluate a solution x
def evaluate(x):
          
    a=np.array(x)
    b=np.array(value)
    c=np.array(weights)
    
    totalValue = np.dot(a,b)     #compute the value of the knapsack selection
    totalWeight = np.dot(a,c)    #compute the weight value of the knapsack selection
    
    if totalWeight > maxWeight:
        totalValue = totalValue - (penalty*totalWeight-maxWeight) 

    return [totalValue, totalWeight]   #returns a list of both total value and total weight
          
       
#here is a simple function to create a neighborhood
#1-flip neighborhood of solution x         

def neighborhood(x):
        
    nbrhood = []     
    
    for i in range(0,n):
        nbrhood.append(x[:])
        if nbrhood[i][i] == 1:
            nbrhood[i][i] = 0
        else:
            nbrhood[i][i] = 1
      
    return nbrhood
          


#create the initial solution
def initial_solution():
    x = []   #i recommend creating the solution as a list
    
    #need logic here!
    for i in range(0,n):
        x.append(myPRNG.randint(0,1))           # Fills the bag randomly
        #x.append(1)                            # Completely fills bag
        
        
        
    return x




#varaible to record the number of solutions evaluated
solutionsChecked = 0


BestsDict = {}  # A Dictionary to store solutions and it's corresponding value/weight

for i in range(0,searches):         # This will store a number of initial solutions 
    x_curr = initial_solution() # equal to number of neighborhoods to seach in parallel
    f_curr = evaluate(i)[:]
    BestsDict.update( {x_curr : f_curr} ) # Stores solution and it's value/weight
              
x_best = initial_solution()     # Generates an initial best solution
f_best = evaluate(x_best)       # Evaluates that initial best solution
    
for key in BestsDict:       # This loop just finds the best of these neighborhoods
    if BestsDict[key][0] > f_best[0]:  # Should check if the best value in the dictionary is better than the current best
        x_bestB = key
        f_bestB = BestsDict[key][:]


#begin local search overall logic ----------------
done = 0
    
while done == 0:
     
    for key in BestsDict:                  # This should make k neighborhoods and run through them all
        Neighborhood = neighborhood(key)   # create a list of all neighbors in the neighborhood of key
    
        for s in Neighborhood:                #evaluate every member in the neighborhood of x_curr
            solutionsChecked = solutionsChecked + 1
            if evaluate(s)[0] > f_best[0]:  
                newkey = s
                f_best = evaluate(key)[:]
                
        if f_best == 
        del BestsDict[key]                  # I think this removes the current key value pair
        BestsDict.update({newkey: f_best})  # Adds the best key value pair from the neighborhood search
       
    for key in BestsDict:       # This loop just finds the best of these neighborhoods
        if BestsDict[key][0] > f_best[0]:  # Should check if the best value in the dictionary is better than the current best
            x_curr = key
            f_best = BestsDict[key][:]    
        
    if f_best == f_bestB:               #if there were no improving solutions in the neighborhood
        done = 1
    else:
        
        x_curr = x_best[:]         #else: move to the neighbor solution and continue
        f_curr = f_best[:]         #evalute the current solution
        
        print ("\nTotal number of solutions checked: ", solutionsChecked)
        print ("Best value found so far: ", f_best)        
    
print ("\nFinal number of solutions checked: ", solutionsChecked)
print ("Best value found: ", f_best[0])
print ("Weight is: ", f_best[1])
print ("Total number of items selected: ", np.sum(x_best))
print ("Best solution: ", x_best)
