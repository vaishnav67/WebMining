import numpy as np
import pandas as pd
from scipy.io import arff
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
#Dataset = https://archive.ics.uci.edu/ml/machine-learning-databases/00426/
data = arff.loadarff('Autism-Adult-Data.arff')
df = pd.DataFrame(data[0])
objs=list(df.columns)
strings=['gender','ethnicity','jaundice','autism','country_of_res','used_app_before','age_desc','relation','Class/ASD']
for i in objs:
    try:
        df[i]=df[i].str.decode('utf-8')
    except:
        print()
df = df.dropna()
kmeans = KMeans(n_clusters=2, max_iter=600, algorithm = 'auto')
for i in strings:
    labelEncoder = LabelEncoder()
    labelEncoder.fit(df[i])
    df[i] = labelEncoder.transform(df[i])
X = np.array(df.drop(['Class/ASD'], 1).astype(float))
x_true = np.array(df['Class/ASD'])
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
kmeans.fit(X_scaled)
x_pred=kmeans.predict(X)
print(accuracy_score(x_true, x_pred))
