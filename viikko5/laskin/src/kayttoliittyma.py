from enum import Enum
from tkinter import Tk, ttk, constants, StringVar



class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Summa:
    def __init__(self, sovelluslogiikka, syote_kentta):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote_kentta = syote_kentta
        self._viime_arvo = 0

    def suorita(self):
        self._viime_arvo = self._sovelluslogiikka.arvo()
        arvo = self._lue_syote()
        self._sovelluslogiikka.plus(arvo)

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._viime_arvo)

    def _lue_syote(self):
        try:
            return int(self._syote_kentta.get())
        except ValueError:
            return 0


class Erotus:
    def __init__(self, sovelluslogiikka, syote_kentta):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote_kentta = syote_kentta
        self._viime_arvo = 0

    def suorita(self):
        self._viime_arvo = self._sovelluslogiikka.arvo()
        arvo = self._lue_syote()
        self._sovelluslogiikka.miinus(arvo)

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._viime_arvo)

    def _lue_syote(self):
        try:
            return int(self._syote_kentta.get())
        except ValueError:
            return 0


class Nollaus:
    def __init__(self, sovelluslogiikka, syote_kentta):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote_kentta = syote_kentta
        self._viime_arvo = 0

    def suorita(self):
        self._viime_arvo = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.nollaa()

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._viime_arvo)


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root
        self._komennot = {}
        self._viime_komento = None

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=self._kumoa
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

        self._komennot = {
            Komento.SUMMA: Summa(self._sovelluslogiikka, self._syote_kentta),
            Komento.EROTUS: Erotus(self._sovelluslogiikka, self._syote_kentta),
            Komento.NOLLAUS: Nollaus(self._sovelluslogiikka, self._syote_kentta)
        }

    def _suorita_komento(self, komento):
        komento_olio = self._komennot.get(komento)
        if komento_olio:
            if komento != Komento.KUMOA:
                self._viime_komento = komento_olio
            komento_olio.suorita()

        if self._viime_komento:
            self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())

    def _kumoa(self):
        if self._viime_komento:
            self._viime_komento.kumoa()
            self._arvo_var.set(self._sovelluslogiikka.arvo())
            self._kumoa_painike["state"] = constants.DISABLED


