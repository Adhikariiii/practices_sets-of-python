students = {
    "Alice": [80, 90, 70],
    "Bob": [50, 40, 30],
    "Charlie": [100, 95, 105]
}
students_results = {}
each_student_data = {}


def conversion(score):
        if score >= 85:
            return "A"
        elif 75 <= score <= 84:
            return "B"
        elif 65 <= score <= 74:
            return "C"
        elif 50 <= score <= 64:
            return "D"
        else: 
            return "F"
average = None

for student, result in students.items():
        average = sum(result) / len(result)
        students_results[student] = {
            "average": average,
            "grade": conversion(average)
        }

print(students_results)