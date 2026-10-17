def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def get_divisors(number):
    if number <= 0:
        return []
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

def sum_of_digits(number):
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number = number // 10
    return total

def reverse_number(number):
    sign = -1 if number < 0 else 1
    number = abs(number)
    reversed_num = 0
    while number > 0:
        reversed_num = reversed_num * 10 + number % 10
        number = number // 10
    return sign * reversed_num

def analyze_number(number):
    if number % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print("Number:", number)
    print("Even/Odd:", even_odd)
    print("Prime:", is_prime(number))
    print("Sum of digits:", sum_of_digits(number))
    print("Reversed:", reverse_number(number))
    print("Divisors:", get_divisors(number))

analyze_number(123)