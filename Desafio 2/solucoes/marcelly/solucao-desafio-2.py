#Etapa 1: Estruturando os Dados

estoque = [
    {'codigo': 1, 'nome': 'Café', 'preco': 20.00, 'quantidade': 80}, 
    {'codigo': 2, 'nome': 'Macarrão Espaguete', 'preco': 13.90, 'quantidade': 100}, 
    {'codigo': 3, 'nome': 'Açúcar', 'preco': 5.49, 'quantidade': 150},
    {'codigo': 4, 'nome': 'Óleo de Soja', 'preco': 7.80, 'quantidade': 200}
]

#Etapa 2: Modularizando Funções

def adicionar_produto(codigo, nome, preco, quantidade):
    produto = {
        'codigo': codigo,
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }

    estoque.append(produto)
    print('Produto adicionado com sucesso!')

def listar_produtos():
    if not estoque:
        print('O estoque está vazio')
        return
    
    #Listagem Ordenada com Lambda
    print('\nComo você deseja ordenar a lista de produtos?')
    print('1 - Por nome')
    print('2 - Por preço')
    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        estoque_ordenado = sorted(estoque, key=lambda produto:produto['nome'])
    elif escolha == '2':
        estoque_ordenado = sorted(estoque, key=lambda produto: produto['preco'])
    else:
        print('Opção inválida, listando produtos sem ordenação...')
        estoque_ordenado = estoque

    print('\nLista de Produtos:')
    for produto in estoque_ordenado:
        print(f"Cód: {produto['codigo']} | Produto: {produto['nome']} | Preço: R$ {produto['preco']:.2f} | Qtd: {produto['quantidade']}")
    
def remover_produto(codigo):
    for produto in estoque:
        if produto['codigo'] == codigo:
            estoque.remove(produto)
            print(f"Produto {produto['nome']} removido com sucesso!")
            return

    print(f'Produto com o código {codigo} não encontrado.')

#Função Calcular Valor Total
def calcular_valor_total():
    valor_total = sum(produto['preco'] * produto['quantidade'] for produto in estoque)
    print(f'Valor total do estoque R$ {valor_total:.2f}')

#Etapa 3: Menu Interativo
def main():
    while True:
        print('\n------------ Mercearia do Bairro -----------------')
        print("1 - Adicionar Produto")
        print("2 - Listar Produtos")
        print("3 - Remover Produto")
        print("4 - Ver valor total do estoque")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            codigo = int(input('Digite o código do produto: '))
            nome = input('Digite o nome do produto: ').capitalize()
            preco = float(input('Digite o preço do produto: R$ '))
            quantidade = int(input('Digite a quantidade em estoque do produto: '))
            adicionar_produto(codigo, nome, preco, quantidade)
            
        elif opcao == '2':
            listar_produtos()

        elif opcao == '3':
            codigo = int(input('Insira o código do produto que deseja remover: '))
            remover_produto(codigo)

        elif opcao == '4':
            calcular_valor_total()

        elif opcao == '5':
            print('Saindo do Sistema....')
            break

        else:
            print('Insira uma opção válida')

main()