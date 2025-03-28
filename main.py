from stats import get_num_words, get_char_count, sort_dict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_count(text)
    sorted_dict = sort_dict(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_dict:
        if dict["name"].isalpha() == True:
            print(f"{dict["name"]}: {dict["num"]}")
    print("============= END ===============")
    #print(char_dict)
    #print(sorted_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()