from tuote import Tuote
from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self):
        self._ostoskori = []
        self._hinta = 0
        self._maara = 0

    def tavaroita_korissa(self):
        return self._maara

    def hinta(self):
        return self._hinta

    def lisaa_tuote(self, lisattava: Tuote):
        onko_korissa = False
        ostos = Ostos(lisattava)
        for ostos_jo_korissa in self._ostoskori:
            if ostos_jo_korissa.tuotteen_nimi() == ostos.tuotteen_nimi():
                onko_korissa = True
                ### muuta tämä ostos.muuta_lukumaaraa(ostos.lukumaara)
        if not onko_korissa:
            self._ostoskori.append(ostos)
        self._maara += ostos.lukumaara()
        self._hinta += ostos.hinta()

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostoskori
