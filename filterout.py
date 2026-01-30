def conversion(unit, temp):            
    if unit == "C":
     celsius = ((temp - 32) * 5) / 9
     return celsius
    elif unit == "F":
        fahernheit = (temp * 1.8) + 32
        return fahernheit   

temps = [0, 12, 233, -22, 66]
unit = "F"
list_summary = []
minimum_temp = 0
maximum_temp = 0
average = 0 
count = 0

for i in temps:
       summary = round( conversion(unit, i), 2)
       list_summary.append(summary)

    
filtered = []

for i in list_summary:
    if i >= -50 and i<=150:
        filtered.append(i)

if not filtered  :
        print("The list seems to be empty")


else:
     minimum_temp = min(filtered)
     maximum_temp = max(filtered)
     average =round( sum(filtered) / len(filtered), 2)
     count = len(filtered)


temp_summary = {
    "min" : minimum_temp,
    "max": maximum_temp,
    "average": average,
    "count": count
}
print(temp_summary)
