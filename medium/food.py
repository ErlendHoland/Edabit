class Person:

    def __init__(self, name, loves, hates):
        self.name = name
        self.loves = loves
        self.hates = hates
        



    def taste(self, food):
        if food in self.loves:
            return "{} eats the {} and loves it!".format(self.name, food)

        elif food in self.hates:
            return "{} eats the {} and hates it!".format(self.name, food)

        else:
            return "{} eats the {}!".format(self.name, food)


p1 = Person("Sam", ["Pizza"], ["Fish"])

print(p1.taste("Pizza"))
print(p1.taste("Fish"))
print(p1.taste("Something else"))

