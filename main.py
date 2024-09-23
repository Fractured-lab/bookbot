from collections import Counter
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_book_word_count(text)
    letters = get_book_letter_count(text)
    print(text, words, letters)
    
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return(file_contents)
    
def get_book_word_count(text):
    words = text.split()
    return len(words)
def get_book_letter_count(text):
    lowered_txt = text.lower()
    letters_only = ""
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in lowered_txt:
        if i in alphabet:
            letters_only += i
    return Counter(letters_only)
        
    


main()