#!/usr/bin/env python3
"""
catraka.py

Funcionalidades existentes:
- Simulação de terminal de autoatendimento para compra de passagens de ônibus.
- Coleta de dados do usuário: nome, ano de nascimento, tipo de dia (útil ou fim de semana).
- Cálculo da idade e aplicação de descontos:
  * Idosos (65+) têm 40% de desconto.
  * Menores de idade (<18) têm 20% de desconto.
  * Promoção extra de 5% para usuários entre 18 e 25 anos em dia útil.
- Cálculo do custo total para quantidade desejada de passagens.
- Recebimento do valor pago e cálculo de troco.
- Decomposição do troco em menor número de notas e moedas (apenas moedas de R$1, R$0,50 e R$0,25).
- Emissão automática de recibo em arquivo .txt.
- Criação automática de pasta de recibos "Pasta-<usuário>".
- Numeração global sequencial de recibos, sem repetição mesmo entre usuários diferentes.
- Permite múltiplas compras pelo mesmo usuário até encerrar.

Alterações implementadas em agosto/2025:
- Adicionado uso de BASE_DIR para garantir que todos os arquivos e pastas (recibos, contador_global.txt)
  sejam salvos sempre na mesma pasta onde o catraka.py está armazenado, independente do diretório de execução.
"""

import os
from decimal import Decimal, ROUND_HALF_UP, getcontext
from typing import Dict

# Caminho base fixo para a pasta do script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Configurações / constantes
getcontext().prec = 9
YEAR_NOW = 2025
BASE_PRICE = Decimal("4.50")
DENOMINATIONS_CENTS = [
    10000, 5000, 2000, 1000, 500, 200,
    100, 50, 25
]
GLOBAL_COUNTER_FILE = os.path.join(BASE_DIR, "contador_global.txt")


def format_brl(valor: Decimal) -> str:
    s = f"{valor:,.2f}"
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {s}"


def ler_string(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Entrada inválida — por favor digite um texto não vazio.")


def ler_int_ano(prompt: str, min_year: int = 1900, max_year: int = YEAR_NOW) -> int:
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if v < min_year or v > max_year:
                print(f"Digite um ano entre {min_year} e {max_year}.")
                continue
            return v
        except ValueError:
            print("Entrada inválida — digite um número inteiro (ex: 1990).")


def ler_dia_tipo(prompt: str) -> str:
    while True:
        s = input(prompt).strip().lower()
        if s in ("util", "fds"):
            return s
        print('Entrada inválida — digite "util" para dia útil ou "fds" para fim de semana.')


def ler_int_positivo(prompt: str, min_value: int = 1) -> int:
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if v < min_value:
                print(f"Digite um número inteiro maior ou igual a {min_value}.")
                continue
            return v
        except ValueError:
            print("Entrada inválida — digite um número inteiro.")


def ler_money(prompt: str, min_value: Decimal = Decimal("0.00")) -> Decimal:
    while True:
        s = input(prompt).strip().replace(",", ".")
        try:
            d = Decimal(s)
            d = d.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            if d < min_value:
                print(f"Digite um valor maior ou igual a {format_brl(min_value)}.")
                continue
            return d
        except Exception:
            print("Entrada inválida — digite um valor monetário (ex: 10.50 ou 10,50).")


def calcular_idade(ano_nasc: int) -> int:
    return YEAR_NOW - ano_nasc


def aplicar_descontos(preco_base: Decimal, idade: int, dia: str) -> Decimal:
    preco = preco_base
    if idade >= 65:
        preco = preco_base * Decimal("0.60")
    elif idade < 18:
        preco = preco_base * Decimal("0.80")
    if dia == "util" and 18 <= idade <= 25:
        preco *= Decimal("0.95")
    return preco.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def decompor_troco(troco: Decimal) -> Dict[Decimal, int]:
    troco_cents = int((troco * 100).to_integral_value(rounding=ROUND_HALF_UP))
    resultado: Dict[Decimal, int] = {}
    for denom in DENOMINATIONS_CENTS:
        if troco_cents <= 0:
            break
        q = troco_cents // denom
        if q:
            valor_reais = Decimal(denom) / Decimal(100)
            resultado[valor_reais] = q
            troco_cents -= q * denom
    return resultado


def carregar_contador_global() -> int:
    if os.path.exists(GLOBAL_COUNTER_FILE):
        with open(GLOBAL_COUNTER_FILE, "r", encoding="utf-8") as f:
            return int(f.read().strip() or 0)
    return 0


def salvar_contador_global(valor: int):
    with open(GLOBAL_COUNTER_FILE, "w", encoding="utf-8") as f:
        f.write(str(valor))


def salvar_recibo(numero: int, pasta_usuario: str, nome: str, idade: int, quantidade: int, preco_unit: Decimal,
                   custo_total: Decimal, valor_pago: Decimal, troco: Decimal,
                   decomposicao: Dict[Decimal, int]):
    pasta_usuario_path = os.path.join(BASE_DIR, pasta_usuario)
    if not os.path.exists(pasta_usuario_path):
        os.makedirs(pasta_usuario_path)
    nome_arquivo = os.path.join(pasta_usuario_path, f"recibo_{numero:04d}.txt")
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("="*48 + "\n")
        f.write("RECIBO DE COMPRA\n")
        f.write("="*48 + "\n")
        f.write(f"Nome: {nome}\n")
        f.write(f"Idade: {idade} anos\n")
        f.write(f"Quantidade de passagens: {quantidade}\n")
        f.write(f"Valor unitário: {format_brl(preco_unit)}\n")
        f.write(f"Custo total: {format_brl(custo_total)}\n")
        f.write(f"Valor pago: {format_brl(valor_pago)}\n")
        f.write(f"Troco a receber: {format_brl(troco)}\n")
        if troco > Decimal("0.00"):
            f.write("\nDevolução do troco:\n")
            for denom in sorted(decomposicao.keys(), reverse=True):
                qtd = decomposicao[denom]
                tipo = "nota(s)" if denom >= Decimal("2.00") else "moeda(s)"
                f.write(f" - {qtd} {tipo} de {format_brl(denom)}\n")
        f.write("="*48 + "\n")
    print(f"Recibo salvo em {nome_arquivo}")


def main():
    print("=" * 60)
    print("Bem-vindo ao Terminal de Autoatendimento - Compra de Passagens")
    print("=" * 60)

    nome = ler_string("1) Digite seu nome completo: ")
    ano_nasc = ler_int_ano("2) Digite o ano de nascimento (ex: 1990): ")
    idade = calcular_idade(ano_nasc)
    pasta_usuario = f"Pasta-{nome.replace(' ', '_')}"

    contador_global = carregar_contador_global()

    while True:
        dia = ler_dia_tipo('\nCompra em dia "util" ou "fds"? (digite util ou fds): ')
        preco_unitario = aplicar_descontos(BASE_PRICE, idade, dia)

        print("\n--- Resumo ---")
        print(f"Idade: {idade} anos")
        print(f"Valor unitário da passagem: {format_brl(preco_unitario)}")

        quantidade = ler_int_positivo("Quantas passagens deseja comprar? (>=1): ", min_value=1)
        custo_total = (preco_unitario * Decimal(quantidade)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        print(f"Custo total: {format_brl(custo_total)}")

        valor_pago = ler_money("Insira o valor em dinheiro para pagar: ", min_value=Decimal("0.00"))

        if valor_pago < custo_total:
            falta = (custo_total - valor_pago).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            print("\n--- Pagamento insuficiente ---")
            print(f"Você inseriu {format_brl(valor_pago)}. Faltam {format_brl(falta)} para completar a compra.")
            print("Transação cancelada.")
        else:
            troco = (valor_pago - custo_total).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            print("\n" + "=" * 48)
            print(" " * 12 + "RECIBO DE COMPRA")
            print("=" * 48)
            print(f"Nome: {nome}")
            print(f"Idade: {idade} anos")
            print(f"Quantidade de passagens: {quantidade}")
            print(f"Valor unitário: {format_brl(preco_unitario)}")
            print(f"Custo total: {format_brl(custo_total)}")
            print(f"Valor pago: {format_brl(valor_pago)}")
            print(f"Troco a receber: {format_brl(troco)}")
            print("=" * 48)

            decomposicao = {}
            if troco > Decimal("0.00"):
                print("\nDevolução do troco:")
                decomposicao = decompor_troco(troco)
                for denom in sorted(decomposicao.keys(), reverse=True):
                    qtd = decomposicao[denom]
                    tipo = "nota(s)" if denom >= Decimal("2.00") else "moeda(s)"
                    print(f" - {qtd} {tipo} de {format_brl(denom)}")
            else:
                print("Sem troco a devolver.")

            contador_global += 1
            salvar_recibo(contador_global, pasta_usuario, nome, idade, quantidade, preco_unitario, custo_total, valor_pago, troco, decomposicao)
            salvar_contador_global(contador_global)

        continuar = input("\nDeseja fazer outra compra? (s/n): ").strip().lower()
        if continuar != 's':
            print("\nObrigado por usar o terminal. Boa viagem!")
            break


if __name__ == "__main__":
    main()
