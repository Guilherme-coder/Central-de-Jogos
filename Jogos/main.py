from classes.adivinha import Adivinha
from classes.forca import Forca
from classes.jogo_da_velha import Jogo_da_velha

print('****************************')
print('Bem-vindo à central de jogos')
print('****************************')
sair = False

while(not sair):
    print('Digite o jogo que você deseja: \n')
    print('(1) Adivinha\n(2) Forca\n(3) Jogo da Velha\n >>> ', end="")
    jogo = int(input())
    print()

    
    

    if(jogo == 1):
        adivinha = Adivinha()
        adivinha.play()
    elif(jogo == 2):
        forca = Forca()
        forca.play()
    elif(jogo == 3):
        jogo_da_velha = Jogo_da_velha()
        jogo_da_velha.play()
    else:
        raise ValueError("Você precisa digitar o índice do jogo que você quer jogar.")
    saida = input('\nSe quiser sair da central digite alguma letra: ')
    if(saida.isalpha()):
        sair = True
    