def get_word_count(unfiltered_text):
    word_list = []
    word_list = unfiltered_text.split()
    num_words = len(word_list)
    return num_words

def get_character_count(unfiltered_text):
    letter_count = {}
    for character in unfiltered_text.lower():
        if character in letter_count:
            letter_count[character] += 1
        else:
            letter_count[character] = 1
    return letter_count

def sort_dictionary(dictionary):
    return dictionary["num"]

def reorganize_dictionary(dictionary):

    dictionary_list = []
    for key, value in dictionary.items():
        if key.isalpha() == True:
            new_dict = {"letter": key, "num": value}
            dictionary_list.append(new_dict)
    
    dictionary_list.sort(reverse=True, key=sort_dictionary)
    return dictionary_list