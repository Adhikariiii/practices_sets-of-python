students = {
    "Alice": [80, 90, 70, 40],
    "Bob": [50, -10, 30, 50],
    "Charlie": [],
    "Dave": [100, 95, 105]
}
filtered_list = {}
final_score = {"students":{}}
passed = 0
failed = 0

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
    if not result:
        filtered_list[name] = []
    else:    
        valid_score = []
        for each_result in result:
            if 0 < each_result <= 100:
                valid_score.append(each_result)
        filtered_list[name] = valid_score


for name, result in filtered_list.items():
    if  not result :
        final_score["students"][name] = {
            "average": None,
            "grade": "no data available"
        }
        failed += 1
        continue
    else: 
        average = round(sum(result) / len(result))
        final_score["students"][name] = { 
             "average": average,
            "grade": conversion(average)

        }
    if average < 50:
        failed += 1
    else:
        passed+=1
final_score["stats"] = {
        "passed": passed,
        "failed": failed
    }

    
print(final_score)