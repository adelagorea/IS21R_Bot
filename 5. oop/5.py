class Engine:
    def __init__(self, horsepower, type):
        """
        Inițializează un obiect Engine cu puterea și tipul date.

        :param horsepower: Puterea motorului
        :param type: Tipul motorului
        """
        self.horsepower = horsepower
        self.type = type

class Car:
    def __init__(self, make, model, engine):
        """
        Inițializează un obiect Car cu marca, modelul și un obiect Engine.

        :param make: Marca mașinii
        :param model: Modelul mașinii
        :param engine: Obiect Engine
        """
        self.make = make
        self.model = model
        self.engine = engine

    def car_details(self):
        """
        Afișează detaliile mașinii și ale motorului.
        """
        print(f"Mașină: {self.make} {self.model}")
        print(f"Motor: {self.engine.horsepower} CP, {self.engine.type}")

# Testează clasele
engine = Engine(300, "V8")
car = Car("Ford", "Mustang", engine)
car.car_details()
# Output:
# Mașină: Ford Mustang
# Motor: 300 CP, V8
