import string

def clean_text(text):

    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    text = ' '.join(text.split())
    return text

def count_word_frequency(text):
    word_count = {}
    words = text.split()
  
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

def main():
    text = input("Enter a text: ")

    word_count = count_word_frequency(text)
    for word, count in word_count.items():
        print(f'Word "{word}" appears {count} times')
        
if __name__ == "__main__":main()