import numpy as np

def computeCost(X, y, theta):
    """
       computes the cost of using theta as the parameter for linear 
       regression to fit the data points in X and y
    """
    m = y.size
    J = 0
    for xi, yi in zip(X,y):
    	h = theta[0]+theta[1]*xi[1]
    	J += (h - yi)**2
    J = J*(1/(2*m))

# ====================== YOUR CODE HERE ======================
# Instructions: Compute the cost of a particular choice of theta
#               You should set J to the cost.


# =========================================================================

    return J


