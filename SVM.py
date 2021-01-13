##This script perform the randomization 10 times using bootstrapping and test the accuracy. 

import numpy as np
from sklearn import svm
from sklearn import metrics

def loadtxt(inputfile):
	input_file=np.loadtxt(inputfile,dtype='string',delimiter=',')

	##bootstrapping 500 iterations
	iter = 500
	for i in range(iter):
		bootstrapSamples = np.random.choice(data,size=45)
		#bootstrapSamples = resample(data,n_samples=500,replace=1)
		

	###split the train and test data according to 70%~30%
	x,y = np.split(data,(4,),axis=1)
	x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=1,train_size=0.7)
	
	return x_train,x_test,y_train,y_test

def svm(x_train,x_test,y_train,y_test):
	###train SVM
	classifier = svm.SVC(C=0.8,kernel='rbf',gamma=20,decision_function_shape='ovr')
	classifier.fit(x_train,y_train.ravel())
	
	return classifier

def plot(classifier,x_test,y_test):
	pred_label = classifier.predict(y_test)
	accuracy = classifier.score(x_test,y_test)
        fpr,tpr,thresholds = sklearn.metrics.roc_curve(y_test,pred_label,pos_label=1)
	roc_auc	= sklearn.metrics.roc_auc_score(fpr,tpr)
	
if __name__ == __main__
