# -*- coding: utf-8 -*-
"""Bosques_Aleatorios(Boston).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/110Pu8i4reCn-MLMG4XOdDdOAkSRyrdNC

***BOSQUES ALEATORIOS REGRESION***
---

1: Importamos la librerias
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import datasets

"""2: Cargamos el dataset en boston"""

boston = datasets.load_boston()

"""3: Mostramos los datos del dataset Boston"""

print(boston)

"""4: Verifico la información contenida en el dataset"""

print(boston.keys())

"""5: Verifico las características del dataset"""

print(boston.DESCR)

"""6: Verifico la cantidad de datos que hay en los dataset"""

print(boston.data.shape)

"""7: Verifico la información de las columnas"""

print(boston.feature_names)

"""8: Seleccionamos solamente la columna 6 del dataset"""

X_bar = boston.data[:, np.newaxis, 5]

"""9: Defino los datos correspondientes a las etiquetas"""

y_bar = boston.target

"""10: Graficamos los datos correspondientes"""

plt.scatter(X_bar, y_bar)
plt.show()

"""Implementamos los bosques aleatorios de regresion

11: Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos 80% y 20%
"""

X_train, X_test, y_train, y_test = train_test_split(X_bar, y_bar, test_size=0.25)

"""12: Defino el algoritmo a utilizar"""

bar = RandomForestRegressor(n_estimators = 300, max_depth = 8)

"""13: Entreno el modelo"""

bar.fit(X_train, y_train)

"""14: Realizo una predicción"""

Y_pred = bar.predict(X_test)

"""15: Graficamos los datos de prueba junto con la predicción"""

X_grid = np.arange(min(X_test), max(X_test), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X_test, y_test)
plt.plot(X_grid, bar.predict(X_grid), color='red', linewidth=3)
plt.show()

"""16: Mostramos las precision"""

print(bar.score(X_train, y_train))