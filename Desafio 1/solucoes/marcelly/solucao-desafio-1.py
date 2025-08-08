print('Olá! Seja bem vindo ao Autoatendimento de Mobilidade Urbana de Belém!\nPara continuar o seu atendimento, precisamos que você insira algumas informações:')

#Etapa 1: Coleta de dados
nome_completo = input('\nInsira seu nome completo: ')
ano_de_nascimento = int(input('Insira seu ano de nascimento: '))
dia_da_compra = input('Sua compra está sendo feita em um dia útil ou no fim de semana? (Digite "util" para dia útil ou "fds" para fim de semana): ')


#Etapa 2: Lógica de Preços e Descontos
idade_do_usuario = 2025 - ano_de_nascimento

preco_base = 4.50
if(idade_do_usuario >= 65):
    preco_final = preco_base * (1 - 0.40) #eu coloco o preco final para atualizar o preco base.
elif(idade_do_usuario < 18):
    preco_final = preco_base * (1 - 0.20)
else:
    preco_final = preco_base


if(dia_da_compra == 'util' and 18 <= idade_do_usuario <= 25):
    preco_final = preco_final * (1 - 0.05)


#Etapa 3: Transação e Pagamento
print(f'O valor final de sua passagem será de R$ {preco_final:.2f}')
quantidade_de_passagens = int(input('Quantas passagens você deseja comprar? '))

custo_total = preco_final * quantidade_de_passagens

valor_inserido = float(input('Insira o valor em dinheiro para o seu pagamento: R$ '))

if(valor_inserido < custo_total):
    print('O valor inserido é insuficiente para o pagamento da passagem.')

troco = valor_inserido - custo_total
    

#Etapa 4: Recibo Final
print('\n--------------RECIBO-----------------')
print(f'Nome: {nome_completo}')
print(f'Idade: {idade_do_usuario} anos')
print(f'Quantidade de passagens compradas: {quantidade_de_passagens}')
print(f'Valor unitário da passagem: R$ {preco_final:.2f}')
print(f'Custo total: R$ {custo_total:.2f}')
print(f'Valor pago: R$ {valor_inserido:.2f}')
print(f'Troco: R$ {troco:.2f}')
print('--------------------------------------')