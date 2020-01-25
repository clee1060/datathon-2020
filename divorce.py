import numpy as np
import pandas
import sklearn
from sklearn.decomposition import PCA
import os
from matplotlib import pyplot as plt

os.chdir("/Users/matthewbrun/Spring 2020/Datathon/")


divorce = np.loadtxt("divorce.csv", delimiter=";", skiprows=1)
pca = PCA(1)
div_trans = pca.fit_transform(divorce[:,0:-1])

#plt.scatter(div_trans[:,0], div_trans[:,1])
ydivorce = divorce[:,-1] == 1
ndivorce = divorce[:,-1] == 0
plt.scatter(div_trans[ydivorce,0],div_trans[ydivorce,0],c="r")
plt.scatter(div_trans[ndivorce,0],div_trans[ndivorce,0],c="g")


print(pca.components_)
component = pca.components_
print(pca.components_[0,:].argsort())
plt.show()