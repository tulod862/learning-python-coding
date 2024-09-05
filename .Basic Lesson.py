def school_age_calculation(age, name):
    if age < 5:
        print("Enjoy the time!", name, "is only", age)
    elif age == 5:
        print("Enjoy kindergarten,", name)
    else:
        print("they grow up so fast!")


school_age_calculation(5, "Pocky")
