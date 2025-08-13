# Programa de gerenciamento de tarefas usando dicionários

tarefas = []

def adicionar_tarefa():
    nome = input("Nome da tarefa: ")
    descricao = input("Descrição da tarefa: ")
    tarefa = {"nome": nome, "descricao": descricao}
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!\n")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
        return
    print("Lista de tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. Nome: {tarefa['nome']}, Descrição: {tarefa['descricao']}")
    print()

def remover_tarefa():
    listar_tarefas()
    if not tarefas:
        return
    try:
        indice = int(input("Digite o número da tarefa para remover: "))
        if 1 <= indice <= len(tarefas):
            removida = tarefas.pop(indice - 1)
            print(f"Tarefa '{removida['nome']}' removida com sucesso!\n")
        else:
            print("Índice inválido.\n")
    except ValueError:
        print("Por favor, digite um número válido.\n")

def acessar_tarefa():
    listar_tarefas()
    if not tarefas:
        return
    try:
        indice = int(input("Digite o número da tarefa para acessar: "))
        if 1 <= indice <= len(tarefas):
            tarefa = tarefas[indice - 1]
            print("Detalhes da tarefa:")
            for chave, valor in tarefa.items():
                print(f"{chave.capitalize()}: {valor}")
            print()
        else:
            print("Índice inválido.\n")
    except ValueError:
        print("Por favor, digite um número válido.\n")

def menu():
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Acessar tarefa")
    print("5 - Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                adicionar_tarefa()
            case "2":
                listar_tarefas()
            case "3":
                remover_tarefa()
            case "4":
                acessar_tarefa()
            case "5":
                print("Saindo...")
                break
            case _:
                print("Opção inválida!\n")
