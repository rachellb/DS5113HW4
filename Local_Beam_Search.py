
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
 

searches = 3

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

x_curr = []         # A list that stores the current solutions of each neighborhood
x_best = []         # This will store the best solution of each neighborhood
f_curr = []         # This stores the current evaluation of the current solution
f_best = []         # Stores the best values of each neighborhood


for i in range(0,searches):
    x_curr.append(initial_solution())         # this makes k current solutions
    x_best.append(x_curr[i][:])               # This will hold the best in this neighborhood
    f_curr.append(evaluate(x_best[i]))           # This will hold the evaluation of the current solution of this neighborhood
    f_best.append(f_curr[i][:])               # This will hold the best of this neighborhood
    
x_bestB = initial_solution()        # This will store the best of the best of the neighborhoods
f_bestB = evaluate(x_bestB)[:]      # This stores the weight and value of the best of the best solution

for i in range(0,len(x_curr)-1):
    if evaluate(x_curr[i])[0] > f_bestB[0]:
        x_bestB = x_curr[i][:]              # This is best solution in all neighborhoods
        f_bestB = evaluate(x_curr[i])[:]    # Stores the value for this best of best solution
        
# By the end of this we have an array of k solutions that will make the neighborhoods


#begin local search overall logic ----------------

done = 0


while done == 0:
            
    for i in range(0,len(x_curr)-1):
        
        Neighborhood = neighborhood(x_curr[i])   #create a list of all neighbors in the neighborhood of x_curr
    
        for s in Neighborhood:                #evaluate every member in the neighborhood of x_curr
            solutionsChecked = solutionsChecked + 1
            if evaluate(s)[0] > f_best[i][0]:   
                x_best[i] = s[:]                 #find the best member and keep track of that solution
                f_best[i] = evaluate(s)[:]       #and store its evaluation 
    
    for i in range(0,len(x_best)-1):                          # this finds the best of the best of the neighborhoods
        if evaluate(x_best[i])[0] > f_bestB[0]:
            x_bestB = x_best[i][:]
            f_bestB = evaluate(x_best[i])[:]
        
    for i in range(0,len(f_curr)-1): 
        if f_bestB == f_curr[i]:                  #if there were no improving solutions in the neighborhood
            done = 1
            
    else:
        for i in range(0,len(x_curr)-1):
            x_curr[i] = x_best[i][:]        #else: move to the neighbor solution and continue
            f_curr[i] = f_best[i][:]         #evalute the current solution
        
        print ("\nTotal number of solutions checked: ", solutionsChecked)
        print ("Best value found so far: ", f_bestB)        
    
print ("\nFinal number of solutions checked: ", solutionsChecked)
print ("Best value found: ", f_bestB[0])
print ("Weight is: ", f_bestB[1])
print ("Total number of items selected: ", np.sum(x_bestB))
print ("Best solution: ", x_bestB)
