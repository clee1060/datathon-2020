import numpy as np
import sklearn
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from scipy.stats import pearsonr
import statistics
import pickle

#!/usr/bin/env python

def predict(q35, q36, q40):

    clf = pickle.load(open("svmweb.p", 'rb'))
    response = [[q35, q36, q40]]

    result = clf.predict(response)

    return(result)
