num = int(input("Give me a number:"))

list_a = range(1,num+1)

divisors = []

for i in list_a:
    if num % i == 0:
        divisors.append(i)

print(divisors) 
