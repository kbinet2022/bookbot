from stats import get_word_count
from stats import get_character_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():

    # places text of book into string
    path_to_file = "./books/frankenstein.txt"
    unfiltered_text = get_book_text(path_to_file)

    num_words = get_word_count(unfiltered_text)
    print(f"{num_words} words found in the document")
    num_letters = get_character_count(unfiltered_text)
    print(num_letters)

main()