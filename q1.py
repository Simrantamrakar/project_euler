#if we list all the natural below 10 that are multiple of 3 or 5,we get 3,5,6 and 9. the sum of these multiples is 23. find the sum of all the multiples of 3 or 5 below 1000 in python.

sum=0

for i in range(1,1000):
    if i % 3==0 or i % 5==0:
        sum+=i
        
print(sum)