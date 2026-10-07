N = int(input("Enter a positive number: "))
if N < 0:
    print("Please enter a positive number.")

even_count = 0
odd_count = 0
total = 0

for i in range(1, N + 1):
  if i % 2 == 0:
    even_count += 1
  else:
    odd_count += 1
    total += i

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)   
print("Sum of all numbers:", total)

  






