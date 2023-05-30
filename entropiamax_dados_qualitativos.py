# -*- coding: utf-8 -*-
"""
Created on Tue May 30 16:37:43 2023

@author: Rebeca
"""

import math

def calcular_entropia_maxima(base_dados):
    total_registros = len(base_dados)
    valores_unicos = set(base_dados)
    num_valores_unicos = len(valores_unicos)

    probabilidade = 1 / num_valores_unicos

    entropia_maxima = -1 * sum(probabilidade * math.log2(probabilidade) for n in range(num_valores_unicos))

    return entropia_maxima


dados = 'D:\Downlods\iris.csv'
entropia_max = calcular_entropia_maxima(dados)
print(f"A entropia máxima da base de dados é: {entropia_max}")
