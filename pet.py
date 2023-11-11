import random
class Animal:
    def __init__(self, name):        self.name = name
        self.gladness = 50        self.alive = True
        self.progress = 1
    def to_play(self):        print("time to play")
        self.progress += 0.5        self.gladness += 7
    def to_sleep(self):
        print("time to sleep")        self.gladness += 3
        self.progress -= 0.7
    def to_eat(self):        print("time to eat!")
        self.gladness += 0.4        self.progress += 0.5
    def is_alive(self):
        if self.progress < -0.5:            print("Cast out")
            self.alive = False        elif self.gladness <= 0:
            print("Depression...")            self.alive = False
        elif self.progress > 29:            print("///")
            self.alive = False
    def end_of_day(self):        print(f"gladness = {self.gladness}")
        print(f"progress = {round(self.progress)}")
    def live(self, day):        day = "Day" + str(day) + "of " + self.name + "life"
        print(f"{day:=^50}")        live_cube = random.randint(1, 3)
        if live_cube == 1:            self.to_play()
        elif live_cube == 2:            self.to_sleep()
        elif live_cube == 3:            self.to_eat()
        self.end_of_day()
        self.is_alive()pyshok = Animal("Pyshok")
for day in range(365):    if pyshok.alive == False:
        break    pyshok.live(day)