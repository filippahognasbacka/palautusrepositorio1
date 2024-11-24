import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko()

    joukko.lisaa_taulukkoon(1)
    joukko.lisaa_taulukkoon(2)
    joukko.lisaa_taulukkoon(3)
    joukko.lisaa_taulukkoon(2)

    print(joukko.to_int_list())


if __name__ == "__main__":
    main()
