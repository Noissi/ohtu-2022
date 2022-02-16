KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.taulukko = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        if n in self.taulukko:
            return True
        return False

    def lisaa(self, n):
        if not self.kuuluu(n):
            if self.alkioiden_lkm == len(self.taulukko):
                self.taulukko = self.taulukko + [0] * self.kasvatuskoko
            self.taulukko[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True
        return False

    def poista(self, n):
        if self.kuuluu(n):
            self.taulukko.remove(n)
            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True
        return False

    def mahtavuus(self):
        return self.alkioiden_lkm
    
    def luvut(self):
        return self.taulukko[0:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        yhdiste = a

        for luku in b.luvut():
            yhdiste.lisaa(luku)

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        luvut = list(set(a.luvut()).intersection(b.luvut()))

        for luku in luvut:
            leikkaus.lisaa(luku)

        return leikkaus

    @staticmethod
    def erotus(a, b):
        yhdiste = a

        for luku in b.luvut():
            yhdiste.poista(luku)

        return yhdiste

    def __str__(self):
        luvut_str = map(str, self.luvut())
        return "{" + ", ".join(luvut_str) + "}"
