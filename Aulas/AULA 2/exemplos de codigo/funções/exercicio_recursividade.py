"""
a ideia é demonstrar o uso de recursividade dentro de uma função, ela executa uma contagem regressiva
que começa a partir do número passado como argumento e vai até 0.
o uso da condicional 'if' é para garantir que a função não entre em um loop infinito,
caso o número seja negativo, a função não será chamada novamente.
"""

def contagem_regressiva(numero: int) -> None:
    if numero >= 0:
        print(numero)
        contagem_regressiva(numero - 1)


print("Iniciando contagem...")
contagem_regressiva(5)
print("Fim da contagem.")