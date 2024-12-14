
from tekoaly_parannettu import TekoalyParannettu
from tekoaly import Tekoaly

class KiviPaperiSakset:
    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)


        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        raise Exception("Tämä metodi pitää korvata aliluokassa")

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmaisen_siirto):
        return input("Toisen pelaajan siirto: ")


class KPSTekoaly(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmaisen_siirto):
        tekoaly = Tekoaly()
        return tekoaly.anna_siirto()


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self, muistin_koko):
        self.tekoaly = TekoalyParannettu(muistin_koko)


    def _toisen_siirto(self, ensimmaisen_siirto):
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        return self.tekoaly.anna_siirto()