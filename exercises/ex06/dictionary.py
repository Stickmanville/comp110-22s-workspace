"""EX06. Fun with dictionaries."""

__author__ = "730332997"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, returns a dictionary with the keys and values swapped."""
    new_dict: dict[str, str] = {}
    key_list: list[str] = []
    for word in dictionary:
        if dictionary[word] in key_list:
            raise KeyError()
        new_dict[dictionary[word]] = word
        key_list.append(dictionary[word])
    return new_dict


def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns a str which is the most repeated value."""
    color_index: dict[str, int] = {}
    output: str = ""
    max: int = 0
    max_color: str = ""
    for word in dictionary:
        if dictionary[word] in color_index:
            color_index[dictionary[word]] += 1
        else:
            color_index[dictionary[word]] = 1
    print(color_index)
    for color in color_index:
        if color_index[color] > max:
            max = color_index[color]
            max_color = color
    output = max_color
    return output


def count(a_list: list[str]) -> dict[str, int]:
    """Given a list, returns a dictionary where each value is the number of times it's key appeared in the input list."""
    color_index: dict[str, int] = {}
    for word in a_list:
        if word in color_index:
            color_index[word] += 1
        else:
            color_index[word] = 1
    return color_index
