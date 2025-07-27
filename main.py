from stats import word_count, char_count, sort_dict
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")

    book_path = sys.argv[1]

    print(f"Analyzing book found at {book_path}...")
    text = get_book_text(book_path)

    print("----------- Word Count ----------")
    wc = word_count(text)
    print(f"Found {wc} total words")

    print("--------- Character Count -------")
    cc_dic = char_count(text)
    sorted_cc = sort_dict(cc_dic)

    for item in sorted_cc:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")


main()
