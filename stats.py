def get_word_count(text):
    return len(text.split())

def get_chars_dict(text):
    chars_dict = {}
    for char in text:
        c = char.lower()
        if c in chars_dict:
            chars_dict[c] += 1
        else:
            chars_dict[c] = 1

    return chars_dict

def sort_on_num(dict):
    return dict["num"]

def get_chars_dict_list(chars_dict):
    chars_dict_list = []
    for c in chars_dict:
        chars_dict_list.append({"char": c, "num": chars_dict[c]})
    chars_dict_list.sort(reverse=True, key=sort_on_num)
    return chars_dict_list