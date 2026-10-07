
count=0

for i in range(5):
    guess=int(input(f"Guess a number between 1 and 10({5-count} left): "))
    count+=1
    

    if guess==8:
        print("Congratulations!")
        print("You guessed the number in",count,"attempts.")
      
    elif guess<1 or guess>10:
        print("Invalid input.")

    else:
       if count < 5:            
            print("Try again.")

else: 
    print("Game Over!")




   