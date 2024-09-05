#Temparature F: 78 to Celsius

def fahrenheit_to_celsius(fahrenheit):
     return (fahrenheit - 32) * 5/9
f = input('Enter temperature in Fahrenheit:')
f = float(f)
c = fahrenheit_to_celsius(f)
print(f"{f}°F is {c:.2f}°C")


