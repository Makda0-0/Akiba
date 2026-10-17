students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]

def validate_student_score(score):
    if 0 <= score <= 100:
        return True
    else:
        return False

def calculate_grade(grade):
    if 90 <= grade <= 100:
        return "A"
    elif 80 <= grade <= 89:
        return "B"
    elif 70 <= grade <= 79:
        return "C"
    elif 60 <= grade <= 69:
        return "D"
    else:
        return "F"

def average_score(score):
    total = 0
    for s in score:
        total += s["score"]
    return total / len(score)

def highest_lower_scores(score):
    highest = score[0]["score"]
    lowest = score[0]["score"]
    for s in score:
        if s["score"] > highest:
            highest = s["score"]
        if s["score"] < lowest:
            lowest = s["score"]
    return highest, lowest

def passing_failing_students(score):
    passing_score = 50
    passed_count = 0
    failed_count = 0
    for s in score:
        if s["score"] >= passing_score:
            passed_count += 1
        else:
            failed_count += 1
    return passed_count, failed_count