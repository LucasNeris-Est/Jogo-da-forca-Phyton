import random
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


class Homemforca:
    def __init__(self,palavra):
        self.palavra=palavra
        self.letras_adv=[]
        self.letras_err=[]
    def advinhar(self,letra):
        if letra in self.palavra and letra not in self.letras_adv:
            self.letras_adv.append(letra)
        elif letra not in self.palavra and letra not in self.letras_err:
            self.letras_err.append(letra)
        else: return False
        return True
    def interface(self,p_escondida):
        print(board[len(self.letras_err)])
        print('A palavra é:'+p_escondida)
        print('\nErradas:',self.letras_err)
        print('\nCertas:',self.letras_adv)

    def esconder(self):
        p_escondida=''
        for letra in self.palavra:
            if letra in self.letras_adv:
                p_escondida+=letra
            else: p_escondida+='_'
        return p_escondida
    def fim(self,p_escondida):
        if '_' not in p_escondida: return False
        elif len(self.letras_err) == 6: return False
        else:return True

def p_aleatoria():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

def main():
    jogo=Homemforca(p_aleatoria())

    while jogo.fim(jogo.esconder()):
        jogo.interface(jogo.esconder())
        entrada=input('\nDigite uma letra:')
        jogo.advinhar(entrada)

    jogo.interface(jogo.esconder())
    if jogo.palavra==jogo.esconder():
        print("\nVocê ganhouu!!")
    else:
        print('Você perdeu.. a palavra era '+ jogo.palavra)


if __name__ == "__main__":
    main()

