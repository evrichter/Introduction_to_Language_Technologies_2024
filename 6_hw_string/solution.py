import sys
from collections import Counter
import argparse
from typing import Optional
import re as regex

parser = argparse.ArgumentParser()
parser.add_argument("input_file", nargs='?', default=None, type=str, help="Path to the input file")

def print_into_file(task_result, filename):
    with open(filename, "w") as outputfile:
        print(task_result, file=outputfile)

# task 1: print number of characters
def spaces_to_underscores(text):
    result = text.replace(" ", "_")
    return result

# task 2: print lines on which all letters are uppercase
def uppercase_lines(text):
    lines = text.split("\n")
    upper_lines = ""
    
    for line in lines:
        if line == line.upper():
            upper_lines += line + "\n"
    return upper_lines

# task 3: split the text into words
def split_into_words(text):
    words = regex.split(r'[^\w]+', text)
    result = ""

    for word in words:
        if word in words:
            result += word + "\n"

    return result

# task 4: find words containing at least two subsequent vowels
def two_subsequent_vowels(text):
    return "\n".join(word for word in text.split() if regex.search(r'[aeiouyAEIOUY]{2}', word))

# task 5: remove stop words
def stop_words_removal(text):
    text = text.lower()  # lower case everything
    words = regex.split(r'[^\w]+', text)  # split by words and remove punctuation
    word_count_dict = {}

    for word in words:  # add words as keys and their frequency count as values to a dictionary
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1

    list_of_stop_words = []  # create a list of stop words, containing all words with a frequency count >= 10
    for word in word_count_dict:
        if word_count_dict[word] >= 10:
            list_of_stop_words.append(word)
    
    words_to_keep = ""  # keep all words that are not in the list of stop words
    for word in words:
        if word not in list_of_stop_words:
            words_to_keep += word + "\n"  # print each word on a separate line
    
    return words_to_keep


# task 6: convert arabic numbers to roman numbers
def replace_with_roman(match):
    number = int(match.group(0))
    if number <= 2000:
        return arabic_to_roman(number)
    else:
        return match.group(0)

def arabic_to_roman(number):
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result = ""
    for (arabic, roman) in roman_numerals:
        while number >= arabic:
            result += roman
            number -= arabic
    return result

def process_text_with_same_lines(text):
    # Process each line separately to maintain line structure
    lines = text.splitlines()
    processed_lines = [regex.sub(r'\b\d+\b', replace_with_roman, line) for line in lines]
    return "\n".join(processed_lines)

# task 7: create new lines after 40th character
def new_lines(input_text):
    text = ' '.join(input_text.split())
    result = []
    i = 0
    
    while i < len(text):
        if i + 40 >= len(text):
            result.append(text[i:])
            break
        
        break_point = text.find(' ', i + 40)
        
        if break_point == -1:
            result.append(text[i:])
            break
        
        result.append(text[i:break_point])
        i = break_point + 1
    
    return '\n'.join(result)

# Main function to process the file
def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    task_1_result = spaces_to_underscores(text)
    print_into_file(task_1_result, filename + ".1")

    task_2_result = uppercase_lines(text)
    print_into_file(task_2_result, filename + ".2")

    task_3_result = split_into_words(text)
    print_into_file(task_3_result, filename + ".3")

    task_4_result = two_subsequent_vowels(text)
    print_into_file(task_4_result, filename + ".4")

    task_5_result = stop_words_removal(text)
    print_into_file(task_5_result, filename + ".5")

    task_6_result = process_text_with_same_lines(text)
    print_into_file(task_6_result, filename + ".6")

    task_7_result = new_lines(text)
    print_into_file(task_7_result, filename + ".7")

def main(args: argparse.Namespace) -> Optional[str]:
    if args.input_file is None:
        report = """
        Report: 

        - Regular expressions were used for task 3 to split the text into words by identifying non-word characters as delimiters, 
          for task 4 to match words with at least two consecutive vowels and for task 6 to find Arabic numbers in the text.
          Moreover, to convert Arabic numbers to Roman numbers in task 6, the largest possible Roman numeral value (e.g., 1000 for "M", 900 for "CM") 
          is subtracted from the input number, appending the corresponding Roman numeral symbol to the result string until the input number is reduced to zero. 
        - No regular expressions were used for task 1, which can be solved with a straightforward string replacement, for task 2, since checking if a line is 
          uppercase can be done with a simple comparison (line == line.upper() and for task 7 to split the text based on character positions and spaces, 
          which can be done using slicing operations. While regex is used to split the text into words for task 5, the primary logic of filtering words based 
          on frequency does not rely on regex. Instead, a dictionary and iteration were used for this task.
        - Vowels were defined using a regular expression pattern that included both lowercase and uppercase vowel characters. 
          The vowels defined in the pattern [aeiouyAEIOUY] primarily correspond to English vowels, as they include the standard English vowels (a, e, i, o, u) 
          along with y, which is sometimes treated as a vowel in English.
        - The solution was tested on English, Turkish, and Russian texts from the UDHR corpus.
        - For the English text, the solution works for all tasks.
        - For the Turkish text, the solution performs well for nearly all tasks. However, in task 5, while stop words are successfully removed, the solution 
          incorrectly splits the words "insan" and "insanlık" into two parts ("i" and "san"/"sanlık").
          The file "trk.2" is empty because the Turkish document does not begin with the capitalized term "PREAMBLE" as in the English version, 
          resulting in no lines containing only uppercase letters.
        - For the Russian text, task 4 does not work because the defined vowels do not include Cyrillic vowels. While adding Cyrillic vowels would fix this, 
          it would still cause tests for other languages to fail unless vowels from all languages are included.
        - Unlike the English and Turkish texts, the Russian text also contains numbers (e.g., 1948, December 10), which are treated as words in all tasks. 
          Additionally, the Russian text includes a Roman numeral (III) that is treated as a vowel ("I") and, as a result, is mistakenly identified as a sequence of vowels in task 4.
        """
        
        print(report)
    else:
        input_filename = args.input_file
        process_file(input_filename)

if __name__ == "__main__":
    main_args = parser.parse_args()
    main(main_args)
