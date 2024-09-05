import string

def count_word_frequency(text):
    word_count = {}
    for word in text.split():
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def main():
    text = input("Enter a text: ") 
    word_count = count_word_frequency(text)
    for word, count in word_count.items():
        print(f'Word "{word}" appears {count} times')

if __name__ == "__main__":main()
