name=input("Enter your name: ")
weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in meters: "))

bmi=weight/(height*height)

print("\n================================")
print("         BMI REPORT             ") 
print("================================")
print("Name: ",name)
print(f"Weight: {weight} kg")
print(f"Height: {height} m  \n")


print(f"\nBMI:{bmi:.2f}")
print("================================")
