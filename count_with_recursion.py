def count_with_recursion(list: list):
    if list == []:
        return 0
    return 1 + count_with_recursion(list[1:])


print(count_with_recursion([1]))

list = [1,2,3,4]
print(list[0:])