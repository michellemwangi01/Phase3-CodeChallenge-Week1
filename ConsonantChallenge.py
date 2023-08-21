# Challenge 3: Consonant value
# Given a lowercase string that has alphabetic characters only and no spaces,
# return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".
# We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.
import re


def highest_consonant_value(word):
    vowels = 'aeiou'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_word = re.sub('[aeiou]', '|', word.lower())
    word_list = new_word.split('|')
    char_value_list = []
    for chars in word_list:
        char_value = sum([alphabet.find(char) + 1 for char in chars])
        char_value_list.append(char_value)
    return f'Highest consonant value in {word} is: {max(char_value_list)}'


while True:
    your_string = input("Enter a string: ")
    if your_string.isalpha():
        break
    else:
        print("Error! Your Input Must Be A String With No Special Characters Or Spaces.")

print(highest_consonant_value(your_string))


# max_value = max(char_value_dict.values())
# vowel_less_word = ''.join([char for char in word if char not in vowels])
# index_values.append({char:char_index + 1})
