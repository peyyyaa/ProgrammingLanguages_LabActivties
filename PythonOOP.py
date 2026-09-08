class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says: Arf! Arf!")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthdayy, {self.name}! You're {self.age} years old now!")

    def show_info(self):
        print(f"Dog Name: {self.name}")
        print(f"Dog Age: {self.age} years old")


# Create a Dog object
myDog = Dog("Nami", 5)

# Use the methods
myDog.show_info()
myDog.bark()
myDog.birthday()
myDog.show_info()