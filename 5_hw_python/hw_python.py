input_text = "In the beginning God created the heavens and the earth. And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters. And God said, Let there be light: and there was light. And God saw the light, that it was good: and God divided the light from the darkness. And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day. And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters. And God made the firmament, and divided the waters which were under the firmament from the waters which were above the firmament: and it was so. And God called the firmament Heaven. And the evening and the morning were the second day. And God said, Let the waters under the heaven be gathered together unto one place, and let the dry land appear: and it was so. And God called the dry land Earth; and the gathering together of the waters called he Seas: and God saw that it was good. And God said, Let the earth bring forth grass, the herb yielding seed, and the fruit tree yielding fruit after his kind, whose seed is in itself, upon the earth: and it was so. And the earth brought forth grass, and herb yielding seed after his kind, and the tree yielding fruit, whose seed was in itself, after his kind: and God saw that it was good. And the evening and the morning were the third day. And God said, Let there be lights in the firmament of the heaven to divide the day from the night; and let them be for signs, and for seasons, and for days, and years: And let them be for lights in the firmament of the heaven to give light upon the earth: and it was so. And God made two great lights; the greater light to rule the day, and the lesser light to rule the night: he made the stars also. And God set them in the firmament of the heaven to give light upon the earth, And to rule over the day and over the night, and to divide the light from the darkness: and God saw that it was good. And the evening and the morning were the fourth day. And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl that may fly above the earth in the open firmament of heaven. And God created great whales, and every living creature that moveth, which the waters brought forth abundantly, after their kind, and every winged fowl after his kind: and God saw that it was good. And God blessed them, saying, Be fruitful, and multiply, and fill the waters in the seas, and let fowl multiply in the earth. And the evening and the morning were the fifth day. And God said, Let the earth bring forth the living creature after his kind, cattle, and creeping thing, and beast of the earth after his kind: and it was so. And God made the beast of the earth after his kind, and cattle after their kind, and every thing that creepeth upon the earth after his kind: and God saw that it was good. And God said, Let us make man in our image, after our likeness: and let them have dominion over the fish of the sea, and over the fowl of the air, and over the cattle, and over all the earth, and over every creeping thing that creepeth upon the earth. So God created man in his own image, in the image of God created he him; male and female created he them. And God blessed them, and God said unto them, Be fruitful, and multiply, and replenish the earth, and subdue it: and have dominion over the fish of the sea, and over the fowl of the air, and over every living thing that moveth upon the earth. And God said, Behold, I have given you every herb bearing seed, which is upon the face of all the earth, and every tree, in the which is the fruit of a tree yielding seed; to you it shall be for meat. And to every beast of the earth, and to every fowl of the air, and to every thing that creepeth upon the earth, wherein there is life, I have given every green herb for meat: and it was so. And God saw every thing that he had made, and, behold, it was very good. And the evening and the morning were the sixth day."

# read the genesis file
# with open("/genesis.txt", "r") as file:
#     input_text = file.read()
#     #print(input_text) 

def print_into_file(task_result, filename):
    with open(filename, "w") as outputfile:
        print(task_result, file=outputfile)



### TOKENS ###
# task 1: print number of characters
def number_of_characters(text):
    character_number = len(text)
    return character_number

task_1_result = number_of_characters(input_text)
print_into_file(task_1_result, "t1.txt")


# task 2: split into tokens
def split_into_tokens(text):
    token_split = text.split(" ")[:20]
    return "\n".join(token_split)

task_2_result = split_into_tokens(input_text)
print_into_file(task_2_result, "t2.txt")


# task 3: print number of tokens
def number_of_tokens(text):
    token_split = text.split(" ")
    token_number = len(token_split)
    return token_number

task_3_result = number_of_tokens(input_text)
print_into_file(task_3_result, "t3.txt")


# task 4: print first three characters from each token
def first_three_characters(text):
    token_split = text.split(" ")
    result = ""

    for token in token_split:
        result += token[:3] + " "

    return result

task_4_result = first_three_characters(input_text)
print_into_file(task_4_result, "t4.txt")


# task 5: print last two characters from first 20 tokens
def last_two_characters(text):
    token_split = text.split(" ")
    result = ""

    for token in token_split[:20]:
        result += token[-2:] + " "

    return result

task_5_result = last_two_characters(input_text)
print_into_file(task_5_result, "t5.txt")


# task 6: compute the average word length
def average_word_length(text):
    token_split = text.split(" ")
    average_length = round(sum(len(word) for word in token_split) / len(token_split), 2)
    return average_length

task_6_result = average_word_length(input_text)
print_into_file(task_6_result, "t6.txt")


# task 7: create a frequency list of words
def word_frequency_list(text):
    token_split = text.split(" ")
    word_count = {}
    for word in token_split:
        word_lower = word.lower()
        if word_lower in word_count:
            word_count[word_lower] += 1 
        else:
            word_count[word_lower] = 1 

    sorted_list = sorted(word_count, key=word_count.get, reverse=True)
    most_frequent_word = sorted_list[0]

    return most_frequent_word

task_7_result = word_frequency_list(input_text)
print_into_file(task_7_result, "t7.txt")


# task 8: print most frequent non-space character
def most_frequent_character(text):
    characters = [character for character in text]
    character_count = {}
    for character in characters:
        character = character.lower()
        if character != " ":
            if character in character_count:
                character_count[character] += 1 
            else:
                character_count[character] = 1

    sorted_list = sorted(character_count, key=character_count.get, reverse=True)
    most_frequent_character = sorted_list[0]

    return most_frequent_character

   
task_8_result = most_frequent_character(input_text)
print_into_file(task_8_result, "t8.txt")



### SENTENCES ###
# task 1: split into sentence
def split_into_sentences(text):
    sentences = text.split('. ')
    result = ""

    for sentence in sentences:
        result += sentence.rstrip().rstrip('.') + "\n"

    return result

task_1_result = split_into_sentences(input_text)
print_into_file(task_1_result, "s1.txt")


# task 2: print number of sentences
def number_of_sentences(text):
    sentences = text.split('. ') 
    return len(sentences)

task_2_result = number_of_sentences(input_text)
print_into_file(task_2_result, "s2.txt")


# task 3: print number of characters in a sentence
def number_of_characters(text):
    sentences = text.split('. ')
    character_count = []

    for sentence in sentences:
        sentence = sentence.strip(".")
        sentence_characters = list(sentence)
        sentence_length = len(sentence_characters)
        character_count.append(str(sentence_length))

    result = " ".join(character_count)

    return result

task_3_result = number_of_characters(input_text)
print_into_file(task_3_result, "s3.txt")

# task 4: create list of sentences where each sentence is a list of its tokens
def list_of_sentences(text):
    sentences = text.split('. ')
    list_of_sentences = []
 
    for sentence in sentences:
        sentence = sentence.strip(".")
        list_of_tokens = sentence.split()
        list_of_sentences.append(list_of_tokens)
       
    return list_of_sentences

task_4_result = list_of_sentences(input_text)
print_into_file(task_4_result, "s4.txt")


# task 5: print number of words in each sentence
def number_of_words(text):
    sentences = text.split('. ')
    word_count = ""

    for sentence in sentences:
        words_in_sentence = sentence.split()
        word_length = len(words_in_sentence)
        word_count += str(word_length) + " "

    return word_count

task_5_result = number_of_words(input_text)
print_into_file(task_5_result, "s5.txt")


# task 6: compute average sentence length in terms of words
def average_sentence_length_words(text):
    sentences = text.split('. ')
    word_count = 0

    for sentence in sentences:
        words_in_sentence = sentence.split()
        word_length = len(words_in_sentence)
        word_count += word_length

    return round(word_count/len(sentences), 2)

task_6_result = average_sentence_length_words(input_text)
print_into_file(task_6_result, "s6.txt")


# task 7: compute average sentence length in terms of characters
def average_sentence_length_characters(text):
    sentences = text.split('. ')
    character_count = 0

    for sentence in sentences:
        sentence = sentence.strip(".").strip()
        characters_in_sentence = list(sentence)
        sentence_length_characters = len(characters_in_sentence)
        character_count += sentence_length_characters

    return round(character_count/len(sentences), 2)

task_7_result = average_sentence_length_characters(input_text)
print_into_file(task_7_result, "s7.txt")


# task 8: print the first two words from each sentence
def first_two_words(text):
    sentences = text.split('. ')
    result = ""

    for sentence in sentences:
        words_in_sentence = sentence.split()
        first_two_words = ' '.join(words_in_sentence[:2])
        result += first_two_words + " \n"

    return result

task_8_result = first_two_words(input_text)
print_into_file(task_8_result, "s8.txt")


# task 9: print the first character from the second word in the third sentence
def first_character(text):
    sentences = text.split('. ')

    third_sentence = sentences[2]
    third_sentence_second_word = third_sentence.split()[1]
    third_sentence_second_word_first_character = third_sentence_second_word[0]

    return third_sentence_second_word_first_character

task_9_result = first_character(input_text)
print_into_file(task_9_result, "s9.txt")
