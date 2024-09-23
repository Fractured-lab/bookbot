def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_book_word_count(text)
    letters = get_book_letter_count(text)
    print(text, words)
    
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return(file_contents)
    
def get_book_word_count(text):
    words = text.split()
    return len(words)
def get_book_letter_count(text):
    lowered_txt = text.lower()
    
    


main()