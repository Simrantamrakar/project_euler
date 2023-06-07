#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_multiple():
    n = 1
    while True:
        for i in range(1, 21):
            if n % i != 0:
                break
        else:
            return n
        n += 1

smallest_multiple_20 = smallest_multiple()
print(smallest_multiple_20)