# Python program to compute the Greatest Common Divisor (GCD) of two positive integers.
# Euclidean algorithm



a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
nwd = 1
    
while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print(f'The greatest common divisor is: {a}')


