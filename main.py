from stats import word_count


def get_book_text(book_path):
    with open (book_path) as f:
        file_contents = f.read() 
        return file_contents
        #print (file_contents)


def main():
    tocount = get_book_text("./books/frankenstein.txt")
    word_count (tocount)

main()
