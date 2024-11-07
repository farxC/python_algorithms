"""
    Desafio 2!
    Classificação de Triângulos com Tratamento de Erros
    Escreva um programa que peça ao usuário para inserir três valores correspondentes aos
    lados de um triângulo. O programa deve usar estruturas condicionais para:
    • Verificar se os valores formam um triângulo válido.
    • Classificar o triângulo como equilátero, isósceles ou escaleno.
    • Caso os valores não formem um triângulo válido (ex.: um dos lados é maior que
    a soma dos outros dois), o programa deve exibir uma mensagem de erro.
    Desafio extra: Implemente validações para garantir que apenas números positivos sejam
    aceitos.
"""


def CheckIfNegative(*numbers):
    isPositive = True
    for number in numbers:
        if number < 0:
            isPositive = False
    
    return isPositive

def CheckIfValid(a,b,c):
    return a + b > c and a + c > b and b + c > a


def classOfTriangles(a,b,c):
    classes = {
        "Equilátero": a == b == c,
        "Isósceles": b == c !=a or a == b != c,
        "Escaleno": a != b and b != c and a != c
    }

    if(CheckIfNegative(a,b,c)):
        print("Todos são positivos..")
        if(CheckIfValid(a,b,c)):
            print("É um triângulo válido...")
            for tClass, cond in classes.items():
                if(cond):
                    print("É um triângulo", tClass)
        else:
            raise TypeError("Não é um triângulo válido.")
    else:
         raise TypeError("Algum desses números é negativo.")


s1 = float(input("Insira o primeiro lado do triângulo: "))
s2 = float(input("Insira o segundo lado do triângulo: "))
s3 = float(input("Insira o terceiro lado do triângulo: "))

classOfTriangles(s1,s2,s3)