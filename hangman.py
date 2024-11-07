# Jogo da forca
# TO DO... REFATORAR UTILIZANDO RECURSIVIDADE.
# Se a condição for verdadeira, vai retornar o valor atual da lista + índice.
# O caso base é se a palavra foi acertada ou se as chances acabaram (enforcado)

def returnUnderList(word: str):
    list = ["_" for letter in word]
    return list

def checkLetter(letter: str, word: str):
   return True if letter in word else False


def hangman(chances):
    hit = hanged = False
    secret_word = 'Banana'.upper()
    list_under_score = returnUnderList(secret_word)
    while not hit and not hanged:
        print(list_under_score)
        choosed_letter = input("Por favor insira uma letra: ").upper()
        found = checkLetter(choosed_letter, secret_word)
        if found:
            print("Você acertou")
            for i, letter in enumerate(secret_word):
                if choosed_letter == letter:
                    list_under_score[i] = letter 
        else:
            print("Você errou")
            chances -=1

          
        if list_under_score == list(secret_word):             
            print(list_under_score)
            hit = True
        if chances <= 0:
            hanged = True
            

hangman(4)
