

#Grafo completo mapeado.
grafo={}
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2


grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5 

grafo["fim"] = {}


#Tabela Hash de Custos
infinito = float("inf")
custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito #Não sabemos até o momento o custo final.


#Tabela dos pais *necessário para identificar o caminho pai em relação ao nodo tendo em consideração o custo.

pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] =  None

# Manter o registro de todos os vértices processados
processados = []


def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None

    for nodo in custos:
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
        return nodo_custo_mais_baixo

def dijkstraAlg():

    # Nodo a ser processado -> Vértice atual
    nodo = ache_no_custo_mais_baixo(custos)
    while nodo is not None:
        custo = custos[nodo] # ->> Evidencia o valor
        vizinhos = grafo[nodo] # ->> Evidencia os outros vértices ao redor do nodo escolhido
        for n in vizinhos.keys(): # Percorre todos os vizinhos == BIG O(N)
            novo_custo = custo + vizinhos[n] # Soma o custo do nodo atual mais o vizinho percorrido.
            if custos[n] > novo_custo: # Caso o vizinho seja mais barato a partir desse vértice ..
                custos[n] = novo_custo # Logo o custo atualiza e fica com o valor somado ao vértice vizinho 
                pais[n] = nodo # O vértice atual se torna o pai para o vizinho, visto que foi percorrido.
            print(custos['fim']) # Valor mais baixo para o fim do grafo.
        processados.append(nodo) # Adiciona ao vetor que checa os vértices que já foram vistos.
        nodo = ache_no_custo_mais_baixo(custos) # Encontra um novo nodo e repete


print(dijkstraAlg())
    
