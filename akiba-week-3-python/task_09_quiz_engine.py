questions = [
    {"q": "2 + 2 = ?", "options": ["3", "4", "5"], "answer": "4"},
    {"q": "Capital of Ethiopia?", "options": ["Addis Ababa", "Cairo", "Nairobi"], "answer": "Addis Ababa"},
    {"q": "Days in a week?", "options": ["5", "6", "7"], "answer": "7"},
    {"q": "Sky color?", "options": ["Green", "Blue", "Red"], "answer": "Blue"},
    {"q": "10 / 2 = ?", "options": ["3", "4", "5"], "answer": "5"},
]


def play_quiz():
    score = 0
    for i, q in enumerate(questions, 1):
        print("")
        print("Q" + str(i) + ":", q["q"])
        for j, option in enumerate(q["options"], 1):
            print("  ", j, ".", option)

        answer = input("Your answer: ").strip().lower()

        
        if answer.isdigit() and 1 <= int(answer) <= len(q["options"]):
            answer = q["options"][int(answer) - 1].lower()

        if answer == q["answer"].lower():
            print("Correct!")
            score = score + 1
        else:
            print("Wrong. Answer:", q["answer"])

    total = len(questions)
    percent = score / total * 100

    if percent >= 80:
        category = "Excellent"
    elif percent >= 60:
        category = "Good"
    elif percent >= 40:
        category = "Pass"
    else:
        category = "Fail"

    print("")
    print("Score:", score, "/", total)
    print("Correct:", score, " Incorrect:", total - score)
    print("Percentage:", percent, "%")
    print("Category:", category)


while True:
    play_quiz()
    if input("Play again? (yes/no): ").strip().lower() != "yes":
        break