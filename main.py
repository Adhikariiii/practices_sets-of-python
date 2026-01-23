def main():
 state = True
 while  state:
  user_input = input("Enter what you want to convert the input into (C/F): ").upper()
  if user_input == "C":
                kelvin = float(input("Enter your a temprature value in Kelvin: "))
                degree = kelvin - 273.15
                print(f"   temp:{kelvin}k = {round(degree, 2)}℃")
                break
  elif user_input == "F":
    kelvin = float(input("Enter your a temprature value in Kelvin: "))
    farenhiet = kelvin -459.67
    print(f"   temp:{kelvin}k = {round(farenhiet, 2)}℉")
    break
  else :
        print("please enter either C or F")
        state = True
        continue

main()

        

