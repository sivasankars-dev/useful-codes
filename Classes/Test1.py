class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Cat(Animal):
    def speak(self):
        return "Meow"

cat = Cat("Little Tiger")
print(f"My cat {cat.name} always says {cat.speak()}") 