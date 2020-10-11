import random
class Adivinha:
    def __init__(self):
        self.tentativas = 0
        self.numero = random.randint(0, 500)
        self.lista = []
        self.derrota = False
        self.acertou = False


    def play(self):
        #inicio da jogo de adivinhação 
        print('\nO jogo consiste em você acertar o número secreto que está entre 0 e 500\n')
        print('Em qual a dificuldade que você deseja jogar?')
        print(' (1) Fácil **Tens 10 tentativas pra adivinhar\n (2) Médio **Tens 7 tentativas pra adivinhar\n (3) Difícil **Tens 5 tentativas pra adivinhar\n (4) Improvável **Tens 3 tentativas pra adivinhar')
        jogo = int(input('>>> '))
        
        #seleciona a dificudade
        if (jogo == 1):
            self.tentativas = 10
        elif (jogo == 2):
            self.tentativas = 7
        elif (jogo == 3):
            self.tentativas = 5
        elif (jogo == 4):
            self.tentativas = 3
        else:
            raise ValueError("Você não selecionou uma dificuldade válida")
        
        print()
        
        #desenha as tentativas restantes
        self.lista = self.desenha_lista(self.tentativas)

        while(not self.acertou and not self.derrota): 
            #imprime as tentativas
            self.imprime_lista()
            num = int(input('\nDigite o número que quer chutar: '))
            print()
            if (self.checa_valor(num)):
                continue
            #verifica se o chute é igual ao numero secreto
            if(self.checa_numero(num, self.numero)):
                print('\nVOCÊ VENCEU!!!\n\n')
                self.acertou = True

            #verifica se o numero de tentativas restantes chegou a zero
            self.derrota = self.derrota_total(self.tentativas)


  
    def derrota_total(self, tentativa):
        if(tentativa == 0):
            print(f'O número era {self.numero}')
            return True
        return False

    def checa_numero(self, numero, numero_secreto):
        #verifica se o chute é igual ao número secreto
        if(numero == self.numero):
            return True
        else:
            self.tentativas -= 1
            if(numero > numero_secreto):
                print('O número que você chutou é maior que o número secreto.')
            else:
                print('O número que você chutou é menor que o número secreto.')
                return False

    def checa_valor(self, num):
        if (num > 500 or num < 0):
            print("Vocẽ precisa inserir um número entre 0 e 500")
            return True
        return False
   
    def desenha_lista(self, dificuldade):
        #desenha as tentativas restantes
        lista = []
        for lis in range(dificuldade):
                lista.append(' | ') 
        return lista
    
    def imprime_lista(self):
        #imprime as tentativas
        print('Tentativas >> ', end='')
        for lis in range(self.tentativas):
            print(self.lista[lis], end="")


if(__name__ == "__main__"):
    adivinha = Adivinha()
    adivinha.play()