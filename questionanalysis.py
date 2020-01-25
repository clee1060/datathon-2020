import numpy as np
import sklearn
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

index = np.arange(5)
bar_width = 0.35

divorce = np.loadtxt("divorce.csv", delimiter=";", skiprows=1)

def count (x):
    list = [0,0,0,0,0]
    for num in x:
        list[int(num)] += 1
    return list


q_34_y = [divorce[i][33] for i in range(0, 170) if divorce[i][-1] == 1]
q_35_y = [divorce[i][34] for i in range(0, 170) if divorce[i][-1] == 1]
q_39_y = [divorce[i][38] for i in range(0, 170) if divorce[i][-1] == 1]

q_34_n = [divorce[i][33] for i in range(0, 170) if divorce[i][-1] == 0]
q_35_n = [divorce[i][34] for i in range(0, 170) if divorce[i][-1] == 0]
q_39_n = [divorce[i][38] for i in range(0, 170) if divorce[i][-1] == 0]

question_34_y = count(q_34_y)
question_34_n = count(q_34_n)
question_35_y = count(q_35_y)
question_35_n = count(q_35_n)
question_39_y = count(q_39_y)
question_39_n = count(q_39_n)

# Good
plt.bar(index, question_34_y, bar_width, color="r", label = "Divorced")
plt.bar(index + bar_width, question_34_n, bar_width, color="g", label = "Not Divorced")
plt.title("Answers to Question 34")
plt.xlabel("Answer to the Survey Question")
plt.ylabel("Number of People")
plt.legend(["Divorce","No Divorce"])
plt.figure()

plt.bar(index, question_35_y, bar_width, color="r", label = "Divorced")
plt.bar(index + bar_width, question_35_n, bar_width, color="g", label = "Not Divorced")
plt.title("Answers to Question 35")
plt.xlabel("Answer to the Survey Question")
plt.ylabel("Number of People")
plt.legend(["Divorce","No Divorce"])
plt.figure()

plt.bar(index, question_39_y, bar_width, color="r", label = "Divorced")
plt.bar(index+ bar_width, question_39_n, bar_width, color="g", label = "Not Divorced")
plt.title("Answers to Question 39")
plt.xlabel("Answer to the Survey Question")
plt.ylabel("Number of People")
plt.legend(["Divorce","No Divorce"])
plt.figure()

#Bad
q_6_y = [divorce[i][5] for i in range(0, 170) if divorce[i][-1] == 1]
q_6_n = [divorce[i][5] for i in range(0, 170) if divorce[i][-1] == 0]
q_7_y = [divorce[i][6] for i in range(0, 170) if divorce[i][-1] == 1]
q_7_n = [divorce[i][6] for i in range(0, 170) if divorce[i][-1] == 0]

question_6_y = count(q_6_y)
question_6_n = count(q_6_n)
question_7_y = count(q_7_y)
question_7_n = count(q_7_n)

plt.bar(index, question_6_y, bar_width, color="r", label = "Divorced")
plt.bar(index + bar_width, question_6_n, bar_width, color="g", label = "Not Divorced")
plt.title("Answers to Question 6")
plt.xlabel("Answer to the Survey Question")
plt.ylabel("Number of People")
plt.legend(["Divorce","No Divorce"])
plt.figure()

plt.bar(index, question_7_y, bar_width, color="r", label = "Divorced")
plt.bar(index+ bar_width, question_7_n, bar_width, color="g", label = "Not Divorced")
plt.title("Answers to Question 7")
plt.xlabel("Answer to the Survey Question")
plt.ylabel("Number of People")
plt.legend(["Divorce","No Divorce"])

plt.show()