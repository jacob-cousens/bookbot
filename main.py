import sys

from stats import (
    get_word_count, 
    get_chars_dict, 
    get_chars_dict_list,
)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_alpha_chars(chars):
    for c in chars:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")

def print_report(book_path, num_words, chars_dict_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_alpha_chars(chars_dict_list)
    print("============= END ===============")
        
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_word_count(text)
    chars_dict = get_chars_dict(text)
    chars_dict_list = get_chars_dict_list(chars_dict)
    print_report(book_path, num_words, chars_dict_list)

if __name__ == "__main__":
    main()
