class Animal:
    def speak(self):
        raise NotImplementedError
class Bird(Animal):
    def speak(self):
        return "Tweet!"
class Dog(Animal):
    def speak(self):
        return "Awwww!"
class Cow(Animal):
    def speak(self):
        return "Moooo!"
class Goat(Animal):
    def speak(self):
        return "Meeee!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
print("\nThis Is Overriding Method\n")
if __name__ == "__main__":

    bird = Bird()
    dog = Dog()
    cow = Cow()
    goat = Goat()
    cat = Cat()

    print("Bird says:", bird.speak())
    print("Dog says:", dog.speak())
    print("Cow says:", cow.speak())
    print("Goat says:", goat.speak())
    print("Cat says:", cat.speak())