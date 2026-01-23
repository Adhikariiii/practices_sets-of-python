
def conversion(user_input, temp):
    if user_input == "F":
        celcius = temp
        temprature = ((celcius - 32) * 5) / 9
        return temprature
    elif user_input == "C":
        farenheit = temp
        temprature = (farenheit * 1.8) + 32
        return temprature


loop = True

while loop:
        user_input = input("Enter C for celcius and F or Farenheit: ")
    
        if user_input == "F":
            temprature = float(input("Enter temprature in farenheit: "))
            celcius = conversion(user_input , temprature)
            print(f"{round(temprature, 2)} = {round(celcius, 2)}")
            break
        elif user_input == "C":
            temprature = float(input("Enter temprature in Celius: "))
            farenheit = conversion(user_input , temprature)
            print(f"{round(temprature, 2)} = {round(farenheit, 2)}")
            break
        else:
            print("wrong Input: ")
            continue


            
            
            


