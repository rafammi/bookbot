import sys 
from stats import get_num_words, get_num_letter, sort_dict 

def get_book_text(path) -> str:
    with open(path) as f:
        file_contents = f.read()

    return file_contents.lower()

def main(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    file_contents = get_book_text(path)
    total_count = get_num_words(file_contents)
    print("----------- Word Count ----------")
    print(f"Found {total_count} total words")
    print("--------- Character Count -------")
    d = get_num_letter(file_contents)
    result = sort_dict(d)
    for char in result:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    main(sys.argv[1])
