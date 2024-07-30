def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = get_characters(text)
    checkWord = input("Enter a word: ")
    inCheck = nicks_a_belter(text, checkWord)

    print(f"{num_words} words found in the document")
    for character, count in characters.items():
        print(f"the '{character}' character was found: {count} times")
    print(f"The word '{checkWord}' was found {inCheck} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_characters(text):
    lowText = text.lower()
    bank = {}
    for i in lowText:
        if i.isalpha():
            if i not in bank:
                bank[i] = 1
            else:
                bank[i] += 1
            
    sorted_bank = dict(sorted(bank.items()))
    return sorted_bank

def nicks_a_belter(text, checkWord):
    words = text.lower().split()
    word_count = words.count(checkWord.lower())
    return word_count

main()
