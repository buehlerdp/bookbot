def word_count(text):
    words = text.split()
    length = len (words)
    print (f"Found {length} total words")


def character_count(text):
    lowercase = text.lower()
    counts = {} 
    for char in lowercase:
        if (char in counts) and (char.isalpha() == True):
            counts[char] += 1
        elif (char.isalpha() == True):
            counts[char] = 1
    return (counts)


#def sort_on(tosort):
  #  return tosort["num"]


def make_list(dict):
    listofdict = [{key:value} for key, value in dict.items()]
    sortedlist = sorted(listofdict, key=lambda d: list(d.values())[0], reverse=True)
    for entry in sortedlist:
        for key, value in entry.items():
            print (f"{key}: {value}")

    
   
    