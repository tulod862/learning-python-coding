def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

lower = float(input("Enter lower limit: "))
upper = float(input("Enter upper limit: "))
increment = float(input("Enter increment: "))

if increment > 0:
    f = lower
    while f <= upper:
        print(f"Temperature {f:.0f} F is the same as {fahrenheit_to_celsius(f):.2f} C")
        f += increment
else:
    print("Increment must be greater than zero.")



