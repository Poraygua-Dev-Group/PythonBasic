# Lista original de cliques (coordenadas como tuplas)
cliques = [(120, 200), (135, 210), (120, 200), (400, 100), (135, 210)]

# 1. Função para obter os pontos únicos clicados
def pontos_unicos(cliques):
    return set(cliques)

# 2. Função para contar quantas vezes um ponto foi clicado
def contar_cliques(cliques, ponto):
    return cliques.count(ponto)

# 3. Função para verificar se um ponto específico foi clicado
def verificar_clique(cliques, ponto):
    return ponto in cliques

# 4. Função para desempacotar o primeiro clique
def primeiro_clique(cliques):
    if cliques:
        x, y = cliques[0]
        return x, y
    return None, None

# Execução das funções com print para mostrar os resultados
print("Pontos únicos clicados:", pontos_unicos(cliques))

ponto_alvo = (120, 200)
print(f"Quantidade de cliques em {ponto_alvo}:", contar_cliques(cliques, ponto_alvo))

ponto_verificar = (0, 0)
print(f"Ponto {ponto_verificar} foi clicado?", verificar_clique(cliques, ponto_verificar))

x, y = primeiro_clique(cliques)
print(f"Primeiro clique -> x: {x}, y: {y}")
