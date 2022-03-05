from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

class KPS:
    @staticmethod
    def luo_pelaaja_vs_pelaaja_kps():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def luo_tekoaly_kps():
        return KPSTekoaly()

    @staticmethod
    def luo_parempi_tekoaly_kps():
        return KPSParempiTekoaly()

    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)
            
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
      return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"


# luokka perii luokan KPS
class KPSPelaajaVsPelaaja(KPS):
    # toteutetaan metodi pelityypin mukaisesti
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")

        return tokan_siirto

class KPSTekoaly(KPS):
    def __init__(self):
        self._tekoaly = Tekoaly()
    
    # toteutetaan metodi pelityypin mukaisesti
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")

        return tokan_siirto

class KPSParempiTekoaly(KPS):
    def __init__(self):
        self._tekoaly = TekoalyParannettu(10)
        self._eka_siirto = True
    
    # toteutetaan metodi pelityypin mukaisesti
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")
        
        if self._eka_siirto:
            self._eka_siirto = False
        else:
            self._tekoaly.aseta_siirto(ensimmaisen_siirto)

        return tokan_siirto