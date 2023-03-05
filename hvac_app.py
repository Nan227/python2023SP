import weather_lib

#setpoint = 21.5
setpoint =float(input("Enter the temperature in celsius: "))

print(f" Your Setpoint is {setpoint} celsius, and it equals to {round(weather_lib.degF(setpoint),2)} fahrenheit" )
