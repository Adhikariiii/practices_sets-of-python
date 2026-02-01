students = {
    "Alice": [80, 90, 70, 40],
    "Bob": [50, -10, 30, 50],
    "Charlie": [],
    "Dave": [100, 95, 105]
}
filetered_students = {}
final_results = {}

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

for name, result in students.items():
    valid_scores = []
    # print(result)
    if not result:
        filetered_students[name] = None
    for every_subject in result:
        #  print(every_subject)
         if 0< every_subject <= 100  :
              valid_scores.append(every_subject)
    filetered_students[name] =  valid_scores
# print(filetered_students)
for student_name, result in filetered_students.items():
    
    if not result:
         final_results[student_name] = {
              "average": None,
              "grade": "No Data Avaliable"
         }
    else:
         average = sum(result) / len(result)
         
         final_results[student_name] = {
              "average": round(average),
              "grade": conversion(average)
         }

for student, result in final_results.items():
    print(f"Student: {student},")
    print(f"score: {result["average"]}")
    print(f"Grade: {result["grade"]}")
    print("-"*30)
    







