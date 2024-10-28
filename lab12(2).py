import random

def generate_phone_numbers(N):
    phone_numbers = []
    for _ in range(N):
        number = "+38 098 " + ''.join(random.choice('0123456789') for _ in range(7))
        phone_numbers.append(number)
    return phone_numbers

N = 10
phone_numbers = generate_phone_numbers(N)
for number in phone_numbers:
    print(number)
