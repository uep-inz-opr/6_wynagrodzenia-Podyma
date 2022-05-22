i = int(input())

class Pracownik: 
  def __init__(self, pracownik, brutto):
    self.pracownik = pracownik
    self.brutto=int(brutto)

  def obliczenia(self):

  #Wysokosc_skladek_pracodwaca  
    emerytalna_pracodawca = 0.0976 * self.brutto
    rentowa_pracodawca = 0.065 * self.brutto 
    wypadkowa = 0.0193 * self.brutto
    FP = 0.0245 * self.brutto
    FGSP = 0.001 * self.brutto
    składki_pracodawca = round(emerytalna_pracodawca,2) + round(rentowa_pracodawca,2) + round(wypadkowa,2) + round(FP,2) + round(FGSP, 2)

  #Skladki_pracownik  
    emerytalna_pracownik = 0.0976 * self.brutto
    rentowa_pracownik = 0.015 * self.brutto
    chorobowa_pracownik = 0.0245 * self.brutto
    składki_pracownik = round(emerytalna_pracownik,2) + round(rentowa_pracownik,2) + round(chorobowa_pracownik,2) #c

    ubezpieczenie_zdrowotne_pracownik = 0.09 * (self.brutto - składki_pracownik) #e
    ubezpieczenie_zdrowotne_do_odliczenia_z_podatku = 0.0775 * (self.brutto - składki_pracownik) #f
    koszty_uzyskania_przychodu = 111.25 #g

    podstawa_do_obliczenia_podatku = self.brutto - round(składki_pracownik,2) - round(koszty_uzyskania_przychodu,2) #h

    zaliczka_podatek_przed_odliczeniem_składki_zdrowotnej = round(podstawa_do_obliczenia_podatku) * 0.18 - 46.33 #i

    zaliczka_podatek_do_pobrania = round(zaliczka_podatek_przed_odliczeniem_składki_zdrowotnej,2) - round(ubezpieczenie_zdrowotne_do_odliczenia_z_podatku,2) #j

    netto = self.brutto - round(składki_pracownik,2) - round(ubezpieczenie_zdrowotne_pracownik,2) - round(zaliczka_podatek_do_pobrania)

  #koszt_pracodawcy
    self.koszt_pracodawcy = self.brutto + składki_pracodawca
    

    return(self.pracownik + " {:.2f} {:.2f} {:.2f}").format(netto, składki_pracodawca, self.koszt_pracodawcy)
    #return(self.pracownik, ' ', f"{netto:.2f}", ' ', f"{składki_pracodawca:.2f}", ' ', f"{koszt_pracodawcy:.2f}")

  def get_laczny_koszt(self):
    return self.koszt_pracodawcy

laczny_koszt=0.00
lista_wynikow=[]
for i in range(0, i):
    dane_pracownika = input().split(" ")
    pracownik = Pracownik(dane_pracownika[0], dane_pracownika[1])
    lista_wynikow.append(pracownik.obliczenia())
    laczny_koszt += pracownik.get_laczny_koszt()

for wynik in lista_wynikow:
    print(wynik)
    
print(("{:.2f}").format(laczny_koszt))