#The prime factors of 13195 are 5,7,13 and 29. what is the largest prime factor of the number 600851475143?

def largest_prime_factor(number):
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
    if number > 1:
        return number
    return i

number = 600851475143
largest_prime = largest_prime_factor(number)
print("The largest prime factor of", number, "is", largest_prime)