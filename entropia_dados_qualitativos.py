# -*- coding: utf-8 -*-
"""
Created on Mon May 29 19:24:12 2023

@author: Rebeca
"""

import numpy as np
import pandas as pd
import math

dados = pd.read_csv('D:\Downlods\iris.csv', delimiter=',')
coluna_qualitativa = dados['class'] 
frequencia = coluna_qualitativa.value_counts()
proporcao = frequencia / len(coluna_qualitativa)
entropia = -sum(proporcao * np.log2(proporcao))
print('Entropia: ', entropia)
