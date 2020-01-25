import numpy as np
import sklearn
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from scipy.stats import pearsonr
import statistics

import os
from matplotlib import pyplot as plt


all = []
limit = []
limworst = []
pcasc = []

for i in range(1000):
    divorce = np.loadtxt("divorce.csv", delimiter=";", skiprows=1)
    pca = PCA(1)
    div_trans = pca.fit_transform(divorce[:,0:-1])

    Xtrain, Xtest, ytrain, ytest, PCAtrain, PCAtest = train_test_split(divorce[:,0:-1], divorce[:,-1], div_trans, train_size=.65)

    svmall = SVC(C = 50, kernel="linear")
    svmall.fit(Xtrain, ytrain)

    predyall = svmall.predict(Xtest)

    #print("All Questions: " + str(accuracy_score(ytest, predyall)))

    questions = [34, 35, 39]

    svm3 = SVC(C = 4, kernel="linear")
    svm3.fit(Xtrain[:,questions], ytrain)

    predy3 = svm3.predict(Xtest[:,questions])

    wquestions = [5,6,45]

    svmworst = SVC(C=4, kernel="linear")
    svmworst.fit(Xtrain[:,wquestions], ytrain)

    predyworst = svmworst.predict(Xtest[:,wquestions])

    #print("Limited Questions: " + str(accuracy_score(ytest,predy3)))

    svmpca = SVC(C=50, kernel="linear")
    svmpca.fit(PCAtrain, ytrain)

    predypca = svmpca.predict(PCAtest)

    #print("PCA: " + str(accuracy_score(ytest, predypca)))

    #print("35/36 Correlation: " + str(pearsonr(divorce[:,34],divorce[:,35])))

    all.append(accuracy_score(ytest, predyall))
    limit.append(accuracy_score(ytest,predy3))
    limworst.append(accuracy_score(ytest, predyworst))
    pcasc.append(accuracy_score(ytest, predypca))
print("All: " + str(statistics.mean(all)))
print("Limit: " + str(statistics.mean(limit)))
print("Limit worst: " + str(statistics.mean(limworst)))
print("PCA: " + str(statistics.mean(pcasc)))