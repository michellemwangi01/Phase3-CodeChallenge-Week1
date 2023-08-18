import re
def highest_consonant_value(word):
    vowels = 'aeiou'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_word = re.sub('[aeiou]', '|', word)
    word_list = new_word.split('|')
    char_value_list = []
    for chars in word_list:
        char_value = sum([alphabet.find(char)+1 for char in chars])
        char_value_list.append(char_value)
    return f'Highest consonant value in {new_word} is: {max(char_value_list)}'


print(highest_consonant_value("strength"))







# max_value = max(char_value_dict.values())
# vowel_less_word = ''.join([char for char in word if char not in vowels])
# index_values.append({char:char_index + 1})




