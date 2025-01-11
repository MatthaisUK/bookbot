def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    word_count = get_num_words(text)
    letter_dict = count_letters(text)

    letter_list = list(letter_dict.items())

    letter_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print(" ")

    for letter, count in letter_list:
        print(f"The '{letter}' character was found {count} times")
        
    print("--- End Report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_letters(text):
    lowercase_text = text.lower()
    letter_counts = {}
    for letter in lowercase_text:
        if letter.isalpha() == False:
            continue
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts

def sort_on(dict):
    return dict[1]

main()