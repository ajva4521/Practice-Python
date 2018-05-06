num = int(input("Give me a number:"))

a = [1, 1, 2, 3, 5, 8, 13, 21]
b = []

for i in a:
  if i < num:
      b.append(i)

print(b)
