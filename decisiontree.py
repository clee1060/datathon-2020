import numpy as np
import sklearn
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import catboost

import os
from matplotlib import pyplot as plt

divorce = np.loadtxt("divorce.csv", delimiter=";", skiprows=1)





