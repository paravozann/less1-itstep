class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand ):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers !=[]:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)

        else:
            print(f"тут нема нікого {self.brand}")

nick = Human("Nick")
sas = Human("Sas")

car = Auto("Merseders")
#car.add_passenger(nick)
car.add_passenger(sas)
car.print_passengers_names()
