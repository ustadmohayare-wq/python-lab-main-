from utils import square, is_even, celsius_to_fahrenheit

number = float(input("Enter a number: "))

print(f"Square: {square(number)}")

if number.is_integer():
    print("Even" if is_even(number) else "Odd")
else:
    print("Not a whole number, so even/odd doesn't apply")

print(f"As Celsius, that is {celsius_to_fahrenheit(number)} °F")