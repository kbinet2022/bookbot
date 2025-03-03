from stats import get_word_count
from stats import get_character_count
from stats import sort_dictionary
from stats import reorganize_dictionary

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_report(path_to_file, num_words):
        print("============ BOOKBOT ============")
        print("Analyzing book found at" + path_to_file)

        print("----------- Word Count ----------")
        print(f"Found {num_words} total words" )

        print("--------- Character Count -------")
        print()

def main():


    # places text of book into string
    path_to_file = "./books/frankenstein.txt"
    unfiltered_text = get_book_text(path_to_file)


    # counts the amount of times each letter appears in the text
    num_words = get_word_count(unfiltered_text)
    character_dict = get_character_count(unfiltered_text)
    
    # Finalizes a report
    dictionary_list = reorganize_dictionary(character_dict)
    print()
    

    # Prints report
    print_report(path_to_file, num_words)


main()