
"""
@author Aadit Meenege
@date 9/7/20
"""

# clustering dataset
# determine k using elbow method
import pandas as pd
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt


#Read in data 
# Please input your source file or change the path while running the code.
data = pd.read_csv('C:\\Users\\Aadit\\Downloads\\Assignment.csv')
data.head()
#Loaded data into numpy array
xAxis = data["V1"]
yAxis = data["V2"]



#start plotting data by using matplotlib.plylot library for scatter plot
plt.plot()
plt.xlim([3, 6]) #setting x-axis boundaries
plt.ylim([0.5, 5]) # setting y-axis boundaries
plt.title('Dataset') # title of the scatter plot graph
plt.scatter(xAxis, yAxis) #generating the scatter plot
plt.show() # displays the scatter plot

# create new plot and data to determine the optimal number of clusters using K-means clustering algorithm
plt.plot()
X = np.array(list(zip(xAxis, yAxis))).reshape(len(xAxis), 2)
colors = ['b', 'g', 'r']
markers = ['o', 'v', 's']
# k means determine k
distortions = []
K = range(1,10)
for k in K:
    kmeanModel = KMeans(n_clusters=k).fit(X)
    kmeanModel.fit(X)
    distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])

# Plot the elbow graph
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()
















