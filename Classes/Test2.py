class Flyer:
    def fly(self):
        print("Flying high!")

class Swimmer:
    def swim(self):
        print("Swimming in water")

class Duck(Flyer, Swimmer):
    def fly(self):
        print("Duck is flying")

    def quack(self):
        print("Quack quack")


myduck = Duck()
myduck.fly()
myduck.swim()  
myduck.quack()  

