def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_dict(dict):
    list_of_dicts = []
    for key in dict:
        hold_dict = {}
        hold_dict["name"] = key
        hold_dict["num"] = dict[key]
        list_of_dicts.append(hold_dict)
    list_of_dicts.sort(key=lambda n : n["num"], reverse=True)
    return list_of_dicts