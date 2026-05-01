import numpy as np


print("--- Exercício 4 ---")
coeficientes = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
])

determinante = np.linalg.det(coeficientes)
print(f"Determinante: {determinante:.2f}")

if round(determinante, 2) != 0:
    print("O sistema linear é resolvível (Determinante ≠ 0).")
else:
    print("O sistema não possui solução única (Det = 0).")
