class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen_tulos = 0

    def miinus(self, arvo):
        self.aseta_edellinen()
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.aseta_edellinen()
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.aseta_edellinen()
        self.tulos = 0

    def kumoa(self):
        self.aseta_arvo(self.edellinen_tulos)

    def aseta_arvo(self, arvo):
        self.tulos = arvo

    def aseta_edellinen(self):
        self.edellinen_tulos = self.tulos