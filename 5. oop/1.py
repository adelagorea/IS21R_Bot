class Dog:
    def __init__(self, name, age):
        """
        Inițializează un obiect Dog cu numele și vârsta date.

        :param name: Numele câinelui
        :param age: Vârsta câinelui
        """
        self.name = name
        self.age = age

    def bark(self):
        """
        Afișează un mesaj specific.
        """
        print(f"{self.name} spune: Ham Ham!")

# Testează clasa
dog = Dog("Rex", 5)
print(dog.name)  # Output: Rex
print(dog.age)   # Output: 5
dog.bark()       # Output: Rex spune: Ham Ham!
