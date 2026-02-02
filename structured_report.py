students = {
    "Alice": [80, 90, 70, 40],
    "Bob": [50, -10, 30, 50],
    "Charlie": [],
    "Dave": [100, 95, 105]
}
status = ""
filtered_students = {}
report = {}
def grade_conversion(score):
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
def status_convversion(grade):
     if grade == "F":
          return "fail"
     else:
         return "pass"

for name, result in students.items():
    # print(result)
    if not result:
        # filtered sutdents should return empty list not none because if there is none it wont be count as empty list 
            valid_score = []

    for every_socre in result:
            if 0 < every_socre <= 100:
                valid_score.append(every_socre)
    filtered_students[name] = valid_score
# print(filtered_students)


for name, every_subject in filtered_students.items():
    
    if not every_subject: 
         report[name] = {
            "socres": "no data available",
            "average": "0",
            "score" : None,
            "status": "fail"
         }
    else:
        average_mark = round(sum(every_subject) / len(every_subject), 1)
        grade = grade_conversion(average_mark)
        status = status_convversion(grade)
            
        report[name] = {
            "socres": every_subject,
            "average": average_mark,
            "score" : grade,
            "status": status
          
     }


print(report)