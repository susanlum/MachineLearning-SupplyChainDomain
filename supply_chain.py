#-------------------------------------------------------------------------------------------------------------------------------------------#
# Load & Overview of Data
#-------------------------------------------------------------------------------------------------------------------------------------------#

# importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import RobustScaler # for RobustScaler
from sklearn.model_selection import train_test_split 
from sklearn.metrics import confusion_matrix # to create a confusion matrix
from sklearn.metrics import plot_confusion_matrix # to draw a confusion matrix

# read the train data
df = pd.read_csv('train.csv')
df 

# Check for datatypes 
df.dtypes

# Check for the null values
df.isna().sum()

# Check for duplicates 
df.duplicated().sum()

df.info()

df['Reached.on.Time_Y.N'].value_counts()

#-------------------------------------------------------------------------------------------------------------------------------------------#
# Data Visualisation
#-------------------------------------------------------------------------------------------------------------------------------------------#

g = sns.pairplot(df,hue="Reached.on.Time_Y.N", palette="husl")

# To perform EDA to answer the following questions:-

# 1) What was Customer Rating? And was the product delivered on time?

# To plot number of Customer Rating with labels from 1 (Worst) to 5 (Best). 
sns.countplot(x = df['Customer_rating']);

# To plot number of Reached On Time where 1 Indicates that the product has NOT reached on time and 0 indicates it has reached on time.
sns.countplot(x = df['Reached.on.Time_Y.N']);

# To plot Customer Rating versus Reached On Time
sns.countplot(x='Customer_rating', data=df, hue='Reached.on.Time_Y.N')
plt.show()

# 2) Is Customer query is being answered?
sns.countplot(x = df['Customer_care_calls']);

# To plot Customer_care_calls versus Reached.on.Time_Y.N
sns.countplot(x='Customer_care_calls', data=df, hue='Reached.on.Time_Y.N')
plt.show()

# 3) If Product importance is high. having highest rating or being delivered on time?
# To plot Product Importance (Low, Medium, High) versus Customer Rating [from 1 (Worst) to 5 (Best)]
sns.countplot(x='Product_importance', data=df, hue='Customer_rating')
plt.show()

# To plot Product Importance (Low, Medium, High) versus Reached.on.Time_Y.N (where 1=product has NOT reached on time; 0=product has reached on time)
sns.countplot(x='Product_importance', data=df, hue='Reached.on.Time_Y.N')
plt.show()

# Insights: Based on the barplots above, high product importance does not affect customer rating. However, when product importance is high, 
# the products have not reached on time.

sns.set(rc = {'figure.figsize': (10, 8)})
sns.heatmap(df.corr(), cmap = 'PuOr', annot = True, vmin = -1, vmax = 1, center = 0);
# annot = True -> label heatmap with correlation number
# center=0 -> white colour at the centre

#-------------------------------------------------------------------------------------------------------------------------------------------#
# Split the Data into Dependent and Indepedent Variables
#-------------------------------------------------------------------------------------------------------------------------------------------#

# Make a new copy of columns used to make predictions (ie. x)
X = df.drop('Reached.on.Time_Y.N', axis=1).copy() 
X.head()

# Make a new copy of the column of data we want to predict
y = df['Reached.on.Time_Y.N'].copy()
y.head()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

#-------------------------------------------------------------------------------------------------------------------------------------------#
# Encode the categorical variables
#-------------------------------------------------------------------------------------------------------------------------------------------#

```
If perform the encoding before the split, it will lead to data leakage (train-test contamination) In the sense, it will introduce new data 
(integers of Label Encoders) and use it for the models thus it will affect the end predictions results (good validation scores but poor in deployment).

After the train and validation data category already matched up, we can perform fit_transform on the train data, then only transform for the 
validation data - based on the encoding maps from train data.

Almost all feature engineering like standarisation, Normalisation etc should be done after train testsplit.
```



