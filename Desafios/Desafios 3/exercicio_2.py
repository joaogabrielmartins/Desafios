print("--- Exercício 2 ---")
vendas_semana1 = [[100, 150], [200, 250]]
vendas_semana2 = [[120, 160], [210, 260]]

soma_vendas = [[0, 0], [0, 0]]
total_geral = 0

for i in range(2):
    for j in range(2):
        soma_vendas[i][j] = vendas_semana1[i][j] + vendas_semana2[i][j]
        total_geral += soma_vendas[i][j]

print("Soma das Vendas (Semana 1 + Semana 2):")
for linha in soma_vendas:
    print(linha)
print(f"Total Geral de Vendas: {total_geral}")
