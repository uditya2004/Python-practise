"""
 - Linear regression builds a model which establishes a relationship between features and targets
     - In the example above, the feature was house size and the target was house price
     - for simple linear regression, the model has two parameters $w$ and $b$ whose values are 'fit' using *training data*.
     - once a model's parameters have been determined, the model can be used to make predictions on novel data.
"""

from matplotlib import pyplot as plt
import numpy as np

#Training Data
x_train = np.array([1.0 , 2.0])          #Provided Inputs
y_train = np.array([300 , 500])          #Expected Outputs

plt.scatter(x_train, y_train, marker= "x", color="red")        #Plotting the give data
# plt.show()

#--------------------------------------

#Developing the function
def model_function(x, w, b):
    m = x.shape[0]
    funct = np.zeros(m)

    for i in range(m):
        funct[i] = w*x[i] + b
    
    return funct


# Try experimenting with different values of w and b. What should the values be, for a line that fits our data?
y_axis = model_function(x_train, 200, 100)         #We notice that for w = 200 and b = 100 , function fits our data.

plt.plot(x_train, y_axis, color = "blue")
plt.show()

#------------------------------------------

#final function
x= 1.2
fnctn = 200 *x + 100
print(fnctn)