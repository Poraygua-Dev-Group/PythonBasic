#Estrutura do Projeto e dos Dados

import pandas as pd
import os

lista_contatos = [
    {
        'nome': 'Ronaldo Silva',
        'telefone': '912283-2634',
        'email': 'ronaldosilva@gmail.com'
    },
    {
        'nome': 'Luiza Costa',
        'telefone': '913055-7256',
        'email': 'luizacosta@gmail.com'
    }
]

#Funções Para a Manipulação dos Arquivos

def carregar_contatos():
    try:
        if os.path.exists('contatos.csv'):
            df = pd.read_csv('contatos.csv', encoding='utf-8')
            return df.to_dict(orient='records')
        else:
            return []
    except FileNotFoundError:
        print('Arquivo contatos.csv não encontrado.')

def salvar_contatos(lista_contatos):
    df = pd.DataFrame(lista_contatos) #transformei o dicionário em Dataframe
    df.to_csv('contatos.csv', index=False, encoding='utf-8')
    
#Etapa 3: Funções do Núcleo da Aplicação
def adicionar_contato(lista_contatos):
    print('Digite suas informações para criar o contato:')

    nome = input('Infome seu nome: ').title()
    telefone = input('Informe seu telefone: ')
    email = input('Informe seu email: ')

    novo_contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }

    lista_contatos.append(novo_contato)

    print('Contato adicionado com sucesso!')

def listar_contatos(lista_contatos):
    if not lista_contatos:
        return []

    print('\nLista de Contatos:')
    for contato in lista_contatos:
        print(f"Nome: {contato['nome']} | Contato: {contato['telefone']} | E-mail: {contato['email']}")

def remover_contato(lista_contatos):
    contato_removido = input('Qual email deseja remover? ')

    for contato in lista_contatos:
        if contato['email'] == contato_removido:
            lista_contatos.remove(contato)
            print('Contato removido com sucesso!')
            return
    
    print('Não foi possível remover pois a lista está vazia.')

def menu():
    carregar_contatos()
    while True:
        print('\n---------- Sistema de Gestão de Contatos -----------')
        print("1 - Adicionar Contato")
        print("2 - Listar Contatos")
        print("3 - Remover Contato")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_contato(lista_contatos)
            salvar_contatos(lista_contatos)
        elif opcao == '2':
            listar_contatos(lista_contatos)
        elif opcao == '3':
            remover_contato(lista_contatos)
            salvar_contatos(lista_contatos)
        else:
            print('Saindo do Sistema...')
            break

menu()
