
def enter_charges_and_total():
    
    while True:
        try:
            num_charges = int(input("Enter the number of charges (between 1 and 3): "))
            if 1<= num_charges <= 3:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    total_sum += num_charges
    for i in range(num_charges):
        while True:
            try:
                charge = float(input(f"Enter charge {i + 1}: "))
                total_sum += num_charges
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    print(f"Total of all charges: ${'Total':.2f}")

enter_charges_and_total()
