# informações  basicas
print('\nOlá seja bem vindo,o preço da passagem é R$ 4,50 para verificar se você tem direito a desconto digite as informações abaixos\n')
nome = input('Digite seu nome: \n').capitalize()
ano = int (input('Digite seu ano de nascimento:  \n'))
dia = input('Se a compra for feita em fim de semana, digite ""fds"",\n Se for feita em dia da semana, digite ""util""  ').lower()
idade_usuario = int ( 2025 - ano)
preco_passagem = 4.5
passagem_ind = preco_passagem
#preço, promoção e desconto da passagem
if idade_usuario >= 65:
     print("Você é elegivel para  receber um desconto de 40% do valor base\n")
     passagem_ind = preco_passagem *0.6
elif 18 > idade_usuario:
  print("Você é elegivel para receber um 20% desconto sobre o valor base\n")
  passagem_ind = preco_passagem *0.8
else:
  print("Você não é elegivel  para receber um desconto\n")
if 18 <= idade_usuario <= 25 and dia == 'util' :
  print("Você é elegivel para receber um desconto de 5% sobre o valor base\n")
  passagem_ind = preco_passagem * 0.95
# transação e pagamento
print(f"{nome}, o preço final da sua passagem foi de R$ {passagem_ind:.2f}\n")
quant = int(input("por favor, informe a quantidade de passagens que você irá comprar: \n"))
total_compra = passagem_ind+ (quant*4.5)
print(f" {nome}, o valor total da compra ficou em: R$ {total_compra:.2f}\n")
pagamento = float(input("Por favor, insira o valor de pagamento para finalizar a compra:  \n"))
if pagamento >= passagem_ind + quant*4.5:
  print(f"Valor suficiente, seu troco é: {pagamento-total_compra:.2f}")
  #recibo
  print(f"{10*'x'}Recibo{10*'x'}")
  print(
      f" NOME = {nome.capitalize()} \n IDADE = {idade_usuario} /nQUANTIDADE DE PASSAGEM = {quant} \n VALOR UNITARIO = {passagem_ind}/n CUSTO TOTAL = {total_compra} \n "
      f"VALOR PAGO = {pagamento}\n TROCO = {pagamento - total_compra}")
else :
    print(f"valor insuficiente, adicione mais {total_compra - pagamento} para efetuar a compra")
