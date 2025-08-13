"""
esse exercicio é para demonstrar o uso de funções dentro de um programa,
passagem de argumentos e retorno de valores.
a ideia é criar uma calculadora simples que recebe dois números e uma operação,
e retorna o resultado da operação.
o programa deve lidar com erros de entrada, como divisão por zero ou entrada inválida.
"""


menu = """Escolha uma opção:
    - - subtrair
    + - somar
    * - multiplicar
    / - dividir
    0 - sair
Digite sua opção:
"""

try:
    numero1 = float(input("Digite o primeiro número: "))
    operacao = input(menu)
    numero2 = float(input("Digite o segundo número: "))
except ValueError:
    print("Erro: Por favor, digite apenas números válidos.")
    exit()


def subtrair(x, y):
    return x - y


def somar(x, y):
    return x + y


def multiplicar(x, y):
    return x * y


def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    return x / y


match operacao:
    case "-":
        resultado = subtrair(numero1, numero2)
    case "+":
        resultado = somar(numero1, numero2)
    case "*":
        resultado = multiplicar(numero1, numero2)
    case "/":
        resultado = dividir(numero1, numero2)
    case "0":
        resultado = "Saindo..."
    case _:
        resultado = "Operação inválida."

print(f"Resultado: {resultado}")
