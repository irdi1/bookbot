import sys
from stats import get_num_words, count_characters, sort_dictionary



def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    # file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_text = get_num_words(text)
    my_dict = count_characters(text)
    sorted_dict = sort_dictionary(my_dict)
    book_report(file_path,num_text, sorted_dict)

def get_book_text(path):
    
    with open(path) as f:
        file_contents = f.read()
    
    return file_contents


def book_report(file_path, num_text, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_text} total words")
    print("--------- Character Count -------")
    for item in sorted_dict:
        if not item["char"].isalpha():
            continue
        print(f"- {item['char']}: {item['num']}")




if __name__ == "__main__":
    main()
