import numpy as np


print("--- Exercício 5 ---")
estoque = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

precos = np.array([
    [5.00],
    [10.00],
    [15.00]
])

estoque_transposto = estoque.T
print("Estoque Transposto (Lojas nas linhas, Produtos nas colunas):")
print(estoque_transposto)

valor_total_por_loja = np.dot(estoque_transposto, precos)

print("\nValor total em estoque por loja (R$):")
print(valor_total_por_loja)
