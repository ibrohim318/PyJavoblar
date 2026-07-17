import math
from math import sqrt
import random as r

# uzunlik = lambda pi, r: 2 * pi * r
# print(uzunlik(math.pi, 10))

# ! sqrt
# sonlar = list(range(11))
# ildiz = list(map(sqrt, sonlar))
# print(ildiz)


# # ! daraja
# def daraja(x):
#     return x * x
# print(list(map(daraja, sonlar)))

# kvadrat = list(map(lambda x: x * x, sonlar))
# print(kvadrat)

sonlar = r.sample(range(100), 10)
# def juftmi(x):
#     return x % 2 == 0
# juftSonlar = list(filter(juftmi, sonlar))

# juftSonlar = list(filter(lambda son: son % 2 == 0, sonlar))
# print(juftSonlar)

mevalar = ["olma", "anor", "banan", "shaftoli"]
harf = "a"
# mevalar_b = list(filter(lambda meva: meva.startswith(harf), mevalar))
# print(mevalar_b)

# mevalar2 = list(filter(lambda meva: len(meva) <= 5, mevalar))
# print(mevalar2)

mevalar3 = list(
    filter(lambda meva: (meva.startswith("a") and (meva.endswith("r"))), mevalar)
)
print(mevalar)
