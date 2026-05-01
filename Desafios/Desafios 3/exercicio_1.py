import random


print("--- Exercício 1 ---")
matriz_aleatoria = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(3):
    for j in range(3):
        matriz_aleatoria[i][j] = random.randint(1, 100)

print("Matriz 3x3 com números aleatórios:")
for linha in matriz_aleatoria:
    print(linha)
