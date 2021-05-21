import pandas as pd
import numpy as np
from scipy.io import arff
from sklearn import naive_bayes
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
objs = ['protocol_type','service','flag','land','logged_in','is_host_login','is_guest_login','class']
data = arff.loadarff('KDDTrain+.arff')
df = pd.DataFrame(data[0])
for i in objs:
    df[i]=df[i].str.decode('utf-8')
df_dummies=pd.get_dummies(df, columns=objs[:7])
labels = df_dummies[['class']]
features = df_dummies.drop(['class'], axis=1)
dt = naive_bayes.BernoulliNB()
dt = dt.fit(features,labels.values.ravel())
test = arff.loadarff('KDDTest+.arff')
t = pd.DataFrame(test[0])
for i in objs:
    t[i]=t[i].str.decode('utf-8')
t_dummies=pd.get_dummies(t, columns=objs[:7])
col_list = (df_dummies.append([t_dummies])).columns.tolist()
t_dummies = t_dummies.reindex(columns=col_list, fill_value=0)
t_dummies = t_dummies.drop(['class'], axis=1)
x_true=t['class'].values
x_pred=dt.predict(t_dummies)
print("Confusion Matrix: \n",confusion_matrix(x_true,x_pred, labels=['normal','anomaly']))
print("Accuracy score: ",accuracy_score(x_true,x_pred))
