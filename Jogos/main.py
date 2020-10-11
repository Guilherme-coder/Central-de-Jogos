from classes.adivinha import Adivinha
from classes.forca import Forca

print('****************************')
print('Bem-vindo à central de jogos')
print('****************************')
sair = False

while(not sair):
    print('Digite o jogo que você deseja: \n')
    print('(1) Adivinha\n(2) Forca\n >>> ', end="")
    jogo = int(input())
    print()

    adivinha = Adivinha()
    forca = Forca()

    if(jogo == 1):
        adivinha.play()
    elif(jogo == 2):
        forca.play()
    else:
        raise ValueError("Você precisa digitar o índice do jogo que você quer jogar.")
    print('\nSe quiser sair da central digite alguma letra: ', end='')
    saida = input()
    if(saida.isalpha()):
        sair = True
    