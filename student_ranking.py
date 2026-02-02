students = {
    "Alice": [80, 90, 70, 40],
    "Bob": [50, -10, 30, 50],
    "Charlie": [],
    "Dave": [100, 95, 105]
}

filtered_students = {}
final_result = []

for name, result in students.items():
    valid_scores = []
    if not result:
           filtered_students[name] = valid_scores
    for each_result in result:
        if  0 < each_result <= 100:
            valid_scores.append(each_result)
        filtered_students[name] = valid_scores
# print(filtered_students)    
            
calculated_result = []     
for name, result in filtered_students.items():
    # print(result)
    if not result:
        calculated_result.append((name, None))
    else:
         average_score = round(sum(result) / len(result))
         calculated_result.append((name, average_score))
calculated_result.sort(key=lambda item: (item[1] is None, item[1]))
print(calculated_result)

        