#O reduce transforma o array em um simples item.
from functools import reduce


arr = [3,5,6,7]
arr_with_reduce = int(reduce(lambda x, y: x+y, arr))

print(arr_with_reduce)

mentira = False
print(not not mentira)