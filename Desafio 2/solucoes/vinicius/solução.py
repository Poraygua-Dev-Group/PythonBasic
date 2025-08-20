produtos = []

def adicionar_produto():
    nome = input("Nome do produto: ")
    try:
        codigo = int(input("Código do produto: "))
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Erro: Código, preço e quantidade precisam ser números. Tente novamente.")
        return

    produto = {"nome": nome, "codigo": codigo, "preco": preco, "quantidade": quantidade}
    produtos.append(produto)
    print("Produto adicionado com sucesso!")

def listar_produtos():
    if not produtos:
        print("Nenhum produto Cadastrado")
        return
    
    print("\nComo você deseja ordenar a lista?")
    print("1 - Ordem Alfabética (Nome)")
    print("2 - Maior para o Menor Preço")
    print("3 - Ordem de Cadastro (Padrão)")
    opcao_ordem = input("Escolha uma opção de ordenação (pressione Enter para padrão): ")

    lista_para_exibir = produtos

    if opcao_ordem == '1':
        lista_para_exibir = sorted(produtos, key=lambda p: p['nome'])
        print("\n--- Lista Ordenada por Nome ---")
    elif opcao_ordem == '2':
        lista_para_exibir = sorted(produtos, key=lambda p: p['preco'], reverse=True)
        print("\n--- Lista Ordenada por Preço ---")
    else:
        print("\n--- Lista por Ordem de Cadastro ---")
        
    for i, produto in enumerate(lista_para_exibir, 1):
        print(f"{i}. Produto: {produto['nome']}, Código: {produto['codigo']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}.")
    print()

def remover_produto():
    if not produtos:
        print("Nenhum produto para remover.")
        return
        
    print("\nLista de Produtos para Remoção:")
    for i, produto in enumerate(produtos, 1):
        print(f"{i}. {produto['nome']}")
    print()
        
    try:
        indice = int(input("Digite o número do produto que você deseja remover: "))
        if 1 <= indice <= len(produtos):
            removido = produtos.pop(indice - 1)
            print(f"Produto '{removido['nome']}' removido com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

def calcular_valor_total():
    if not produtos:
        print("Nenhum produto cadastrado para calcular o total.")
        return
    
    total = 0.0
    print("\nCalculando valor total do estoque...")

    for produto in produtos:
        try:
            total += produto['preco'] * produto['quantidade']
        except (ValueError, KeyError):
            print(f"Aviso: Produto '{produto.get('nome', 'Desconhecido')}' com dados inválidos foi ignorado no cálculo.")
    
    print(f"O valor total do estoque é: R$ {total:.2f}")
    print()


def menu():
    print("####################################")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Remover produto")
    print("4 - Calcular valor total no estoque")
    print("5 - Sair")


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        print() # Adiciona um espaço natural após a escolha do usuário

        match opcao:
            case "1":
                adicionar_produto()
            case "2":
                listar_produtos()
            case "3":
                remover_produto()
            case "4":
                calcular_valor_total()
            case "5":
                print("Até logo!...")
                break
            case _:
                print("Opção inválida.")
        
        print() # Adiciona um espaço antes de mostrar o menu novamente

if __name__ == "__main__":
    main()
