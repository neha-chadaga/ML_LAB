from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
import numpy as np
import pandas as pd

iris=datasets.load_iris()
X=iris.data
Y=iris.target

#Shuffle of Data 
X,Y = shuffle(X,Y)

model=KMeans(n_clusters=3,init='k-means++',max_iter=10,n_init=1,random_state=3425)

#Training of the model
model.fit(X)

# This is what KMeans thought (Prediction)
Y_Pred=model.labels_

from sklearn.metrics import confusion_matrix

cm=confusion_matrix(Y,Y_Pred)
print(cm)

from sklearn.metrics import accuracy_score

print(accuracy_score(Y,Y_Pred))

#Defining EM Model
from sklearn.mixture import GaussianMixture
model2=GaussianMixture(n_components=3,random_state=3425)

#Training of the model
model2.fit(X)

#Predicting classes for our data
Y_predict2= model2.predict(X)

#Accuracy of EM Model
from sklearn.metrics import confusion_matrix

cm=confusion_matrix(Y,Y_predict2)
print(cm)

from sklearn.metrics import accuracy_score

print(accuracy_score(Y,Y_predict2))
