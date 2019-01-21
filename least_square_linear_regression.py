import numpy as np
import pandas as pd
import scipy.stats.stats as sc
import matplotlib.pyplot as plt

def getCoefficientAndIntercept(x, y):
    correlation = sc.pearsonr(data['x'], data['y'])[0]
    coefficient = correlation * (np.std(data['y']) / np.std(data['x']))
    intercept = np.mean(y) - (coefficient * np.mean(x))
    return coefficient, intercept

def plotDistribution(x,y):
    plt.scatter(x,y)

data = pd.DataFrame( {'x':[4,5,6,7,8,9,10], 'y':[4,5,7,8,8.5,10,10.5]} )

# Plot the data
plotDistribution(data['x'], data['y'])

# Get coefficient, intercept
coefficient, intercept = getCoefficientAndIntercept(data['x'], data['y'])
print(coefficient, intercept)
