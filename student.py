
import random

class Student:
    print("Hi, I'm a student")
    def __init__(self):
        self.alive = True
        self.name = name
        self.gladness = 50
        self.progress = 0

    def to_study(self):
        print("time to study")
        self.progress += 0.2
        self.gladness -= 3


    def to_sleep(self):
        print("time to sleep")
        self.gladness += 5

    def to_chill(self):
        print("time to rest")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5
            print("Cast out")
            self.alive = False
        elif self.gladness <= 0
            print("depression")
            self.alive = False

        elif self.progress > 5:
            print("frff")
            self.alive = False

    def end_of_day(self):
        print(f"gladness = {self.gladness}")
        print(f"progress = {round(self.progress)}


    def live(self, day):
        day = "Day" = str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)

    if live_cube == 1

        '''

nick = Student()
ann = Student()
ann.name = "Ann"


print(f"My name is {nick.name}")
print(f"My name is {ann.name}")

'''

