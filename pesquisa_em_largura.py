from collections import deque

grafo = {}

grafo["voce"] = ["alice", "bob", "claire"]

grafo["bob"] = ["annuj", "peggy"]

grafo["alice"] = ["peggy"]

grafo["claire"] = ["thom", "jonny"]

grafo["annuj"] = []

grafo["peggy"] = []

grafo ["thom"] = []

grafo["jonny"] = []


def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'




def pesquisa_em_largura(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []
    contador = 0
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:

            if (pessoa_e_vendedor(pessoa)):
                print (pessoa + " é um vendededor de Manga!", "Teve que procurar:", contador)
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
                contador +=1 
    return False

pesquisa_em_largura("voce")

print(grafo)