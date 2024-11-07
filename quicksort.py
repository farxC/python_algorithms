def quicksort(arr):
    if (len(arr) <= 2):
        return arr
    else:
        pivo = arr[0] #O pivô pode ser qualquer elemento presente no array. No quicksort prezamos por bons pivôs
        
        menores = [i for i in arr[1:] if i <= pivo] #Levamos em conta da segunda posição a diante já que o pivô é o primeiro elemento, então sem necessidade de percorrermos novamente.
        
        maiores = [i for i in arr[1:] if i > pivo]
        
    return quicksort(menores) + [pivo] + quicksort(maiores)


print(quicksort([1,2,3,4,5,6,7,8]))

