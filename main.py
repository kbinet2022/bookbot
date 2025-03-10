from stats import get_word_count
from stats import get_character_count
from stats import reorganize_dictionary
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_report(path_to_file, num_words, dictionary_list):
        print("============ BOOKBOT ============")

        print(f"Analyzing book found at {path_to_file}...")

        print("----------- Word Count ----------")
        print(f"Found {num_words} total words" )

        print("--------- Character Count -------")
        for dict in dictionary_list:
             print(f"{dict["letter"]}: {dict["num"]}")


def main():


    # places text of book into string
    if sys.argv[1] != None:
        path_to_file = sys.argv[1]
    else:
         print("Usage: python3 main.py ./books/<bookname.txt>")
         sys.exit(1)

    unfiltered_text = get_book_text(path_to_file)


    # counts the amount of times each letter appears in the text
    num_words = get_word_count(unfiltered_text)
    character_dict = get_character_count(unfiltered_text)
    
    # rearrange and sort dictionary
    dictionary_list = reorganize_dictionary(character_dict)
    
    # Prints report
    print_report(path_to_file, num_words, dictionary_list)


main()