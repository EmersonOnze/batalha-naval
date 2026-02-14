from tabuleiro import Tabuleiro
from navio import Navio

class Jogo:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.turno = 1

    def iniciar(self):
        # Colocando navios automaticamente
        self.tabuleiro.posicionar_navio(Navio(3), 1, 1, True)
        self.tabuleiro.posicionar_navio(Navio(2), 4, 3, False)

    def jogar(self):
        while not self.tabuleiro.todos_afundados():
            print(f"\nTurno {self.turno}")
            self.tabuleiro.mostrar()

            try:
                linha = int(input("Linha: "))
                coluna = int(input("Coluna: "))
                resultado = self.tabuleiro.atacar(linha, coluna)
                print(resultado)
                self.turno += 1
            except ValueError:
                print("Entrada inválida.")

        print("🎉 Todos os navios foram afundados!")
