inicio = int(input("Entre com o número inicial da contagem: "))
fim = int(input("Entre com o número final da contagem: "))

if inicio < fim:
    while inicio <= fim:
        print(inicio)
        inicio += 1
else:
    print("O número inicial deve ser menor que o número final.")