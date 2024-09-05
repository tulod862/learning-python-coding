def enter_charges_and_total():
    while True:
        try:
            num_charges = int(input("Enter the number of charges (greater than 1): "))
            if num_charges > 1:
                break
            print("Number of charges must be greater than 1.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    total_sum = 0
    for i in range(num_charges):
        while True:
            try:
                total_sum += num_charges
                float(input(f"Enter charge {i + 1}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    print(f"Total of all charges: ${total_sum:.2f}")

enter_charges_and_total()