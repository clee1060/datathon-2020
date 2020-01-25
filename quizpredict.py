import numpy as np
import sklearn
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from scipy.stats import pearsonr
import statistics
import pickle
import sys

def predict(q35, q36, q40):

    clf = pickle.load(open("svmweb.p", 'rb'))
    response = [[q35, q36, q40]]

    result = clf.predict(response)

    return(result)


print("On a scale of 1 to 5, to what degree do you agree with the following statements?\n")
print("I can insult my spouse during our discussions")
q35 = float(input("Response: "))
while q35 not in [1, 2, 3, 4, 5]:
    q35 = float(input("Please enter an integer between 1 and 5: "))

print("I can be humiliating during discussions with my spouse")
q36 = float(input("Response: "))
while q36 not in [1, 2, 3, 4, 5]:
    q36 = float(input("Please enter an integer between 1 and 5: "))

print("I am just starting a discussion with my spouse before I know what's going on")
q40 = float(input("Response: "))
while q40 not in [1, 2, 3, 4, 5]:
    q40 = float(input("Please enter an integer between 1 and 5: "))

result = predict(q35-1, q36-1, q40-1)

if result == 1:
    print("You will get divorced!")
else:
    print("You will not get divorced!")