class Clasa1:
    def __init__(self, marca, tip):
        self.marca = marca
        self.tip = tip

    def accepta_culoare(self, culoare):
        self.culoare = culoare

    def AfisareCuloare(self):
        print("Culoarea masinii este:", self.culoare)


class Clasa2(Clasa1):
    def adauga_scaune_incalzite(self, scaune_incalzite):
        self.scaune_incalzite = scaune_incalzite


class Clasa3(Clasa1):
    def adauga_blocuri_optice_led(self, blocuri_optice_led):
        self.blocuri_optice_led = blocuri_optice_led


obiect1 = Clasa2("ARO", "M461")
obiect1.adauga_scaune_incalzite("Nu")
obiect1.accepta_culoare("Rosu")
obiect2 = Clasa3("Dacia", "1310")
obiect2.adauga_blocuri_optice_led("Nu")
obiect2.accepta_culoare("Negru")
print(obiect1.culoare)
print(obiect1.scaune_incalzite)
print(obiect1.marca)
print(obiect1.tip)
print(obiect2.culoare)
print(obiect2.blocuri_optice_led)
print(obiect2.marca)
print(obiect2.tip)
