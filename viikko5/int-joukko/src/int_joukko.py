KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self._validoi_kapasiteetti(kapasiteetti)
        self.kasvatuskoko = self._validoi_kasvatuskoko(kasvatuskoko)
        self.luvut = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    @staticmethod
    def _validoi_kapasiteetti(kapasiteetti):
        if kapasiteetti is None:
            return KAPASITEETTI
        if not isinstance(kapasiteetti, int) or kapasiteetti <= 0:
            raise ValueError("Väärä kapasiteetti")
        return kapasiteetti

    @staticmethod
    def _validoi_kasvatuskoko(kasvatuskoko):
        if kasvatuskoko is None:
            return OLETUSKASVATUS
        if not isinstance(kasvatuskoko, int) or kasvatuskoko <= 0:
            raise ValueError("kapasiteetti2")
        return kasvatuskoko
        
    @staticmethod
    def _luo_lista(koko):
        return [0] * koko


    def kuuluu_taulukkoon(self, luku):
        return luku in self.luvut[:self.alkioiden_lkm]

    def lisaa_taulukkoon(self, luku):
        if not self.kuuluu_taulukkoon(luku):
            if self.alkioiden_lkm == len(self.luvut):
                self.kasvata_taulukkoa()
            self.luvut[0] = luku
            self.luvut[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1
            return True
        return False


    def poista_taulukosta(self, luku):
        try:
            indeksi = self.luvut.index(luku, 0, self.alkioiden_lkm)
        except ValueError:
            return False
        self.siirra_vasemmalle(indeksi)
        self.alkioiden_lkm -= 1
        return True

    def kasvata_taulukkoa(self):
        uusi_koko = len(self.luvut) + self.kasvatuskoko
        uusi_taulukko = self._luo_lista(uusi_koko)
        for i in range(self.alkioiden_lkm):
            uusi_taulukko[i] = self.luvut[i]
        self.luvut = uusi_taulukko


    def siirra_vasemmalle(self, alkaen):
        for i in range(alkaen, self.alkioiden_lkm -1):
            self.luvut[i] = self.luvut[i+1]
        self.luvut[self.alkioiden_lkm -1] = 0

    def mahtavuus(self): 
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.luvut[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()
        for luku in a.to_int_list() + b.to_int_list():
            tulos.lisaa_taulukkoon(luku)
        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        for luku in a.to_int_list():
            if b.kuuluu_taulukkoon(luku):
                tulos.lisaa_taulukkoon(luku)
        return tulos


    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        for luku in a.to_int_list():
            if not b.kuuluu_taulukkoon(luku):
                tulos.lisaa_taulukkoon(luku)
        return tulos


    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.luvut[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.luvut[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.luvut[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
