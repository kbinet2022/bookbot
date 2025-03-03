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
