def adicionar_nome(nomes):
    nome = input("Digite o nome para adicionar: ")
    nomes.append(nome)
    print(f"Nome '{nome}' adicionado.")

def acessar_nomes(nomes):
    print("Lista de nomes:")
    for i, nome in enumerate(nomes, 1):
        print(f"{i}: {nome}")

def retirar_nome(nomes):
    acessar_nomes(nomes)
    indice = input("Digite o número do nome para retirar: ")
    if indice.isdigit():
        indice = int(indice)
        if 1 <= indice <= len(nomes):
            removido = nomes.pop(indice - 1)
            print(f"Nome '{removido}' removido.")
        else:
            print("Índice inválido.")
    else:
        print("Entrada inválida.")

def main():
    nomes = []
    while True:
        print("\nEscolha uma opção:")
        print("1 - Adicionar nome")
        print("2 - Acessar nomes")
        print("3 - Retirar nome")
        print("4 - Sair")
        opcao = input("Opção: ")

        match opcao:
            case "1":
                adicionar_nome(nomes)
            case "2":
                acessar_nomes(nomes)
            case "3":
                retirar_nome(nomes)
            case "4":
                print("Saindo...")
                break
            case _:
                print("Opção inválida.")