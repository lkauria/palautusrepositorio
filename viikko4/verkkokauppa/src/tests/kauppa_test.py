import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    # tähän tekisin def setUp(self), johon kaikki toisto, jos aikaa

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_koriin_tuote_jota_loytyy_varastosta_ja_ostetaan(self):
        # alustan ensin kaikille olioille mockin ja muutan tehtävän myötä
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock() 
        varasto_mock = Mock()

        # palautetaan aina arvo 1
        viitegeneraattori_mock.uusi.return_value = 1

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("Arto Vihavainen", "3425-1652")

        pankki_mock.tilisiirto.assert_called_with("Arto Vihavainen", ANY, "3425-1652", "33333-44455", 5)

    def test_ostoskoriin_kaksi_eri_tuotetta_joita_varastossa_suoritetaan_ostos(self):
        # alustettaan mockit, joita tarvitaan kauppaan
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock() 
        varasto_mock = Mock()

        # palautetaan aina arvo 1
        viitegeneraattori_mock.uusi.return_value = 1

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
        

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "jauhot", 2)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("Arto Vihavainen", "3425-1652")

        pankki_mock.tilisiirto.assert_called_with("Arto Vihavainen", ANY, "3425-1652", "33333-44455", 7)

    def test_ostoskoriin_kaksi_samaa_tuotetta_joita_varastossa_suoritetaan_ostos(self):
        # alustettaan mockit, joita tarvitaan kauppaan
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock() 
        varasto_mock = Mock()

        # palautetaan aina arvo 1
        viitegeneraattori_mock.uusi.return_value = 1

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
        

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("Arto Vihavainen", "3425-1652")

        pankki_mock.tilisiirto.assert_called_with("Arto Vihavainen", ANY, "3425-1652", "33333-44455", 10)

    def test_ostoskoriin_kaksi_eri_tuotetta_joista_toinen_loppunut_suoritetaan_ostos(self):
        # alustettaan mockit, joita tarvitaan kauppaan
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock() 
        varasto_mock = Mock()

        # palautetaan aina arvo 1
        viitegeneraattori_mock.uusi.return_value = 1

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 0
        

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "jauhot", 2)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("Arto Vihavainen", "3425-1652")

        pankki_mock.tilisiirto.assert_called_with("Arto Vihavainen", ANY, "3425-1652", "33333-44455", 5)
