def binary_search(lista, item):
    low = 0 #Menor item possível (na memória).
    high = len(lista) - 1 #Posição na memória do vetor // Último elemento da Lista
   
    while low <= high:
        middle = (low + high) // 2 # O meio sempre será a soma de low (0) + high (no exemplo do array 1, 14), dividido por 2 (0+14) // 2 = 7 <- POSIÇÃO, NÃO O VALOR, DENTRO DO ARRAY.
        n = lista[middle] # Chute, decisão, fator. 
    
        if n == item: 
            return print(middle)
        if n > item: # É maior? 
            high = middle - 1 # É necessário acrescentar ou diminuir dentro da posição do Array na busca binária justamente pelo fato de que, sabendo-se que 
                              # o elemento de busca não é o meio e é ou alto/baixo a partir desse ponto, logo a posição imediata a tal (para baixo ou para alto)
                              # é a posição mais 'segura' de se continuar na busca.
        else: # É menor?
            low = middle + 1
    return None 
    

array_list= []

for i in range(0,10000000):
    array_list.append(i)

array1 = [0,1,2,3,4,5,6,7,8,9]
array2 = [2,3,4,4,5,6,7,8,9,10,28]


binary_search(array_list, 450)
