import numpy as np


print("--- Exercício 3 ---")
notas_alunos = np.array([
    [8.0, 7.5, 9.0],
    [6.0, 5.5, 7.0],
    [9.5, 10.0, 9.0]
])

medias = notas_alunos.mean(axis=1)

for i in range(len(medias)):
    print(f"Média do Aluno {i+1}: {medias[i]:.2f}")
