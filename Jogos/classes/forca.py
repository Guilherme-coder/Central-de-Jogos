import random

class Forca:
    def __init__(self):
        self.erros = 0
        self.letra = ''
        self.trilha = ''
        self.acerto = False
        self.ganhou = False
        self.enforcou = False
        self.indice_aleatorio = random.randint(0, 28)
        #escolhe a palavra da vez
        self.palavra = self.escolhe_palavra(self.indice_aleatorio)

    def play(self):
        print('Jogando forca')
        print("Bem-vindo ao jogo da forca")
        
        #desenha a trilha da palavra
        self.trilha = self.desenha_trilha(self.palavra)
        self.trilha = list(self.trilha)

        print()

        while(not self.ganhou and not self.enforcou):
            #desenha o boneco da forca
            self.desenha_boneco(self.erros)
            print()

            self.formata_trilha(self.trilha)
            
            #captura a letra que o usuário digita e devolve uma cópia tratada
            chute = self.pega_chute()

            # verifica se a letra corresponde e insere a letra na trilha
            index = 0
            self.acerto = False
            for letra in self.palavra:
                resultado = letra == chute
                if(resultado):
                    self.trilha.pop(index)
                    self.trilha.insert(index, letra.upper())
                    self.acerto = True
                index += 1

            # se a letra não corresponder acrescenrta em 1 o numero de erros
            if (not self.acerto):
                self.erros += 1

            # verifica se o numero de erros chegou ao máximo e termina a partida    
            self.enforcou = self.verifica_derrota(self.erros, self.palavra)

            # verifica se a trilha já foi totalmente completa e termina a partida    
            self.ganhou = self.verifica_vitoria(self.trilha, self.palavra)           



    def formata_trilha(self, trilha):
        print('\t\t', end="")
        for letra in trilha:
            print(letra + " ", end="")
        print()
        print()


    def verifica_derrota(self, erros, palavra):
        if(erros == 6):
            self.desenha_boneco(erros)
            print("\n\nVocê se enforcou\n\n")
            print(f'A palavra era {palavra.title()}')
            return True
        return False

    def verifica_vitoria(self, trilha, palavra):
        for letra in trilha:
            if(letra == '_'):
                return False
        print("\n\n\n\nVocê Venceu!!!\n")
        print(f'A palavra era {palavra.capitalize()}\n')
        return True

    def pega_chute(self):
        letra = str(input('Digite uma letra: '))
        if(not letra.isalpha()):
            raise ValueError('Você precisa digitar uma letra')
            return ''
        if(len(letra) != 1):
            raise ValueError('Você precisa digitar apenas uma letra')
            return ''
        return letra.lower()

    def escolhe_palavra(self, indice):
        arquivo = open('./Palavras/palavras.txt', 'r')
        lista = arquivo.readlines()
        arquivo.close()
        return lista[indice].replace('\n', '')


    def desenha_trilha(self, palavra):
        trilha = ''
        print('Palavra:  ', end="")
        for trilha_palavra in palavra:
            if(trilha_palavra == '-'):
                trilha += '-'
                continue
            trilha += '_'
        return trilha


    def desenha_boneco(self, erros):
        if(erros == 0):
            print('\t  _________      ')
            print('\t  |/      |      ')
            print('\t  |       |      ')
            print('\t  |              ')
            print('\t  |              ')
            print('\t  |              ')
            print('\t  |              ')
            print('\t  |              ')
            print('\t  |              ')
            print('\t _|_             ')
        elif(erros == 1):
            print('\t  _________      ')
            print('\t  |/      |      ')
            print('\t  |       |      ')
            print('\t  |       0      ')
            print('\t  |              ')
            print('\t  |              ')
            print('\t  |              ')
            print('\t  |              ')
            print('\t  |              ')
            print('\t _|_             ')
        elif(erros == 2):
            print('\t  _________      ')
            print('\t  |/      |      ')
            print('\t  |       |      ')
            print('\t  |       0      ')
            print('\t  |       |      ')
            print('\t  |       |      ')
            print('\t  |              ')
            print('\t  |              ')
            print('\t  |              ')
            print('\t _|_             ')
        elif(erros == 3):
            print('\t  _________      ')
            print('\t  |/      |      ')
            print('\t  |       |      ')
            print('\t  |       0      ')
            print('\t  |      /|      ')
            print('\t  |       |      ')
            print('\t  |              ')
            print('\t  |              ')
            print('\t  |              ')
            print('\t _|_             ')
        elif(erros == 4):
            print('\t  _________      ')
            print('\t  |/      |      ')
            print('\t  |       |      ')
            print('\t  |       0      ')
            print('\t  |      /|\     ')
            print('\t  |       |      ')
            print('\t  |              ')
            print('\t  |              ')
            print('\t  |              ')
            print('\t _|_             ')
        elif(erros == 5):
            print('\t  _________      ')
            print('\t  |/      |      ')
            print('\t  |       |      ')
            print('\t  |       0      ')
            print('\t  |      /|\     ')
            print('\t  |       |      ')
            print('\t  |      /       ')
            print('\t  |              ')
            print('\t  |              ')
            print('\t _|_             ')
        elif(erros == 6):
            print('\t  _________      ')
            print('\t  |/      |      ')
            print('\t  |       |      ')
            print('\t  |       0      ')
            print('\t  |      /|\     ')
            print('\t  |       |      ')
            print('\t  |      / \     ')
            print('\t  |              ')
            print('\t  |              ')
            print('\t _|_             ')



if __name__ == "__main__":
    forca = Forca()
    forca.play()