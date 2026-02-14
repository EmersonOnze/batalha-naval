class Navio:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.posicoes = []
        self.acertos = 0

    def registrar_acerto(self):
        self.acertos += 1

    def afundado(self):
        return self.acertos >= self.tamanho
