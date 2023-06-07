#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009=91*99. Find  the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def largest_palindrome_product():
    largest_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
    return largest_palindrome

largest_palindrome = largest_palindrome_product()
print("The largest palindrome made from the product of two 3-digit numbers is", largest_palindrome)