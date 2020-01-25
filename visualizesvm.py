from sklearn.svm import SVC
from sklearn.decomposition import PCA
import numpy as np
from matplotlib import pyplot as plt
import pickle
import os

divorce = np.loadtxt("datathon-2020/divorce.csv", delimiter=";", skiprows=1)
clf = pickle.load(open("datathon-2020/svmweb.p", 'rb'))
ydivorce = divorce[:,-1] == 1
ndivorce = divorce[:,-1] == 0
pca = PCA(1)
div_trans = pca.fit_transform(divorce[:,0:-1])

plt.scatter(div_trans[ydivorce,0],np.zeros(div_trans[ydivorce,0].shape),c="r")
plt.scatter(div_trans[ndivorce,0],np.zeros(div_trans[ndivorce,0].shape),c="g")


print(clf.decision_function(np.arange(-15,15,.1).reshape(-1, 1)))



plt.show()