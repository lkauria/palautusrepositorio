from pickle import FALSE


HINTA = 5


class Kassapaate:
    def __init__(self):
        self.myytyja_lounaita = 0

    def lataa(self, kortti, summa):
        if summa > 0:
            kortti.lataa(summa)

    def osta_lounas(self, kortti):
        saldo = kortti.saldo
        if saldo >= HINTA:
            kortti.osta(HINTA)
            self.myytyja_lounaita = self.myytyja_lounaita + 1
        else:
            return FALSE
