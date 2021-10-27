print(" *** Wind classification ***")
speed = float(input("Enter wind speed (km/h) : "))
if speed >= 0 and speed <=51.99:
    wind_class = "Breeze"
elif speed >= 52.00 and speed <=55.99:
    wind_class = "Depression"
elif speed >= 56.00 and speed <=101.99:
    wind_class = "Tropical Storm"
elif speed >= 102.00 and speed <=208.99:
    wind_class = "Typhoon"
elif speed >= 209:
    wind_class = "Super Typhoon"
print("Wind classification is " + wind_class + ".")