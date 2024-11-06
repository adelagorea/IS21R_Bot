class Animal:
    def __init__(self, name, species):
        """
        Inițializează un obiect Animal cu numele și specia date.

        :param name: Numele animalului
        :param species: Specia animalului
        """
        self.name = name
        self.species = species

class Cat(Animal):
    def __init__(self, name, species, color):
        """
        Inițializează un obiect Cat cu numele, specia și culoarea date.

        :param name: Numele pisicii
        :param species: Specia pisicii
        :param color: Culoarea pisicii
        """
        super().__init__(name, species)
        self.color = color

    def meow(self):
        """
        Afișează un mesaj specific.
        """
        print(f"{self.name} spune: Miau!")

# Testează clasele
cat = Cat("Whiskers", "Felina", "alb")
print(cat.name)    # Output: Whiskers
print(cat.species) # Output: Felina
print(cat.color)   # Output: alb
cat.meow()         # Output: Whiskers spune: Miau!
