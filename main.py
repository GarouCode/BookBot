def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

book_string = main()

def word_count(book_string):
    words = book_string.split()
    return words

num_of_words = word_count(book_string)

def character_count(book_string):
    chars = {}
    for c in book_string:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

character_dictionary = character_count(book_string)

def print_report(book_string, num_of_words, character_dictionary):
    print("****** Beginning report of frankenstein.txt ******")
    print(f"{len(num_of_words)} words found in the document")
    
    # sorted_characters = sorted(character_dictionary.items(), key=lambda item: item[1], reverse=True )
    for key, value in character_dictionary.items():
        if key.isalpha():
            print(f"The letter '{key}' was found {value} times")
    print("*** End of Report ***")


main()
word_count(book_string)
character_count(book_string)
print_report(book_string, num_of_words, character_dictionary)