tempratures = []
user_input = input("what do you want celcius or farenheit (C/F): ").upper()
enter_more = True

def conversion(user_input, temp):            
    if user_input == "F":
        celcius = temp
        temprature = ((celcius - 32) * 5) / 9
        return temprature
    elif user_input == "C":
        farenheit = temp
        temprature = (farenheit * 1.8) + 32
        return temprature   

while enter_more:
    list_of_temprature = float(input("whats your desired temprature: "))
    tempratures.append(list_of_temprature)
    ask_again = input("enter more or Press Q to sotp: " ).upper()
    if ask_again == "Q":
        break
    else:
        continue
if user_input == "C":
    for i in tempratures:
     farenheit = conversion(user_input, i)
     print(f"{i}c = {round(farenheit, 2)}f")
elif user_input == "F":
    for i in tempratures:
        celcius = conversion(user_input, i)
        print(f"{i}f= {round(celcius,2)}c")
                



   











            

      


