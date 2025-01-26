import pandas as pd
import numpy as np
#import statsmodels.api as sm 4 import io
import base64
import io
import matplotlib.image as mpimg
from io import BytesI0


import seaborn as sns


c=pd.read_csv("creditcard.csv")
print(c.head())

from sklearn.preprocessing import StandardScaler


c=StandardScaler()
amount=c['Amount'].values
c['Amount']=c.fit_transform(amount.reshape(-1,1))

c.drop(['Time'], axis=1, inplace=True)
x=c.drop('Class', axis=1).values
y=c['Class'].values
print(x)

