from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._ostokset = {}

    def tavaroita_korissa(self):
        ostokset = list(self._ostokset.values())
        maara = map(lambda t: t.lukumaara(), ostokset)
        return sum(maara)
        
    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        ostokset = list(self._ostokset.values())
        hinta = map(lambda t: t.hinta, ostokset)
        return sum(hinta)

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        if lisattava in self._ostokset:
            self._ostokset[lisattava].muuta_lukumaaraa(1)
        else:
            self._ostokset[lisattava] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
