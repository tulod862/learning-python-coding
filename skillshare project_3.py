import random

def assign_secret_santas(names):
    santas = names[:]
    random.shuffle(santas)
    return dict(zip(names, santas))

names = ["Pocky", "Martin", "Beary", "Evy"]
assignments = assign_secret_santas(names)
for giver, receiver in assignments.items():
    print(f"{giver} -> {receiver}")