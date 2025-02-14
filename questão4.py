salario = 1500
porcentagem = 11

def desconto (salario, porcentagem):
    return (porcentagem / 100) * salario

resultado = desconto(1500, 11)
print(f"Será descontando {porcentagem}% dos {salario} reais, vai dar o valor em real de {int(resultado)} reais")