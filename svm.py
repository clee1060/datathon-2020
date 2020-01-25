import numpy as np
import sklearn
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import os
from matplotlib import pyplot as plt

divorce = np.loadtxt("divorce.csv", delimiter=";", skiprows=1)
Xtrain, Xtest, ytrain, ytest = train_test_split(divorce[:,0:-1], divorce[:,-1], train_size=.65, random_state=4)

svmall = SVC(C = 4, kernel="linear")
svmall.fit(Xtrain, ytrain)

predyall = svmall.predict(Xtest)

print("All Questions: " + str(accuracy_score(ytest, predyall)))

questions = [34, 35]

svm3 = SVC(C = 4, kernel="linear")
svm3.fit(Xtrain[:,questions], ytrain)

predy3 = svm3.predict(Xtest[:,questions])

print("Limited Questions: " + str(accuracy_score(ytest,predy3)))