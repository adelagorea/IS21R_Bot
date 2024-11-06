class FormaGeometrica:
    def calcul_suprafata(self):
        pass  # Metoda care va fi suprascrisă în clasele derivate

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.latura = latura

    def calcul_suprafata(self):
        return self.latura * self.latura

class Dreptunghi(FormaGeometrica):
    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

    def calcul_suprafata(self):
        return self.lungime * self.latime

class Triunghi(FormaGeometrica):
    def __init__(self, baza, inaltime):
        self.baza = baza
        self.inaltime = inaltime

    def calcul_suprafata(self):
        return (self.baza * self.inaltime) / 2

# Funcție care primește o listă de forme geometrice și calculează suma suprafețelor acestora
def calcul_suma_suprafetelor(forme):
    suma = 0
    for forma in forme:
        suma += forma.calcul_suprafata()
    return suma

# Testăm funcționalitatea
patrat1 = Patrat(5)
dreptunghi1 = Dreptunghi(4, 6)
triunghi1 = Triunghi(3, 8)

forme = [patrat1, dreptunghi1, triunghi1]
print("Suma suprafețelor formelor geometrice este:", calcul_suma_suprafetelor(forme))
