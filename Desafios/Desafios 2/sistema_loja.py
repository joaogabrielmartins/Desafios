def cadastrar_produto(produtos):
    while True:
        nome = input("Nome do produto: ").strip()
        if not nome:
            print("Nome não pode ser vazio.")
            continue
        existe = False
        for p in produtos:
            if p["nome"].lower() == nome.lower():
                existe = True
                break
        if existe:
            print("Produto já cadastrado.")
            continue
        break

    while True:
        try:
            preco = float(input("Preço: "))
            if preco <= 0:
                print("Preço deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Valor inválido. Digite um número real.")

    while True:
        try:
            estoque = int(input("Estoque inicial: "))
            if estoque < 0:
                print("Estoque não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

    produtos.append({"nome": nome, "preco": preco, "estoque": estoque})
    print("\nProduto cadastrado com sucesso!")
    return produtos


def listar_produtos(produtos):
    if not produtos:
        print("\nNenhum produto cadastrado.")
        return False
    print("\n--- Produtos Disponíveis ---")
    for i, p in enumerate(produtos):
        texto = (f"{i}. {p['nome']} - R$ {p['preco']:.2f} - "
                 f"Estoque: {p['estoque']}")
        print(texto)
    return True


def calcular_venda(produto, quantidade):
    valor_bruto = produto["preco"] * quantidade
    desconto = 0.0
    if quantidade > 10:
        desconto = valor_bruto * 0.05
    valor_final = valor_bruto - desconto
    produto["estoque"] -= quantidade
    return {
        "valor_bruto": valor_bruto,
        "desconto": desconto,
        "valor_final": valor_final
    }


def realizar_venda(produtos, vendas):
    nome_cliente = input("\nNome do cliente: ").strip()
    if not nome_cliente:
        print("Nome do cliente não pode ser vazio.")
        return

    if not listar_produtos(produtos):
        return

    produto_selecionado = None

    while True:
        try:
            indice = int(input("Selecione o produto pelo índice: "))
            if indice < 0 or indice >= len(produtos):
                print("Índice inválido.")
                continue
            produto_selecionado = produtos[indice]
            break
        except ValueError:
            print("Digite um número inteiro válido para o índice.")

    while True:
        try:
            quantidade = int(input("Quantidade desejada: "))
            if quantidade <= 0:
                print("A quantidade deve ser maior que zero.")
                continue
            if quantidade > produto_selecionado["estoque"]:
                print(f"Estoque insuficiente. Temos apenas "
                      f"{produto_selecionado['estoque']} unidades.")
                continue
            break
        except ValueError:
            print("Digite um número inteiro válido para a quantidade.")

    dados_venda = calcular_venda(produto_selecionado, quantidade)

    venda = {
        "cliente": nome_cliente,
        "produto": produto_selecionado["nome"],
        "quantidade": quantidade,
        "valor_bruto": dados_venda["valor_bruto"],
        "desconto": dados_venda["desconto"],
        "valor_final": dados_venda["valor_final"]
    }

    vendas.append(venda)
    print("\nVenda realizada com sucesso!")


def gerar_relatorio(vendas):
    if not vendas:
        print("\nNenhuma venda realizada até o momento.")
        return 0

    print("\n=== Relatório de Vendas ===")
    total_arrecadado = 0
    for venda in vendas:
        print(f"Cliente: {venda['cliente']}")
        print(f"Produto: {venda['produto']}")
        print(f"Quantidade: {venda['quantidade']}")
        print(f"Valor Bruto: R$ {venda['valor_bruto']:.2f}")
        print(f"Desconto: R$ {venda['desconto']:.2f}")
        print(f"Valor Final: R$ {venda['valor_final']:.2f}")
        print("-" * 20)
        total_arrecadado += venda["valor_final"]

    print(f"Total arrecadado pela loja: R$ {total_arrecadado:.2f}")
    return total_arrecadado


def salvar_relatorio(vendas):
    if not vendas:
        print("\nNenhuma venda para salvar.")
        return

    print("\nDigite o nome ou caminho do arquivo para salvar")
    caminho = input("(ex: relatorio_vendas.txt): ")
    try:
        with open(caminho, 'w', encoding='utf-8') as arquivo:
            arquivo.write("=== Relatório de Vendas ===\n")
            total_arrecadado = 0
            for venda in vendas:
                arquivo.write(f"Cliente: {venda['cliente']}\n")
                arquivo.write(f"Produto: {venda['produto']}\n")
                arquivo.write(f"Quantidade: {venda['quantidade']}\n")
                arquivo.write(f"Valor Bruto: R$ {venda['valor_bruto']:.2f}\n")
                arquivo.write(f"Desconto: R$ {venda['desconto']:.2f}\n")
                arquivo.write(f"Valor Final: R$ {venda['valor_final']:.2f}\n")
                arquivo.write("-" * 20 + "\n")
                total_arrecadado += venda["valor_final"]
            texto_total = f"Total arrecadado: R$ {total_arrecadado:.2f}\n"
            arquivo.write(texto_total)
        print(f"\nRelatório salvo com sucesso em: {caminho}")
    except Exception as e:
        print(f"\nErro ao tentar salvar o arquivo: {e}")


def main():
    produtos = []
    vendas = []

    while True:
        print("\n--- Menu da Loja ---")
        print("1. Cadastrar produto")
        print("2. Realizar venda")
        print("3. Gerar relatório")
        print("4. Salvar relatório em arquivo")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_produto(produtos)
        elif opcao == '2':
            realizar_venda(produtos, vendas)
        elif opcao == '3':
            gerar_relatorio(vendas)
        elif opcao == '4':
            salvar_relatorio(vendas)
        elif opcao == '5':
            print("\nEncerrando o programa. Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
