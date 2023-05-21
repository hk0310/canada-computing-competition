import math

prime = []
num_input = []
result = []
rep = int(input())

def is_prime(n):
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    square = math.floor(math.sqrt(n)) 
    for i in range(3, 1+square, 2):
        if n % i == 0:
            return False
    return True


for i in range(rep):
    num = int(input())
    num_input.append(num)

for num in num_input:
    total = int(num) * 2

    for potential_prime in range(2, total):
        if is_prime(potential_prime):
            prime.append(potential_prime)

    for i, number in enumerate(prime):
        complementary = total - number
        if complementary in prime[i:]:
            result.append(number)
            result.append(complementary)
            break
    """
    for a in prime:
        if (total - a) % 2 == 0 and total - a != 2:
            prime.remove(a)
    for b in prime:
        if result == []:
            if total - b == 2:
                result.append(b)
                result.append(2)
                break
            for c in prime:
                if b + c == total:
                    result.append(b)
                    result.append(c)
                    break
"""
    print(*result, sep=" ")
    result.clear()
