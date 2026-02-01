scores = [80, 40, 50, 30, -8, 69]
filtered_scores = []
average = None
highest = None
lowest = None
grade = None

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
            
for i in scores:
    if i > 0:
        filtered_scores.append(i)
if not filtered_scores:
    print({})      

average = round(sum(filtered_scores) / len(filtered_scores), 1)
highest = max(filtered_scores)
lowest = min(filtered_scores)
grade =  grade_conversion(average)

report = {
    "valid score": filtered_scores,
    "avaerage": average,
    "highest": highest,
    "lowest": lowest,
    "grade": grade
}

print(report)