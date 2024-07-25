# -*- coding: utf-8 -*-
"""projet_3_breast_cancer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1m_P9yC7xByTt68BxexnkavjkEmv_BEp0
"""

import pandas as pd

df_breast_cancer = pd.read_csv('df_breast_cancer.csv').drop(columns = ['Unnamed: 0'], axis =1)

df_breast_cancer.columns

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline as ImbPipeline

# Séparer les caractéristiques et la variable cible
X = df_breast_cancer.drop(columns=['id', 'diagnosis'])
y = df_breast_cancer['diagnosis']


# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state=42, stratify=y)

# Définir les techniques de rééchantillonnage
over_sampler = SMOTE(random_state=42)
under_sampler = RandomUnderSampler(random_state=42)

# Créer le pipeline avec MaxAbsScaler, SMOTE, RandomUnderSampler, et Logistic Regression
pipeline = ImbPipeline([
    ('scaler', StandardScaler()),
    ('over', over_sampler),
    ('under', under_sampler),
    ('model', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Entraîner le pipeline
pipeline.fit(X_train, y_train)

# Prédictions sur l'ensemble de test
y_pred = pipeline.predict(X_test)


def prediction_breastcancer(liste):
  if pipeline.predict(liste)[0] == 0 :
    return "Le risque potentiel de tumeur bénigne est détecté"
  else :
    return "Le risque potentiel de tumeur maligne est détecté"
