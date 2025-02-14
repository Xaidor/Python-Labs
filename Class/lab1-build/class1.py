# Create a new class with the following changes
# 1. Weights should be a random numbers matrix of size layers X units
# 2. Change training method to multiply input X and add input Y
import numpy as np

class randmodel(object):

     def __init__ (self, numlayers, numunits, name):
        self.layers  = numlayers
        self.units   = numunits
        self.name    = name
        self.weights = np.random.randn(self.layers, self.units)

     def UnitsInModel(self):
        totalUnits = self.layers * self.units
        print(f"There are {totalUnits} units in the model.")
  
     def trainModel(self,x,y):
        self.weights = self.weights * x + y
        return self.weights
    
     def __str__(self):
       return f"This is a {self.name} architecture."
    
model1 = randmodel(3,4,"Kay")
model1.trainModel(n)
model1.__str__()
