import time

hora = time.localtime().tm_hour
dia_semana = time.localtime().tm_wday
ano_atual = time.localtime().tm_year
passagem = 4.50
# Algumas variáveis úteis futuramente

if hora >= 6 and hora <= 12:
    print ("Bom dia!\nFavor digitar seu nome e ano de nascimento")
elif hora > 12 and hora < 18:
    print ("Boa tarde!\nFavor digitar seu nome e ano de nascimento")
else:
    print ("Boa noite!\nFavor digitar seu nome e ano de nascimento")
#Aqui uma frescurinha pra saudar diferente dependendo do horário no relógio do terminal

nome = input("nome: ")
ano_nascimento = int(input("Ano de nascimento: "))
print ("--------------------------------------------------")

idade = ano_atual - ano_nascimento
if idade >= 65:
    passagem *= 0.6
elif idade < 18:
    passagem *= 0.8

if dia_semana <= 4 and idade >= 18 and idade <= 25:
    passagem *= 0.95
#no pdf  ele pressupoem que o usuário que compra em dia útil e tem entre 18 e 25 anos (inclusive), recebe outro desconto prévio "sobre o valor já calculado"
#sendo que ele somente recebe esse desconto de 5%, mas fiz como pedido no documento

if dia_semana == 0:
    dia_semana = "Segunda Feira"
elif dia_semana == 1:
    dia_semana = "Terça Feira"
elif dia_semana == 2:
    dia_semana = "Quarta Feira"
elif dia_semana == 3:
    dia_semana = "Quinta Feira"
elif dia_semana == 4:
    dia_semana = "Sexta Feira"
elif dia_semana == 5:
    dia_semana = "Sábado"
elif dia_semana == 6:
    dia_semana = "Domingo"
# Aqui eu automatizei o processo para saber se é dia útil ou fim de semana, não confio nesses usuários
# Só pude fazer isso agora por quê a variável dia_semana não pode estar em formato string na hora de definir o desconto ali em cima

passagem_arredondada = round(passagem, 2)
print (f"Seja bem vindo, {nome}!\nO valor individual da sua passagem deu um total de R${passagem_arredondada} \n Quantas passagens você gostaria de comprar?")

quantidade_passagens = int(input("Quantidade de passagens: "))
print ("--------------------------------------------------")

preço_total = round(quantidade_passagens * passagem_arredondada, 2)
print (f"O valor total deu R${preço_total}")

dinheiro_suado_do_usuario = float(input("Insira um valor em dinheiro para continuar com a compra: "))
print ("--------------------------------------------------")
if dinheiro_suado_do_usuario < preço_total:
    print ("     Erro\n Saldo insuficiente")
elif dinheiro_suado_do_usuario == preço_total:
    print ("Compra finalizada com sucesso\nAguarde a emissão do seu recibo")
    print ("--------------------------------------------------")
    print (f"Vinícius's Transportes - Transportando desde 2025\nNome: {nome}       Idade: {idade}\nQuantidade de Passagens: {quantidade_passagens}  Valor da passagem: {passagem_arredondada}\nPreço total: {preço_total}     Valor recebido: {dinheiro_suado_do_usuario}\n{dia_semana} - {hora} horas")
elif dinheiro_suado_do_usuario > preço_total:
    print ("Aguarde seu troco")
#aqui eu separo a mensagem final para cada caso, se não tem saldo suficiente pra compra e se precisa ou não de troco

    troco_total = round(dinheiro_suado_do_usuario - preço_total, 2)
    troco = round(dinheiro_suado_do_usuario - preço_total, 2)
    
    nota_100 = troco // 100
    troco = troco % 100
    nota_50 = troco // 50
    troco = troco % 50
    nota_20 = troco // 20
    troco = troco % 20
    nota_10 = troco // 10
    troco = troco % 10
    nota_5 = troco // 5
    troco = troco % 5
    nota_2 = troco // 2
    troco = troco % 2
    nota_1 = troco // 1
    troco = troco % 1
    nota_05 = troco // 0.5
    troco = troco % 0.5
    nota_025 = troco // 0.25
    troco = troco % 0.25
    nota_010 = troco // 0.1
    troco = troco % 0.10
    nota_005 = troco // 0.05
    troco = troco % 0.05
# Isso aqui deu trabalho, meu amigo me desafiou a fazer sem lista, quebrei a cabeça por horas

    print (f" {nota_100} nota(s) de R$100\n {nota_50} nota(s) de R$50\n {nota_20} nota(s) de R$20\n {nota_10} nota(s) de R$10\n {nota_5} nota(s) de R$5\n {nota_2} nota(s) de R$2\n {nota_1} moeda(s) de R$1\n {nota_05} moeda(s) de R$0,50\n {nota_025} moeda(s) de R$0,25\n {nota_010} moeda(s) de R$0,10\n {nota_005} moeda(s) de R$0,05")
    print ("--------------------------------------------------")

    print ("Compra finalizada com sucesso\nAguarde a emissão do seu recibo")
    print ("--------------------------------------------------")
    print (f"Vinícius's Transportes   -   Transportando desde 2025\nNome: {nome}          Idade: {idade}\nQuantidade de Passagens: {quantidade_passagens}   Valor da passagem: {passagem_arredondada}\nPreço total: {preço_total}   Valor recebido: {dinheiro_suado_do_usuario}   Troco: {troco_total}\n{dia_semana} - {hora} horas")

# Aconteceu algo bem engraçado, se você colocar alguem com idade acima de 65 anos, que quer 17 passagens e que vai dar 50 reais para pagar
# o algoritmo reconhece a quantidade correta de troco a ser dado, mas por problema na forma como o python armazena informação,  ele vai dar o troco errado
# Aparentemente quando chega na linha 92 ele diz que 4.1 % 2 é 0,09999...
# por conta disso ele acaba dando apenas uma moeda de 5 centavos ao invés de uma de 10 centavos
