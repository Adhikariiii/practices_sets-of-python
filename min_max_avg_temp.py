temps = [0, 12, 233, -22, 66]
unit = "F"
converted_temps = []

def conversion(unit, temp):            
    if unit == "C":
     celcius = ((temp - 32) * 5) / 9
     return celcius
    elif unit == "F":
        farenheit = (temp * 1.8) + 32
        return farenheit   
if unit == "C":
  for i in temps:
    list_of_celicus = conversion(unit, i)
    converted_temps.append(round(list_of_celicus , 2))
elif unit == "F":
  for i in temps:
    list_of_farenheit = conversion(unit, i)
    converted_temps.append(round(list_of_farenheit , 2))
minimum_temprature = min(converted_temps)
maximum_temprature = max(converted_temps)
average = round((sum(converted_temps) / len(converted_temps)), 2)

print(f"list in {unit} : {converted_temps}")
print(f"Minimum temprature : {minimum_temprature}")
print(f"Maximim temprature : {maximum_temprature}")
print(f"Average temprature : {average}")
         
       

        