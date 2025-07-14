num = int(input("Enter a number: "))
odd_numbers = [i for i in range(num) if i % 2 != 0]
odd_numbers_after = [i for i in range(num + 1, num * 2) if i % 2 != 0]
print("Odd numbers less than", num, ":", odd_numbers)
print("Odd numbers after", num, "to", num * 2, ":", odd_numbers_after)
fruits = ['apple', 'banana', 'cherry', 'mango']
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("Capitalized fruits list:", capitalized_fruits)


import random
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
all_characters = lowercase + uppercase + digits
password_length = 12
password = "".join(random.sample(all_characters, password_length))
print("Generated Password:", password)


class Dog:
    animal = "Dog"
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
    def display(self):
        print(f"Animal: {Dog.animal}, Breed: {self.breed}, Color: {self.color}")
dog1 = Dog("Labrador", "Black")
dog2 = Dog("German Shepherd", "Brown")
dog1.display()
dog2.display()


import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
radius_input = float(input("Enter the radius of the circle: "))
my_circle = Circle(radius_input)

print(f"Area of the circle: {my_circle.area():.2f}")
print(f"Perimeter of the circle: {my_circle.perimeter():.2f}")


class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100
class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare() 
        maintenance = base_fare * 0.10
        return base_fare + maintenance
bus = Bus(50)
print(f"Total bus fare: INR {bus.fare()}")


class Reverse:
    def __init__(self, s=""):
        self.__s = s 
    def set_string(self, new_string):
        self.__s = new_string
    def get_reversed(self):
        words = self.__s.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)
sentence = input("Enter a sentence: ")
rev = Reverse()
rev.set_string(sentence)
print("Reversed string (word by word):", rev.get_reversed())


class BMW:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "250 km/h"

class Ferrari:
    def fuel_type(self):
        return "Diesel"

    def max_speed(self):
        return "340 km/h"
def display_car_info(car):
    print("Fuel Type:", car.fuel_type())
    print("Max Speed:", car.max_speed())
    print()
bmw_car = BMW()
ferrari_car = Ferrari()

display_car_info(bmw_car)
display_car_info(ferrari_car)


class IntegerToRoman:
    def __init__(self, number):
        self.number = number
    def convert_to_roman(self):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        roman = ""
        num = self.number
        for i in range(len(val)):
            while num >= val[i]:
                roman += syms[i]
                num -= val[i]
        return roman
num = int(input("Enter an integer to convert to Roman numeral: "))
converter = IntegerToRoman(num)
print("Roman numeral:", converter.convert_to_roman())


import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game screen")
gray = (58, 58, 58)
image = pygame.image.load("background.png")
image = pygame.transform.scale(image, (300, 300))
rect = image.get_rect(center=(250, 250))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(gray)
    screen.blit(image, rect)
    pygame.display.flip()

pygame.quit()









