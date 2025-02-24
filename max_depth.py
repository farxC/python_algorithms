"""
Exercício 03 – Profundidade Máxima de Listas Aninhadas (Recursividade) - (tempo aproximado 15 a 20 min)

Objetivo:
Crie uma função recursiva chamada `max_depth` que receba uma 
lista e retorne a profundidade máxima de aninhamento de sublistas.

Requisitos:
1. Se a lista não contiver nenhuma sublista, retorne 1.
2. Se houver sublistas, a profundidade da lista será 1 + a maior profundidade encontrada entre as sublistas.
3. Considere que apenas elementos do tipo lista devem ser tratados como níveis de aninhamento.

Exemplos:
    - max_depth([1, 2, 3]) deve retornar 1.
    - max_depth([1, [2, 3], 4]) deve retornar 2.
    - max_depth([1, [2, [3, 4]], 5]) deve retornar 3.

Dicas:
    - Utilize a função `isinstance(x, list)` para verificar se um elemento é uma lista.
    - Percorra cada elemento da lista e, se for uma sublista, chame recursivamente a função `max_depth`.

Escreva sua solução abaixo.
"""


def max_depth(arr: list, index = 0, max_depth_value = 1):
    if index == len(arr):
        return max_depth_value
    if isinstance(arr[index], list):
        sublist_depth = max_depth(arr[index], 0, max_depth_value + 1)
        max_depth_value = max(max_depth_value, sublist_depth)
    
    return max_depth(arr,index + 1, max_depth_value)

    

case1 = max_depth([1,2,3])
case2 = max_depth([1, [2, 3], 4])
case3 = max_depth([1, [2, [3,4]], 5])

print("Caso 1:", case1) #Correct result
print("Caso 2:", case2) #Correct result
print("Caso 3:", case3) #Correct result