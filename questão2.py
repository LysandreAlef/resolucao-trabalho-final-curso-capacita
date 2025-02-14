aluno = input("Digite o nome do aluno: ")

nota1 = int(input("Digite a primeira nota deste aluno: "))

nota2 = int(input("Digite a segunda nota deste aluno: "))

nota3 = int(input("Digite a terceira nota deste aluno: "))

soma = nota1 + nota2 + nota3
divida = soma / 3

media = divida
if media >= 7:
    print(f"O aluno {aluno} está aprovado")
else:
    print(f"O aluno {aluno} está reprovado")