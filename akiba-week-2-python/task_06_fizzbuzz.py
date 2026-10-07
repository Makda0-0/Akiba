start_num=int(input("Enter the starting number: "))
end_num=int(input("Enter the ending number: "))

for num in range(start_num, end_num+1):
    if num%3==0 and num%5==0:
        print("FizzBuzz")

    elif num%3==0:
            print("Fizz")
                
    elif num%5==0:
        print("Buzz")
    
    else:
        print(num)    
