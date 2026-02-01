temps = [10, 20, 30, 40, 50, 60]
unit = "C"
average = 0 
status =  None
Tempratures = None
filtered_temp = []

if not temps:
    print("No Temprature data available")
else:
    if unit == "C":
        for i in temps:
         filtered_temp.append(f"{i}℃")
    elif unit == "F":
        for i in temps:
                filtered_temp.append(f"{i}℉")

    if not filtered_temp:
                Tempratures = None
    else:
                Tempratures = ', '.join(filtered_temp)
                average = sum(temps) / len(temps)
                if average < 10:
                    status = "Cold"
                elif average >= 10 and average<25:
                    status = "warm"
                elif average > 25: 
                    status = "hot"
                print("Weather Report")
                print("--------------------------")
                print(f"Tempratures = {Tempratures}")
                print(f"Average temprature = {average}")
                print(f"status= {status}")










    