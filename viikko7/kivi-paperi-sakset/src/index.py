from kps import KPS

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        paatteet = ("a", "b", "c")

        if vastaus.endswith(paatteet):
            print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
            
            if vastaus.endswith("a"):
                peli = KPS.luo_pelaaja_vs_pelaaja_kps()
            elif vastaus.endswith("b"):
                peli = KPS.luo_tekoaly_kps()
            else:
                peli = KPS.luo_parempi_tekoaly_kps()
        else:
            break
        peli.pelaa()


if __name__ == "__main__":
    main()
