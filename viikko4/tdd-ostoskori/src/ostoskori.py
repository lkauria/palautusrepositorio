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
        i = 0
        for ostos in self._ostoskori:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                maara = ostos.lukumaara()
                if maara > 1:
                    ostos.muuta_lukumaaraa(-1)
                if maara == 1:
                    self._ostoskori.pop(i)
            i += 1
        self._maara -= 1

    def tyhjenna(self):
        self._ostoskori.clear()
        self._maara = 0
        self._hinta = 0

    def ostokset(self):
        return self._ostoskori
