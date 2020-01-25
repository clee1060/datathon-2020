import numpy as np
import sklearn
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import catboost

import os
from matplotlib import pyplot as plt

divorce = np.loadtxt("divorce.csv", delimiter=";", skiprows=1)

Xtrain, Xtest, ytrain, ytest = train_test_split(divorce[:,0:-1], divorce[:,-1], train_size=.1)

clf = catboost.CatBoostClassifier(depth=5, learning_rate=.01, verbose=1)
pool = catboost.Pool(data=Xtrain, label=ytrain)

clf.fit(pool)

test_pool = catboost.Pool(data=Xtest)

predy = clf.predict(test_pool)

print("CatBoost: " + str(accuracy_score(ytest, predy)))
