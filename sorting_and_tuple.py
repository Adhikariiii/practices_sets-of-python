students = { "Alice": [80, 90, 70, 40],
             "Bob": [50, -10, 30, 50], 
             "Charlie": [], 
             "Dave": [100, 95, 105] 
             }
filtered_students = {}
final_result = []

for name, result in students.items():
    if not result:
        filtered_students[name] =  []
    else:
        valid_score = []
        for each in result:
            if 0 < each <= 100:
                valid_score.append(each)
        filtered_students[name] = valid_score
# print(filtered_students)

for name, result in filtered_students.items():
    score_tuple = ()
    if not result:
        score_tuple =(name, None)
        
        final_result.append(score_tuple)
    else:
        highest_score = round(sum(result) / len(result))
        score_tuple = (name, highest_score)
        final_result.append(score_tuple)

def key(item):
    return (item[1] is None, item[1])

# for item in final_result:
#     key_value = key(item)

    # if key_value 
  
final_result.sort(
    key=lambda item: (item[1] is None, -(item[1] or 0)),
    # reverse=True,
    )

print(final_result)