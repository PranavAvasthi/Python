import math as m
number = 29
is_prime = True

if number > 1:
    for i in range(2, int(m.sqrt(number))):
        if (number%i) == 0:
            is_prime = False
            break

print(is_prime)