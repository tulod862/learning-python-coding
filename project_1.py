#celsuis_to_fahrentheit

def celsius_to_fahrentheit(Celsius):
    return (Celsius * 9/5) + 32
c = input ("Enter temperature in celsius")    
c = float (c)
f= celsius_to_fahrentheit(c)

print(f"{c}°C is {f:.2f}°F")

if c > 36:
  print ("It hot bring a water. ") 
