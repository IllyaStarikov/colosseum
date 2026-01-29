def find_repeated(string, length):
    length_of_string = len(string)
    assert length_of_string != 0

    search_character = 'a'
    number_of_search_character_in_string = sum(map(lambda character: 1 if character == search_character else 0, string))

    without_truncated_string = number_of_search_character_in_string * (length // length_of_string)
    truncated_string = sum(map(lambda character: 1 if character == search_character else 0, string[:length % length_of_string]))

    return without_truncated_string + truncated_string


string = input()
length = int(input())

print(find_repeated(string, length))