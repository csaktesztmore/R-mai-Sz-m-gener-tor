class Szamkonventer:
    def __init__(self, alapszam, konvertalandoszam):
        self.alapszam = alapszam
        self.konvertalandoszam = konvertalandoszam

   #     def konvertalas(alapszam, konvertalandoszam):
#

arabszotar = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}
romaiszotar = {
    1:  "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}

def konverterArab(arab):
    pass
def konverterRomai(romai):
    szam = 0
    for i in romai:
        pass

konverterArab(int(input("adj egy arab számot és én átváltom romaiba")))
konverterRomai(str(input("adj egy romai számot és én átváltom arabba")))

