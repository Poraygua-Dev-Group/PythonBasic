import pandas as pd
ARQUIVO = "contatos.csv"

# Etapa 2: Funções de Arquivo
def carregar_contatos():
    """Carrega os contatos do arquivo CSV ou retorna lista vazia."""
    try:
        df = pd.read_csv(ARQUIVO)
        return df.to_dict(orient="records")
    except FileNotFoundError:
        return []
def salvar_contatos(lista_contatos):
    """Salva a lista de contatos no arquivo CSV."""
    df = pd.DataFrame(lista_contatos)
    df.to_csv(ARQUIVO, index=False)
# Funções do Sistema
def adicionar_contato(lista_contatos):
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    novo_contato = {"nome": nome, "telefone": telefone, "email": email}
    lista_contatos.append(novo_contato)
    salvar_contatos(lista_contatos)
    print(f"\n✅ Contato {nome} adicionado com sucesso!\n")
def listar_contatos(lista_contatos):
    if not lista_contatos:
        print("\n📭 Nenhum contato na lista.\n")
        return
    print("\n📒 Lista de Contatos:")
    for i, contato in enumerate(lista_contatos, start=1):
        print(f"{i}. {contato['nome']} | {contato['telefone']} | {contato['email']}")
    print()
def remover_contato(lista_contatos):
    email = input("Digite o email do contato que deseja remover: ")
    encontrado = False
    for contato in lista_contatos:
        if contato["email"] == email:
            lista_contatos.remove(contato)
            salvar_contatos(lista_contatos)
            print(f"\n🗑 Contato {contato['nome']} removido com sucesso!\n")
            encontrado = True
            break
    if not encontrado:
        print("\n Contato não encontrado.\n")
# Menu Principal

def menu():
    lista_contatos = carregar_contatos()

    while True:
        print("==== MENU AGENDA ====")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Remover contato")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_contato(lista_contatos)
        elif opcao == "2":
            listar_contatos(lista_contatos)
        elif opcao == "3":
            remover_contato(lista_contatos)
        elif opcao == "4":
            print("\n👋 Saindo do programa. Até mais!")
            break
        else:
            print("\n⚠ Opção inválida! Tente novamente.\n")

if _name_ == "_main_":
    menu()
