KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = KAPASITEETTI
        self.kasvatuskoko = OLETUSKASVATUS

        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        for i in range(self.alkioiden_lkm):
            if n == self.ljono[i]:

                return True

        return False

    def lisaa(self, n):
        if not self.kuuluu(n):          
            self.ljono[self.alkioiden_lkm] = n  
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm % len(self.ljono) == 0: 
                self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)  

            return True

        return False

    def poista(self, n):
        kohta = -1

        for i in range(self.alkioiden_lkm): 
            if n == self.ljono[i]:         
                kohta = i  
                break

        if kohta != -1:     
            for j in range(kohta, self.alkioiden_lkm - 1):  
                self.ljono[j] = self.ljono[j + 1]       

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            
            return True

        return False

    def alkioiden_lukumaara(self):
        return self.alkioiden_lkm

    def palauta_jono(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.palauta_jono()
        b_taulu = b.palauta_jono()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.palauta_jono()
        b_taulu = b.palauta_jono()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.palauta_jono()
        b_taulu = b.palauta_jono()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
