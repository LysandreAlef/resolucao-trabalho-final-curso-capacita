# Função para ler o arquivo e obter os nomes
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            nomes = arquivo.readlines()  # Lê todas as linhas
        return [nome.strip() for nome in nomes]  # Remove espaços extras
    except FileNotFoundError:
        print("Arquivo não encontrado!")
        return []

# Função para ordenar os nomes em ordem alfabética
def ordenar_nomes(nomes):
    return sorted(nomes)

# Função para pegar apenas os nomes que começam com "A"
def filtrar_nomes_com_a(nomes):
    return [nome for nome in nomes if nome.lower().startswith("a")]

# Função para encontrar o maior nome da lista filtrada
def encontrar_maior_nome(nomes):
    if nomes:
        return max(nomes, key=len)  # Retorna o nome mais longo
    return "Nenhum nome encontrado."

# Função principal que chama as outras funções
def main():
    nome_arquivo = "nomes-questao7.txt"  # Nome do arquivo com a lista de nomes

    # Passo 1: Ler os nomes do arquivo
    lista_nomes = ler_arquivo(nome_arquivo)

    # Passo 2: Ordenar os nomes
    nomes_ordenados = ordenar_nomes(lista_nomes)

    # Passo 3: Filtrar os nomes que começam com "A"
    nomes_com_a = filtrar_nomes_com_a(nomes_ordenados)

    # Passo 4: Encontrar o maior nome entre os filtrados
    maior_nome = encontrar_maior_nome(nomes_com_a)

    # Passo 5: Exibir os resultados
    print("\nLista de Nomes Ordenada:")
    print("\n".join(nomes_ordenados))

    print("\nMaior nome que começa com 'A':")
    print(maior_nome)

# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    main()
