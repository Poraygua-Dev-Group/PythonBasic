# Programa de autoatendimento para a compra de passagens de ônibus

passagem = 4.50

nome = input("| Digite o seu nome completo: ")
nascimento = int(input("| Digite o ano de seu nascimento: "))
semana = input("| A compra está sendo feita em dia útil ou no fim de semana?\n| Digite 'util' para dia útil ou 'fds' para final de semana: ")

idade = 2025 - nascimento

if idade >= 65:
    valor_final = passagem * 0.60
elif idade < 18:
    valor_final = passagem * 0.80
else:     
    valor_final = passagem

if semana == "util" and 18 <= idade <= 25:
    valor_final = round((passagem * 0.95), 2)

print(f"\nO valor final da pasasagem individual é: {valor_final}")

quantidade = int(input("Quantas passagens você deseja comprar? "))
custo_total = round((valor_final * quantidade), 2)

print(f"\nO valor total da compra é igual a: {custo_total}")

dinheiro = float(input("Informe o valor que será usado para pagar a(s) passagem(ns): "))

if dinheiro < custo_total:
    print("ERRO. O valor informado é insuficiente.")
else:
    troco = round(dinheiro - custo_total,2)
    print("Sua passagem foi paga com sucesso")

print("\n##################  RECIBO  ##################")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"---------------------------------------------")
print(f"Valor unitário: {valor_final}")
print(f"Quantidade de passagens compradas: {quantidade}")
print(f"Custo total da transação: {custo_total}")
print(f"----------------------------------------------")
print(f"Valor usado para o pagamento: {dinheiro}")
print(f"Troco recebido: {troco}")
print(f"################## Troco: ###################")


if troco != 0:
    print(f"{int(troco // 100)} nota(s) de 100 reais")
    troco = troco % 100

    print(f"{int(troco // 50)} nota(s) de 50 reais")
    troco = troco % 50
   
    print(f"{int(troco // 20)} nota(s) de 20 reais")
    troco = troco % 20 
    
    print(f"{int(troco // 10)} nota(s) de 10 reais")
    troco = troco % 10

    print(f"{int(troco // 5)} nota(s) de 5 reais")
    troco = troco % 5

    print(f"{int(troco // 2)} nota(s) de 2 reais")
    troco = troco % 2

    print(f"{int(troco // 1)} moeda(s) de 1 real")
    troco = troco % 1

    print(f"{int(troco // 0.5)} moeda(s) de 50 centavos")
    troco = troco % 0.5

    print(f"{int(troco // 0.25)} moeda(s) de 25 centavos")
    troco = troco % 0.25

    print(f"{int(troco // 0.1)} moeda(s) de 10 centavos")
    troco = troco % 0.1

    print(f"{int(troco // 0.05)} moeda(s) de 5 centavos")
    troco = troco % 0.05
