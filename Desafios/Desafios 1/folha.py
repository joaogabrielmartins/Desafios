def calcular_salario_estagiario(salario_fixo):
    return {
        "bruto": salario_fixo,
        "inss": 0.0,
        "irrf": 0.0,
        "liquido": salario_fixo
    }


def calcular_salario_freelancer(horas, valor_hora):
    salario_bruto = horas * valor_hora
    desconto_inss = salario_bruto * 0.05
    salario_liquido = salario_bruto - desconto_inss

    return {
        "bruto": salario_bruto,
        "inss": desconto_inss,
        "irrf": 0.0,
        "liquido": salario_liquido
    }


def calcular_salario_clt(salario_bruto):
    desconto_inss = salario_bruto * 0.08
    desconto_irrf = 0.0

    if salario_bruto > 2000.00:
        desconto_irrf = salario_bruto * 0.10

    salario_liquido = salario_bruto - desconto_inss - desconto_irrf

    return {
        "bruto": salario_bruto,
        "inss": desconto_inss,
        "irrf": desconto_irrf,
        "liquido": salario_liquido
    }


def cadastrar_funcionario():
    print("\n--- NOVO CADASTRO ---")

    while True:
        nome = input("Digite o nome do funcionário: ").strip()
        if nome != "":
            break
        print("Erro: O nome não pode estar vazio.")

    while True:
        prompt_tipo = "Digite o tipo (estagiario, clt, freelancer): "
        tipo = input(prompt_tipo).strip().lower()
        if tipo in ["estagiario", "clt", "freelancer"]:
            break
        print("Erro: Tipo inválido.")

    while True:
        try:
            if tipo == "freelancer":
                horas = float(input("Digite as horas trabalhadas: "))
                valor = float(input("Digite o valor por hora: R$ "))

                if horas <= 0 or valor <= 0:
                    print("Erro: Valores devem ser maiores que zero.")
                    continue

                return {
                    "nome": nome,
                    "tipo": tipo,
                    "horas": horas,
                    "valor_hora": valor
                }
            else:
                prompt_salario = f"Digite o salário bruto do {tipo}: R$ "
                salario = float(input(prompt_salario))

                if salario <= 0:
                    print("Erro: O salário deve ser maior que zero.")
                    continue

                return {
                    "nome": nome,
                    "tipo": tipo,
                    "salario": salario
                }

        except ValueError:
            print("Erro Crítico: Digite apenas números válidos.")


def processar_salario(funcionario):
    tipo = funcionario["tipo"]

    if tipo == "estagiario":
        calc = calcular_salario_estagiario(funcionario["salario"])
    elif tipo == "clt":
        calc = calcular_salario_clt(funcionario["salario"])
    elif tipo == "freelancer":
        calc = calcular_salario_freelancer(
            funcionario["horas"],
            funcionario["valor_hora"]
        )

    # Junta os dados matemáticos com os dados de cadastro
    funcionario.update(calc)
    return funcionario


def gerar_relatorio(lista_funcionarios):
    print("\n=== Relatório de Folha de Pagamento ===")
    total_empresa = 0.0

    for func in lista_funcionarios:
        print(f"Nome: {func['nome']}")
        print(f"Tipo: {func['tipo'].capitalize()}")
        print(f"Salário Bruto: R$ {func['bruto']:.2f}")
        print(f"Desconto INSS: R$ {func['inss']:.2f}")
        print(f"Desconto IRRF: R$ {func['irrf']:.2f}")
        print(f"Salário Líquido: R$ {func['liquido']:.2f}")
        print("-" * 30)

        total_empresa += func['liquido']

    print(f"Total pago pela empresa: R$ {total_empresa:.2f}")


def salvar_relatorio(lista_funcionarios):
    try:
        with open("relatorio_folha.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("=== Relatório de Folha de Pagamento ===\n")
            total_empresa = 0.0

            for func in lista_funcionarios:
                arquivo.write(f"Nome: {func['nome']}\n")
                arquivo.write(f"Tipo: {func['tipo'].capitalize()}\n")
                arquivo.write(f"Salário Bruto: R$ {func['bruto']:.2f}\n")
                arquivo.write(f"Desconto INSS: R$ {func['inss']:.2f}\n")
                arquivo.write(f"Desconto IRRF: R$ {func['irrf']:.2f}\n")
                arquivo.write(f"Salário Líquido: R$ {func['liquido']:.2f}\n")
                arquivo.write("-" * 30 + "\n")

                total_empresa += func['liquido']

            arquivo.write(f"Total pago pela empresa: R$ {total_empresa:.2f}\n")

        print("\nSucesso: Relatório salvo como 'relatorio_folha.txt'.")
    except IOError:
        print("\nErro: Não foi possível salvar o arquivo.")


def main():
    lista_funcionarios = []

    while True:
        print("\nMenu Principal:")
        print("1. Cadastrar funcionário")
        print("2. Gerar relatório")
        print("3. Salvar relatório em arquivo")
        print("4. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            dados = cadastrar_funcionario()
            dados_processados = processar_salario(dados)
            lista_funcionarios.append(dados_processados)
            print("Funcionário cadastrado com sucesso!")

        elif opcao == "2":
            if len(lista_funcionarios) > 0:
                gerar_relatorio(lista_funcionarios)
            else:
                print("Nenhum funcionário cadastrado ainda.")

        elif opcao == "3":
            if len(lista_funcionarios) > 0:
                salvar_relatorio(lista_funcionarios)
            else:
                print("Nenhum funcionário cadastrado para salvar.")

        elif opcao == "4":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Escolha um número de 1 a 4.")


if __name__ == "__main__":
    main()
