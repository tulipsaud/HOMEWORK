ASCII - 
ch = input("Enter a letter: ")
if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
   print("ASCII code is:", ord(ch))
else:
   print("Not a letter.")

ALPHABET- 
alp = input("Enter a character: ")
if ('a' <= alp <= 'z') or ('A' <= alp <= 'Z'):
    print("It is an alphabet.")
else:
    print("It is not an alphabet.")

TRIANGLE - 
n = int(input("Enter the number of rows: "))
char = input("Enter a character to use for the triangle: ")
for i in range(1, n + 1):
    print(" " * (n - i) + char * i)

POWER -
base = float(input("Enter the base number: "))
exponent = int(input("Enter the power: "))
result = base ** exponent
print("Result:", result)

REVERSE ORDER-
num = int(input("Enter a number: "))
if num < 0:
    num = -num
count = 0
if num == 0:
    count = 1
else:
    while num > 0:
        num = num // 10
        count += 1
print("Number of digits:", count)

BINARY CONVERSION- 
num = int(input("Enter a decimal number: "))
binary = ""
while num > 0:
    for i in range(1): 
        binary = str(num % 2) + binary
    num = num // 2
print("Binary:", binary)

CIRCUMFERENCE-
def calculate_circumference(radius):
    pi = 3.1416
    return 2 * pi * radius
r = float(input("Enter the radius of the circle: "))
circumference = calculate_circumference(r)
print("Circumference of the circle is:", circumference)