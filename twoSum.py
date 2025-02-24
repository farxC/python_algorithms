def twoSum(nums: list[int], target: int) -> list[int]:
    d = {}
    for i in range(len(nums)):
        # Complemento - Ex: 9 - 7 = 2 <- Necessário encontrar esse número
        complement = target - nums[i]
        if complement in d: # Se o complemento está no dicionário, retorne o elemento e o índice atual
            return [d.get(complement), i]
        else:
            d[nums[i]] = i # Armazena número e índice

    return []

twoSum([2,7,11,15], 9)