from ast import Str
import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto_deux = Varasto(-1, -1)
        self.varasto_kolme = Varasto(2, 1)


    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_kontruktori_korjaa_negatiivisen_tilavuuden(self):
        self.assertAlmostEqual(self.varasto_deux.tilavuus, 0.0)

    def test_konstruktori_korjaa_negatiivisen_saldon(self):
        self.assertAlmostEqual(self.varasto_deux.saldo, 0.0)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertAlmostEqual(self.varasto_kolme.saldo, 1)

    def test_konstruktori_ei_aseta_tilavuutta_suurempaa_saldoa(self):
        self.varasto = Varasto(2, 3)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_lisays_ei_lisaa_negatiivista(self):
        self.varasto = Varasto(4, 2)
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 2)

    def test_lisays_lisaa_maksimimaaran_jos_liian_iso(self):
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ala_ota_negatiivista_varastosta(self):
        self.varasto = Varasto(5,1)
        palautusarvo= self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(palautusarvo, 0.0)
    
    def test_ota_kaikki_varastosta(self):
        self.varasto = Varasto(5,2)
        self.varasto.ota_varastosta(6)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str_toimii_oikein(self):
        self.varasto = Varasto(5, 2)
        merkkijonoesitys = str(self.varasto)
        self.assertEqual(merkkijonoesitys, "saldo = 2, vielä tilaa 3")