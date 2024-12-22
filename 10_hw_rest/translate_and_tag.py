import requests
import re

def main():
    text_to_translate = input("Please, enter the English text to be translated to Czech: ")
    
    translated_text = translate(text_to_translate)
    
    formated_translated_text = format_translation(translated_text)
    print("Czech Translation: ",formated_translated_text, "\n")
    
    tagged_text = tagger(formated_translated_text)

    formatted_tagged_text = format_tagger(tagged_text)
    print(f"{"Word".ljust(20)} {"Tag".ljust(10)}\n")
    print(formatted_tagged_text)


def translate(input_text):
    # Endpoint URL
    url = "https://lindat.mff.cuni.cz/services/transformer/api/v2/models/en-cs"
    
    # Query parameters
    params = {"src": "en", "tgt": "cs"}
    
    # Form data
    data = {"input_text": input_text}
    
    # Headers
    headers = {"Content-Type": "application/x-www-form-urlencoded","Accept": "application/json"}
    
    # Send POST request
    response = requests.post(url, headers=headers, params=params, data=data)
    
    # Handle response
    if response.status_code == 200:
        return response.json()  # Returns the translated text
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


# Remove newline characters
def format_translation(translation):
    # Check if translation is a list and contains at least one element
    if translation and isinstance(translation, list) and len(translation) > 0:
        return " ".join(translation)
    # if no valid translation return empty string
    return ""  


def tagger(translated_input_text):
    # Endpoint URL for UDPipe (Czech model)
    url = "https://lindat.mff.cuni.cz/services/udpipe/api/process"

    # Parameters for UDPipe processing
    params = {
        "model": "czech-cltt-ud-2.15-241121",  
        "tokenizer": "false",
        "tagger": "true"  
        #"parser": "false"   
    }
    
    # Form data
    data = {"data": translated_input_text} 
    
    # Headers
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}
    
    # Send POST request
    response = requests.post(url, headers=headers, params=params, data=data)
    
    # Handle response
    if response.status_code == 200:
        return response.json()  # Returns the UDPipe analysis result
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


# Extract only POS tags and print the words and corresponding tags line by line 
def format_tagger(tagged_input_text):
    formatted_tagged_input_text = re.search("# text = (.*)", tagged_input_text["result"], re.DOTALL)

    # If the text part is found:
    if formatted_tagged_input_text:
        formatted_tagged_input_text =  formatted_tagged_input_text.group(1)

        lines = formatted_tagged_input_text.split("\n")

        words_and_tags = ""

        for line in lines:
            parts = line.split("\t")

            if len(parts) >= 4:
                word = parts[1]
                tag = parts[3]
                words_and_tags += f"{word.ljust(20)} {tag.ljust(10)}\n"

                # Make output format mor readable
                if tag == "PUNCT" and word == ".":
                    words_and_tags += "---------------------------\n"

    return words_and_tags

main()