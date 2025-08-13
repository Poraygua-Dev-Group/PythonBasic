def buscar_nome(nome_procurado, arquivo='nomes.txt'):
    with open(arquivo, 'r', encoding='utf-8') as f:
        if arquivo == '' or not nome_procurado:
            print("Arquivo ou nome não informado.")
        else:
            encontrado = False
            
            
            for linha in f:
                if nome_procurado == linha.strip():
                    encontrado = True
                    break
                
            if encontrado:
                print(f'O nome "{nome_procurado}" foi encontrado na lista.')
            else:
                print(f'O nome "{nome_procurado}" NÃO foi encontrado na lista.')

nome = input("Digite o nome que deseja procurar: ")
buscar_nome(nome)