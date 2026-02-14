class Tabuleiro:
    def __init__(self, tamanho=8):
        self.tamanho = tamanho
        self.grade = [["~" for _ in range(tamanho)] for _ in range(tamanho)]
        self.navios = []

    def dentro_limite(self, linha, coluna):
        return 0 <= linha < self.tamanho and 0 <= coluna < self.tamanho

    def posicionar_navio(self, navio, linha, coluna, horizontal=True):
        for i in range(navio.tamanho):
            l = linha
            c = coluna + i if horizontal else coluna
            if not horizontal:
                l = linha + i

            if not self.dentro_limite(l, c) or self.grade[l][c] != "~":
                return False

        for i in range(navio.tamanho):
            l = linha
            c = coluna + i if horizontal else coluna
            if not horizontal:
                l = linha + i

            self.grade[l][c] = "N"
            navio.posicoes.append((l, c))

        self.navios.append(navio)
        return True

    def atacar(self, linha, coluna):
        if not self.dentro_limite(linha, coluna):
            return "Inválido"

        if self.grade[linha][coluna] == "N":
            self.grade[linha][coluna] = "X"

            for navio in self.navios:
                if (linha, coluna) in navio.posicoes:
                    navio.registrar_acerto()
                    if navio.afundado():
                        return "Afundou!"
                    return "Acertou!"

        elif self.grade[linha][coluna] == "~":
            self.grade[linha][coluna] = "O"
            return "Água!"

        return "Já atacado"

    def todos_afundados(self):
        return all(navio.afundado() for navio in self.navios)

    def mostrar(self):
        for linha in self.grade:
            print(" ".join(linha))
