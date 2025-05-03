def get_num_words(words):

    total_words = words.split()
    return len(total_words)


def count_characters(text):
    count_dictionary = {}
    lowercase_text = text.lower()

    print("checking something out:  ")
    for char in lowercase_text:
        if char in count_dictionary:
            count_dictionary[char] += 1
        else:
            count_dictionary[char] = 1;

    return count_dictionary

def sort_on(dict):
    return dict["num"]

def sort_dictionary(the_char_dictionary):
    sorted_list = []
    for ch in the_char_dictionary:
        sorted_list.append({"char": ch, "num": the_char_dictionary[ch]})
    
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
