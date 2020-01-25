import numpy as np
import pandas
import sklearn
from sklearn.decomposition import PCA
import os
from matplotlib import pyplot as plt

divorce = np.loadtxt("divorce.csv", delimiter=";", skiprows=1)
pca = PCA(1)
div_trans = pca.fit_transform(divorce[:,0:-1])

#plt.scatter(div_trans[:,0], div_trans[:,1])
ydivorce = divorce[:,-1] == 1
ndivorce = divorce[:,-1] == 0
plt.scatter(div_trans[ydivorce,0],div_trans[ydivorce,0],c="r")
plt.scatter(div_trans[ndivorce,0],div_trans[ndivorce,0],c="g")
plt.title("Principal Component (1) on Divorce Questions")
plt.xlabel("Component 1")
plt.ylabel("Component 1")
plt.legend(["Divorce","No Divorce"])

print(pca.components_)
component = pca.components_
print(pca.components_[0,:].argsort() + 1)


pca2 = PCA(2)
div_trans2 = pca2.fit_transform(divorce[:,0:-1])
plt.figure()

plt.scatter(div_trans2[ydivorce,0],div_trans2[ydivorce,1],c="r")
plt.scatter(div_trans2[ndivorce,0],div_trans2[ndivorce,1],c="g")
plt.title("Principal Components (2) on Divorce Questions")
plt.xlabel("Component 1")
plt.ylabel("Component 2")
plt.legend(["Divorce","No Divorce"])


plt.show()