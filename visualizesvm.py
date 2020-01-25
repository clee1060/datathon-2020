from sklearn.svm import SVC
from sklearn.decomposition import PCA
import numpy as np
from matplotlib import pyplot as plt
import pickle

clf = pickle.load(open("svmweb.p", 'rb'))

divorce = np.loadtxt("divorce.csv", delimiter=";", skiprows=1)
ydivorce = divorce[:,-1] == 1
ndivorce = divorce[:,-1] == 0
pca = PCA(1)
div_trans = pca.fit_transform(divorce[:,0:-1])

plt.scatter(div_trans[ydivorce,0],0,c="r")
plt.scatter(div_trans[ndivorce,0],0,c="g")