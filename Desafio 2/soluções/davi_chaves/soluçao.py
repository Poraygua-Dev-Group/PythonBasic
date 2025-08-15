estoque = [
    {'codigo': 1, 'nome': 'Arroz 5 kg',  'preco': 25.50, 'quantidade': 50},
    {'codigo': 2, 'nome': 'Trigo 50 kg', 'preco': 250.00, 'quantidade': 20},
]

def adicionar_produto():
    try:
        codigo = int(input("Digite o código do produto: "))
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: ").replace(',', '.'))
        quantidade = int(input("Digite a quantidade: "))
    except ValueError:
        print("Entrada inválida. Tente novamente.\n")
        return

    produto = {'codigo': codigo, 'nome': nome, 'preco': preco, 'quantidade': quantidade}
    estoque.append(produto)
    print("Produto adicionado com sucesso!\n")

def listar_produtos():
    if not estoque:
        print("O estoque está vazio.\n")
        return

    print("\nProdutos no estoque:\n")
    for produto in estoque:
        print(f"Código: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Quantidade: {produto['quantidade']}")
        print("=-" * 20)
    print()

def remover_produto():
    if not estoque:
        print("O estoque está vazio.\n")
        return

    try:
        codigo = int(input("Digite o código do produto a remover: "))
    except ValueError:
        print("Código inválido.\n")
        return

    for produto in estoque:
        if produto['codigo'] == codigo:
            estoque.remove(produto)
            print(f"Produto com código {codigo} removido com sucesso.\n")
            return
    print(f"Produto com código {codigo} não encontrado.\n")

while True:
    print("--- Mercadinho do Bairro ---")
    print("1. Adicionar Produto")
    print("2. Listar Produtos")
    print("3. Remover Produto")
    print("4. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        remover_produto()
    elif opcao == "4":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
