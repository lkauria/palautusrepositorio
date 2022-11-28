import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisays_ostoskorissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        kahvi = Tuote("Kahvi", 13)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kahvi)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_summa(self):
        maito = Tuote("Maito", 3)
        kahvi = Tuote("Kahvi", 13)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kahvi)

        self.assertEqual(self.kori.hinta(), 16)

    def test_kahden_saman_tuotteen_lisays_ostoskorissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_summa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        kahden_maidon_hinta = 2 * maito.hinta()
        self.assertEqual(self.kori.hinta(), kahden_maidon_hinta)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(self.kori._ostoskori), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.hinta(), 3)
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")

    # tämä testi on toistoa toisesta, mutta pyydettiin kahdesti?
    def test_kahden_eri_tuotteen_lisays_ostoskorissa_kaksi_tavaraa_2(self):
        maito = Tuote("Maito", 3)
        kahvi = Tuote("Kahvi", 13)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kahvi)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)