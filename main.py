from stats import word_count

from stats import character_count

from stats import make_list

import sys

def get_book_text(book_path):
    with open (book_path) as f:
        file_contents = f.read() 
        return file_contents
        #print (file_contents)


def main():
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        tocount = get_book_text(sys.argv[1])
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        word_count (tocount)
        print("--------- Character Count -------")
        intermediate = character_count (tocount)
        make_list (intermediate)
        print("============= END ===============")

main()
