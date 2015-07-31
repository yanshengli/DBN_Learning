__author__ = 'lige'
#encoding:utf-8
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn import svm
from sklearn import neighbors

train_vector=np.zeros([1071,19937])
f1=open('train_all.txt','rb')
datas=f1.readlines()
i=0
for data in datas:
    data=data.strip()
    data=data.split('\t')
    #print data
    for ii in range(0,len(data)):
        train_vector[i,ii]=data[ii]
    i=i+1

test_vector=np.zeros([712,19937])


f2=open('test_all.txt','rb')
lines=f2.readlines()
print len(lines)
j=0
for line in lines:
    line=line.strip()
    line=line.split('\t')
    for jj in range(0,len(line)):
        test_vector[j,jj]=line[jj]
    j=j+1

cats = ['alt.atheism','sci.electronics']
newsgroups_train = fetch_20newsgroups(subset='train',categories=cats)
newsgroups_test = fetch_20newsgroups(subset='test',categories=cats)
ply=svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,
gamma=0.0, kernel='rbf', max_iter=-1, probability=False, random_state=None,
shrinking=True, tol=0.001, verbose=False)
#knn = neighbors.KNeighborsClassifier(n_neighbors=3, algorithm='ball_tree')
clf=ply.fit(train_vector, newsgroups_train.target)
pred = clf.predict(test_vector)
print pred

print metrics.f1_score(newsgroups_test.target, pred)


