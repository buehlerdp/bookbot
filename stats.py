def word_count(text):
    words = text.split()
    length = len (words)
    #return (length)
    print (f"{length} words found in the document")


def character_count(text):
    lowercase = text.lower()
    counts = {}
    #"a": lowercase.count("a")  
    for char in lowercase:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    print (counts)

 