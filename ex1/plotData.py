import matplotlib.pyplot as plt
import numpy as np

def plotData(data):
    """
    plots the data points and gives the figure axes labels of
    population and profit.
    """

# ====================== YOUR CODE HERE ======================
# Instructions: Plot the training data into a figure using the
#               "figure" and "plot" commands. Set the axes labels using
#               the "xlabel" and "ylabel" commands. Assume the
#               population and revenue data have been passed in
#               as the x and y arguments of this function.
#
# Hint: You can use the 'rx' option with plot to have the markers
#       appear as red crosses. Furthermore, you can make the
#       markers larger by using plot(..., 'rx', 'MarkerSize', 10);
    # x, y = np.loadtxt('ex1data1.txt', delimiter=',', unpack=True)
    x = data[:, 0]
    y = data[:, 1]
    plt.scatter(x,y)
    plt.xlabel('Profit in $10,000s')
    plt.ylabel('Population of city in 10,000s')
    plt.show()
    plt.figure()  # open a new figure window
    
# ============================================================
