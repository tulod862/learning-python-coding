import csv

total_sum = 0.0

with open('spent.csv') as file:
    csv_reader = csv.DictReader(file)
        
    for row in csv_reader:
        try:
            
            price = float(row['price'])
            if price < 0:
                print("price cannot be negative")
                continue
            total_sum += price
        except ValueError:

            print(f"Warning: Could not convert {row['price']} to float.")

print(f"Total sum of all spent items: YEN {total_sum:.2f}")
