print(" *** Wind classification ***")
user_input = float(input("Enter wind speed (km/h) : "))
if user_input < 0:
    print("!!!Wrong value can't classify.")
elif  user_input >= 0 and user_input <= 51.99:
    print("Wind classification is Breeze.")
elif user_input > 51.99 and user_input <= 55.99:
    print("Wind classification is Depression.")
elif user_input > 55.99 and user_input <= 101.99:
    print("Wind classification is Tropical Storm.")
elif user_input > 101.99 and user_input <= 208.99:
    print("Wind classification is Typhoon.")
elif user_input >= 209:
    print("Wind classification is Super Typhoon.")