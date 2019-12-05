# karatsuba multiplication
import math

def karatsuba_multiplication(x, y):
    if x == 0 or y == 0 : return 0

    len_x = int(math.log10(x)) + 1
    len_y = int(math.log10(y)) + 1

    if len_x == 1 and len_y == 1: return x * y

    n = len_x if len_x >= len_y else len_y

    base_and_exp = math.pow(10, int(n / 2))

    a, b = int(x / base_and_exp), x % base_and_exp
    c, d = int(y / base_and_exp), y % base_and_exp

    step_one, step_two, step_three = a*c, b*d, (a+b)*(c+d)
    step_four = step_three - step_two - step_one

    return (step_one * math.pow(10, n)) + (step_two) + (step_four * math.pow(10, int(n/2)))

print(karatsuba_multiplication(5,3))
print(karatsuba_multiplication(5,30))
print(karatsuba_multiplication(5,35))
print(karatsuba_multiplication(35,5))
print(karatsuba_multiplication(15,15))
print(karatsuba_multiplication(5678, 1234))
print(karatsuba_multiplication(5678, 123))

# recursive integer multiplication
# (10^(n/2)a + b) * (10^(n/2)c + d)
# = 10^n * a * c + 10^(n/2)(ad + bc) + bd
def recursive_integer_multiplication(x, y):
    if x == 0 or y == 0 : return 0

    len_x = int(math.log10(x)) + 1
    len_y = int(math.log10(y)) + 1

    if len_x == 1 and len_y == 1: return x * y

    n = len_x if len_x >= len_y else len_y

    base_and_exp = math.pow(10, int(n / 2))

    a, b = int(x / base_and_exp), x % base_and_exp
    c, d = int(y / base_and_exp), y % base_and_exp

    ac = recursive_integer_multiplication(a, c)
    ad = recursive_integer_multiplication(a, d)
    bc = recursive_integer_multiplication(b, c)
    bd = recursive_integer_multiplication(b, d)

    return math.pow(10, n) * ac \
           + math.pow(10, int(n/2)) * (ad + bc) \
           + bd

print(recursive_integer_multiplication(5,3))
print(recursive_integer_multiplication(5,30))
print(recursive_integer_multiplication(5,35))
print(recursive_integer_multiplication(35,5))
print(recursive_integer_multiplication(15,15))
print(recursive_integer_multiplication(5678, 1234))
print(recursive_integer_multiplication(5678, 123))
print(recursive_integer_multiplication(123, 5678))
