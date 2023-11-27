import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split

# ---------------------------------
# Creating dataset and cleaning it
dataset = pd.read_csv("./dataset/Heart_disease_cleveland_new.csv")

dataset.isnull().sum()
dataset['target'] = dataset['target'].replace({0: 'Normal', 1: 'Heart Disease'})
# ---------------------------------


# ------------------------
# X, Y - TRAIN TEST SPLIT
X = dataset.drop(['target'], axis=1)
Y = dataset['target']

datasets = train_test_split(X, Y, train_size=0.7, test_size=0.3, random_state=2)
(X_train, X_test, Y_train, Y_test) = datasets
# ------------------------

model = tree.DecisionTreeClassifier(criterion='entropy', max_depth=4)

def getModel():
    return model