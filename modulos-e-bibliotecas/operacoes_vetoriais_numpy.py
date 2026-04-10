import numpy as np


# print(v1 + v2)

# #concatenação (Junta as listas)

# a = [3, 5, 7]
# b = [-3, 1, -4]
# print(a+b)

v1 = np.array([3, 5, 7])
v2 = np.array([3, 1, 4])

def soma (v1, v2):
    som = np.add(v1, v2)
    return som


def subtracao(v1, v2):
    sub = np.subtract(v1, v2)
    return sub


def multi(v1,v2):
    mult = np.multiply(v1, v2)
    return mult


def divisao(v1,v2):
    div = np.divide(v1,v2)
    return div


def escalar(v1, v2):
    esca = np.dot(v1,v2)
    return esca

print(f'A soma de v1 e v2 é: {soma(v1, v2)}')
print(f'A subtracao de v1 e v2 é: {subtracao(v1, v2)}')
print(f'A divisao de v1 e v2 é: {divisao(v1, v2)}')
print(f'A multiplicacao de v1 e v2 é: {multi(v1, v2)}')
print(f'O produto escalar de v1 e v2 é: {escalar(v1, v2)}')