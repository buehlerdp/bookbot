from stats import word_count

from stats import character_count

from stats import make_list

def get_book_text(book_path):
    with open (book_path) as f:
        file_contents = f.read() 
        return file_contents
        #print (file_contents)


def main():
    tocount = get_book_text("./books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at /books/frankenstein.txt...")
    print("----------- Word Count ----------")
    word_count (tocount)
    print("--------- Character Count -------")
    intermediate = character_count (tocount)
    make_list (intermediate)
    print("============= END ===============")

main()
