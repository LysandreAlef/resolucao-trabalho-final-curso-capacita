def verificar_tipo_triangulo(a, b, c):
    if a == b == c:
        return "Triângulo Equilátero"
    elif a == b or a == c or b == c:
        return "Triângulo Isósceles"
    else:
        return "Triângulo Escaleno"


triangulos = [
    (5, 5, 5),  # Equilátero
    (3, 4, 4),  # Isósceles
    (3, 4, 5)   # Escaleno
]


for i, triangulo in enumerate(triangulos, start=1):
    a, b, c = triangulo
    tipo = verificar_tipo_triangulo(a, b, c)
    print(f"Triângulo {i}: {tipo}")