#Import python modules
import numpy as np
import pandas as pd

#Visualisation
import matplotlib.pyplot as plt
#import missingno
import seaborn as sns

#Model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve, classification_report
from sklearn.preprocessing import LabelEncoder

from sklearn import svm  #for Support Vector Machine (SVM) Algorithm
from sklearn import metrics #for checking the model accuracy


# split into train/test
def train_test_split(df, train_frac= 0.7, seed=1):
    df_matrix = df.values

    # shuffle the data
    np.random.seed(seed)
    np.random.shuffle(df_matrix)

    # split the data
    train_size = int(df_matrix.shape[0] * train_frac)
    # features are all except last column
    train_features  = df_matrix[:train_size, :-1]
    # the last column
    train_labels = df_matrix[:train_size, -1]

    # test data
    test_features = df_matrix[train_size:, :-1]
    test_labels = df_matrix[train_size:, -1]

    return (train_features, train_labels), (test_features, test_labels)

#Energy Usage
from codecarbon import EmissionsTracker

tracker = EmissionsTracker()
#@track_emissions(project_name="asd screening")

def main():

    #load the adult autism dataset
    df = pd.read_csv("Autism_Data.arff")
    df = df.replace('?', np.nan)

    #column name spell check/ fixes
    df = df.rename(columns = {"A1_Score":"A1","A2_Score":"A2", 'A3_Score':'A3', 'A4_Score':'A4', 'A5_Score':'A5', 'A6_Score':'A6', 'A7_Score':'A7', 'A8_Score':'A8', 'A9_Score':'A9', 'A10_Score':'A10', "jundice":"jaundice", "austim":"autism", "contry_of_res": "country", "Class/ASD":"asd_classification"})

    #Missing data
 #   missingno.matrix(df, figsize =(30,10))
 #   print(df.dtypes)
 #   print(df.describe())
    print(df.age)

    fig = plt.figure(figsize=(26,8))
    sns.countplot(x="age", data=df)

    #Check how many NaN values exist
    df['age'].isnull().sum()

    #Removing the two rows that don't have the age values
    df.dropna(subset = ["age"], inplace=True)

    df['age'].max()
    mean = df['age'].mean()
    df['age']= df['age'].replace(383.0 ,mean)

    #Country: Country of residence of the participants. Maximum participants are from United States, UAE, India, New Zealand and the UK.
    fig = plt.figure(figsize=(22,25))
    sns.countplot(y='country', data=df);
    df.country.value_counts()

    #Gender Distribution
    fig = plt.figure(figsize=(10,6))
    sns.countplot(x="gender", data=df, facecolor=(0, 0, 0, 0), linewidth=5, edgecolor=sns.color_palette("dark", 3))


    #Jaundice at birth
    fig = plt.figure(figsize=(25,6))
    sns.countplot(y='jaundice', data=df);
    df.jaundice.value_counts()

    # If the user has an immediate family member who had a Pervasive Developmental Disorder then, yes( = 1); If the user has an immediate family member who had Pervasive Developmental Disorder then, no( = 0); According to the dataset, 91 individuals had a family member who had PDD out of 704.
    new_df= pd.DataFrame({'autism':df.autism.map(dict(yes=1,no=0))})
    df.update(new_df)
    df['autism'] = df['autism'].astype('int')
    fig = plt.figure(figsize=(25,6))
    sns.countplot(y='autism', data=df);
    df.autism.value_counts()

    #ASD Classification
    new_df = pd.DataFrame({'asd_classification':df.asd_classification.map(dict(YES=1,NO=0))})
    df.update(new_df)

    df['asd_classification'] = df['asd_classification'].astype('int')

    fig = plt.figure(figsize=(25,6))
    sns.countplot(y='asd_classification', data=df);
    df.asd_classification.value_counts()

    #Used App Before Whether the p/w ASD has used a screening app

    new_df = pd.DataFrame({'used_app_before':df.used_app_before.map(dict(yes=1,no=0))})
    df.update(new_df)
    df['used_app_before'] = df['used_app_before'].astype('int')
    fig = plt.figure(figsize=(25,6))
    sns.countplot(y='used_app_before', data=df);
    df.used_app_before.value_counts()
    df.age_desc.value_counts()

    plt.figure(figsize =(15,10))
    sns.countplot(x= 'ethnicity',data = df)
    df['ethnicity'].value_counts()

    plt.figure(figsize =(15,10))
    sns.countplot(x= 'relation', data = df)
    df['relation'].value_counts()

    # Dropped age (since its not an indicator whether an individual has ASD).
    # Incomplete data on Ethinicity, Relation (Check missing data plot)
    df.drop(['country', 'ethnicity', 'used_app_before' , 'age','age_desc','relation', 'result'],axis=1, inplace=True)

    fig = plt.figure(figsize=(12,10))
    sns.heatmap(df.corr())
#    plt.show()

    le = LabelEncoder()
    df.gender = le.fit_transform(df.gender)
    df.jaundice = le.fit_transform(df.jaundice)
    print(df)

    # get train/test data
    (train_features, train_labels), (test_features, test_labels) = train_test_split(df, train_frac=0.7)

    #train the model
    lg = LogisticRegression()

    lg.fit(train_features, train_labels)
    lgpredict = lg.predict(test_features)
    lg.score(test_features, test_labels)
    pred_lg = lg.predict(test_features)
    log_reg_predict_proba = lg.predict_proba(test_features)[:, 1]
    print('\nLogistic Regression Accuracy: {:.2f}%'.format(accuracy_score(test_labels, lgpredict) * 100))
    print('Logistic Regression AUC: {:.2f}%'.format(roc_auc_score(test_labels, lgpredict) * 100))
    print(classification_report(test_labels,pred_lg))
    #SupportVectorMachines

    model = svm.SVC()
    model.fit(train_features, train_labels)
    prediction=model.predict(test_features)
    score = model.score(test_features, test_labels)
    print('\nSVM Regression Accuracy: {:.2f}%'.format(accuracy_score(test_labels, prediction) * 100))
    print('SVM Regression AUC: {:.2f}%'.format(roc_auc_score(test_labels, prediction) * 100))
    print(classification_report(test_labels,prediction))



if __name__ == "__main__":
    tracker.start()
    main()
    emi: float=tracker.stop()
    print(f"overall emmisions:{emi} kg")
    emi= emi*89875517873681764
    print(f"overall emmisions:{emi} joules")
