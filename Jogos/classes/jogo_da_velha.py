import random
class Jogo_da_velha:
    def __init__(self):
        self.cerquilha = ['\n\t', ' ', '|', ' ', '|', ' ', '\n', '      ','---------', '\n', '\t', ' ', '|', ' ', '|', ' ', '\n', '      ','---------', '\n', '\t', ' ', '|', ' ', '|', ' ', '\n\n']
        self.oponente_jogou = False
        #faz a seleção aleatória do primeiro a jogar
        self.jogador = random.randint(1, 2)
        self.acabou = False


    def play(self):
        while(not self.acabou):
            self.imprime_cerquilha()

            if(self.jogador % 2 == 0):
                print('\n>>>Sua vez<<<')
                self.linha = int(input('Digite a linha que você vai jogar: '))
                self.coluna = int(input('Digite a coluna que você vai jogar: '))
                self.valida_linha_e_coluna(self.linha, self.coluna)
                self.indice = self.pega_posicao(self.linha, self.coluna)
                #verifica se a posição está vazia
                if(not self.vazia(self.indice)):
                    print('Você deve ocupar uma posição vazia.')
                    continue
                self.marca_na_cerquilha(self.indice, 'X')
                self.jogador += 1
            self.verifica_quem_ganhou()
            if(self.verifica_velha()):
                self.acabou = True
                break


            if(self.jogador % 2 == 1):
                print('\n>>>Vez do computador<<<')
                self.linha_oponente = random.randint(1, 3)
                self.coluna_oponente = random.randint(1, 3)
                self.valida_linha_e_coluna(self.linha_oponente, self.coluna_oponente)
                self.indice = self.pega_posicao(self.linha_oponente, self.coluna_oponente)
                if(not self.vazia(self.indice)):
                    continue
                self.marca_na_cerquilha(self.indice, 'O')
                self.jogador += 1
            self.verifica_quem_ganhou()
            if(self.verifica_velha()):
                self.acabou = True
                break



    def imprime_cerquilha(self):
        for pedaco in self.cerquilha:
            print(pedaco, end='')
    
    def valida_linha_e_coluna(self, linha, coluna):
        if(linha < 1 or coluna < 1):
            raise ValueError('Você precisa digitar linhas e colunas entre 1 e 3.')
    
    #verifica se a posição está vazia
    def vazia(self, indice):
        if(self.cerquilha[indice] != ' '):
            return False
        return True

    #transforma a coordenada que o jogador inseriu n indice correspondente do array
    def pega_posicao(self, linha, coluna):
        if(linha == 1 and coluna == 1):
            return 1
        if(linha == 1 and coluna == 2):
            return 3
        if(linha == 1 and coluna == 3):
            return 5
        if(linha == 2 and coluna == 1):
            return 11
        if(linha == 2 and coluna == 2):
            return 13
        if(linha == 2 and coluna == 3):
            return 15
        if(linha == 3 and coluna == 1):
            return 21
        if(linha == 3 and coluna == 2):
            return 23
        if(linha == 3 and coluna == 3):
            return 25
    
    #marca a jogada na cerquilha
    def marca_na_cerquilha(self, indice, simbolo):
        self.cerquilha.pop(indice)
        self.cerquilha.insert(indice, simbolo)
        

    #faz a varredura na cerquilha verificando as linhas possiveis para vencer
    def verifica_quem_ganhou(self):
        self.analisa_trecho(1, 3, 5)
        self.analisa_trecho(11, 13, 15)
        self.analisa_trecho(21, 23, 25)
        self.analisa_trecho(1, 11, 21)
        self.analisa_trecho(3, 13, 23)
        self.analisa_trecho(5, 15, 25)
        self.analisa_trecho(1, 13, 25)
        self.analisa_trecho(5, 13, 21)

    #verifica se ha uma linha vitoriosa
    def analisa_trecho(self,pos1, pos2, pos3):
        if(self.cerquilha[pos1].find('X') != -1 and self.cerquilha[pos2].find('X') != -1 and self.cerquilha[pos3].find('X') != -1):
            print('\n\nParabéns, você ganhou\n\n')
            self.imprime_cerquilha()
            self.acabou = True
        elif(self.cerquilha[pos1].find('O') != -1 and self.cerquilha[pos2].find('O') != -1 and self.cerquilha[pos3].find('O') != -1):
            print('\n\nO computador venceu\n\n')
            self.imprime_cerquilha()
            self.acabou = True
    
    #verifica se não há mais casas restantes
    def verifica_velha(self):
        for pedaco in range(1, 25):
            if (self.cerquilha[pedaco] == ' '):
                return False
        print('\n\n')
        self.imprime_cerquilha()
        print('O jogo deu velha\n\n')
        return True
