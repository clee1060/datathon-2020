import numpy as np
import sklearn
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

import os
from matplotlib import pyplot as plt

divorce = np.loadtxt("divorce.csv", delimiter=";", skiprows=1)
Xtrain, Xtest, ytrain, ytest = train_test_split(divorce[:,0:-1], divorce[:,-1], train_size=.5)

svm = SVC()
svm.fit(Xtrain, ytrain)



