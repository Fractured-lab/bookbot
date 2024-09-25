def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_book_word_count(text)
    chars = get_book_letter_count(text)
    sorted_chars = get_sorted_letter_count(chars)
    print(f"---Report of {book_path}---")
    print(f"{words} total words in document")
    print()
    for item in sorted_chars:
        print(f"The Letter {item['char']} was found {item['num']} times.")
    print("=====End Report=====")
    
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return(file_contents)
    
def get_book_word_count(text):
    words = text.split()
    return len(words)
def get_book_letter_count(text):
    lowered_txt = text.lower()
    chars = {}
    for c in lowered_txt:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_on(d):
    return d["num"]

def get_sorted_letter_count(chars):
    letters = []
    for char in chars:
        if char.isalpha():
            #print(char)
            key_value_pair = {"char": char, "num": chars[char]}
            #print(key_value_pair)
            letters.append(key_value_pair)
            #print(letters)
    letters.sort(reverse=True, key=sort_on)
    return letters


    



        
    


main()