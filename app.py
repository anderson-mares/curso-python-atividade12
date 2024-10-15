import math

# Definição das funções lambda para calcular as áreas
area_quadrado = lambda lado: lado ** 2
area_triangulo = lambda base, altura: (base * altura) / 2
area_circulo = lambda raio: math.pi * raio ** 2
area_trapezio = lambda base_maior, base_menor, altura: ((base_maior + base_menor) * altura) / 2

# Função principal para o cálculo da área
def calcular_area():
    print("Escolha a figura geométrica para calcular a área:")
    print("1. Quadrado")
    print("2. Triângulo")
    print("3. Círculo")
    print("4. Trapézio")
    
    escolha = input("Digite o número correspondente à figura: ")

    if escolha == '1':
        lado = float(input("Digite o valor do lado do quadrado: "))
        print(f"A área do quadrado é: {area_quadrado(lado):.2f}")
    elif escolha == '2':
        base = float(input("Digite o valor da base do triângulo: "))
        altura = float(input("Digite o valor da altura do triângulo: "))
        print(f"A área do triângulo é: {area_triangulo(base, altura):.2f}")
    elif escolha == '3':
        raio = float(input("Digite o valor do raio do círculo: "))
        print(f"A área do círculo é: {area_circulo(raio):.2f}")
    elif escolha == '4':
        base_maior = float(input("Digite o valor da base maior do trapézio: "))
        base_menor = float(input("Digite o valor da base menor do trapézio: "))
        altura = float(input("Digite o valor da altura do trapézio: "))
        print(f"A área do trapézio é: {area_trapezio(base_maior, base_menor, altura):.2f}")
    else:
        print("Opção inválida. Tente novamente.")

# Executar o programa
calcular_area()
