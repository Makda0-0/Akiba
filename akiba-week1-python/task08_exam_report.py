student_name=input("Enter your name: ")
python_score=float(input("Enter your python score: "))
english_score=float(input("Enter your english score: "))
mathematics_score=float(input("Enter your mathematics score: "))

average_score=(python_score+english_score+mathematics_score)/3

print("================================")
print("         STUDENT RESULT       ")
print("================================")

print("Student: ", student_name)
print("Python: ", python_score)
print("English: ", english_score)
print("Mathematics: ", mathematics_score)
print("--------------------------------")
print(f"Average Score: {average_score:.2f}")
print("================================")
