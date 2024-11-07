def sum_with_recursion(list: list):
    total = 0
    if (list == []):
        return  0
    return list[0] + sum_with_recursion(list[1:]) 

    

list = [2,4,6,10]

print(sum_with_recursion(list))