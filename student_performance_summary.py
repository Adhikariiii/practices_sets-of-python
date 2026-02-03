students = {
    "Alice": [80, 90, 70, 40],
    "Bob": [50, -10, 30, 50],
    "Charlie": [],
    "Dave": [100, 95, 105]
}
filtered_students = {}
collect = {}
summary = {"students": {}, "summary": {}}
passed = 0
failed = 0 
highest_average = []
lowest_average = []

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

for  name, result in students.items():
    #  print(result)
     if not result:
          filtered_students[name] = []
     else:
          valid_score = []
          for each_result in result:
            #    print(each_result)
            if 0 < each_result <= 100 : 
                 valid_score.append(each_result)
            filtered_students[name] = valid_score
# print(filtered_students)

for name, result in filtered_students.items():

    if  not result:
        summary["students"][name] = {
            "average":None,
            "grade": "No Data"
        }
        failed += 1
        continue

    else:
        highest_average.append(max(result))
        lowest_average.append(min(result))
        average = round(sum(result) / len(result))

        if conversion(average) == "F":
            failed += 1
        else:
            passed += 1
        
        summary["students"][name] = {

                    "average": average,
                    "grade": conversion(average)
                
            }


summary["summary"] =  {
            "passed": passed,
            "failed": failed,
            "highest_average": sum(highest_average) / len(highest_average),
            "lowest_average": sum(lowest_average) / len(lowest_average)
        }


print(summary)

