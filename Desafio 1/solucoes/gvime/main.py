
#CONSTANTE COM O PRECO DA PASSAGEM
#(PYTHON NAO TEM "CONSTANTS", ENTAO E USADO
#A CONVENSAO DE NOMECLATURA "SCREAMING SNAKE CASE":
#TODAS AS LESTRAS EM MAIUSCULO COM
#PALAVRAS SEPARADAS POR UNDERLINE)
PRECO_PASSAGEM = 4.5


#COMO A MENSAGEM DE SAIDA E SEMPRE A MESMA E
#SERA USADA MAIS DE UMA VEZ, E INTERESSANTE
#SALVA-LA NUMA VARIAVEL
mensagemSaida = "Obrigado por utilizar nosso sistema!\n Saindo..."

continuar = True
while continuar:

    print("--------------------------------------------------------------------")
    print("Bem vindo ao sistema! Preencha seus dados para comprar sua passagem.")
    print("Preencha com -1 a qualquer momento para cancelar.")
    print("--------------------------------------------------------------------")

    nome = input("Digite seu nome: ")
    try:
        if int(nome) == -1:
            print(mensagemSaida)
            break
    except ValueError:
        print("Ola, ", nome)

    #E UTILIZADO WHILE TRUE E TRATAMENTO DE EXCESSAO
    #PARA LIDAR COM CASOS EM QUE O USUARIO INSERE
    #OPCOES INVALIDAS

    print()

    while True:
        try:
            anoNasc = int(input("Digite seu ano de nascimento (somente numeros): "))
            break
        except ValueError:
            print("Preenchimento incorreto! Digite somente numeros!")

    if anoNasc == -1:
        print(mensagemSaida)
        break

    print()

    while True:
        diaSemana = input('Hoje e dia util? (S para "sim" ou N para "nao": ')
        if (diaSemana.lower() == "s" or diaSemana.lower() == "n") or (int(diaSemana) == -1):
            break
        print("Entrada incorreta!")
        print('Digite "S" para "sim" ou "N" para "nao" ou "-1" para sair.')

    if diaSemana.lower() == 's':
        diaSemana = True
    elif diaSemana.lower() == 'n':
        diaSemana = False
    elif int(diaSemana) == -1:
        print(mensagemSaida)
        break

    idade = 2025 - anoNasc

    if idade >= 65:
        desconto = 0.4
    elif idade < 18:
        desconto = 0.2
    else:
        desconto = 0

    preco = (1 - desconto) * PRECO_PASSAGEM
    if diaSemana and (18 <= idade <= 25):
        preco *= 0.95

    print()
    print("Preço da passagem: ", round(preco, 2))
    print()

    while True:
        continuar = input("Deseja continuar? (S/N): ")
        if continuar.lower() == "n" or (int(continuar) == -1):
            print(mensagemSaida)
            continuar = False
            break
        elif continuar.lower() == "s":
            continuar = True
            break
        else:
            print("Opcao invalida!")
            print()
