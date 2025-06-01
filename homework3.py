def calculate_return(paid, total_bill):
    return paid - total_bill
paid_amount = 4.00
total_bill = 2.50
money_returned = calculate_return(paid_amount, total_bill)
print("The shopkeeper should return $", money_returned)

def check_age():
    try:
        age_input = input("Enter your age: ")
        age = int(age_input)
        if age % 2 == 0:
            print("The age entered is even.")
        else:
            print("The age entered is odd.")
    except ValueError:
        print("Value Error: Please enter a valid whole number (no letters, decimals, or symbols).")
check_age()

import math

def trigonometric_calculations():
    try:
        angle_deg = float(input("Enter the angle in degrees: "))
        angle_rad = math.radians(angle_deg)
        sine_value = math.sin(angle_rad)
        cosine_value = math.cos(angle_rad)
        tangent_value = math.tan(angle_rad)
        print(f"\nTrigonometric values for {angle_deg}°:")
        print(f"Sine: {sine_value}")
        print(f"Cosine: {cosine_value}")
        print(f"Tangent: {tangent_value}")
    except ValueError:
        print("Invalid input! Please enter a numeric value for the angle.")
trigonometric_calculations()

import calendar
def print_month_names():
    print("Names of all the months:\n")
    for month in range(1, 13):
        print(calendar.month_name[month])
print_month_names()

def squaresep(start, end):
    squares = ()
    odd_squares = ()
    even_squares = ()
    for num in range(start, end + 1):
        square = num ** 2
        squares.append(square)
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)
    print(f"All squares from {start} to {end}: {squares}")
    print(f"Even squares: {even_squares}")
    print(f"Odd squares: {odd_squares}")
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
squaresep(start, end)