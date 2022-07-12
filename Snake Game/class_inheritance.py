class Animal:
    def __init__(self):
        self.eyes = 2

    def breath(self):
        print("this animal can breathe")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("Breaths in water.")



fish = Fish()
fish.breath()
print(fish.eyes)