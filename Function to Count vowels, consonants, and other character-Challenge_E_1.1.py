sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0
others = 0

vowel_set = "aeiouAEIOU"

for char in sentence:
    if char.isalpha():
        if char in vowel_set:
            vowels += 1
        else:
            consonants += 1
    elif char != " ":
        others += 1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Other characters (excluding spaces):{others}")