
total=0
even_count=0
odd_count=0
largest=None
smallest=None

for i in range(10):
    num = int(input(f"Enter a number {i + 1}: "))
    total+=num
    if num % 2 == 0:
        even_count+=num
    else:
        odd_count+=1

    if largest is None or num > largest:
      largest=num

    if smallest is None or num < smallest :
      smallest=num

average=total/10  

print("\nLargest number:",largest)
print("Smallest number:",smallest)
print("Total Sum:",total)
print("Average:",average)
print("Even numbers:",even_count)
print("Odd numbers:",odd_count)


      
    

   
    
        
          