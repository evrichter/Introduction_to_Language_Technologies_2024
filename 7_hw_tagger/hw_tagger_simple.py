import sys
from collections import defaultdict

def read_training_data(training_file):
    word_tag_dict = defaultdict(list)
    tag_freq = defaultdict(int)
    
    with open(training_file, 'r', encoding='iso-8859-2') as f:
        for line in f:
            line = line.strip()
            if line:
                word, tag = line.split('\t')
                word_tag_dict[word].append(tag)
                tag_freq[tag] += 1
    
    most_frequent_tag = max(tag_freq, key=tag_freq.get)
    return word_tag_dict, most_frequent_tag

def predict_pos_tag(word_tag_dict, most_frequent_tag, word):
    if word in word_tag_dict:
        return max(word_tag_dict[word], key=word_tag_dict[word].count)
    else:
        if word.endswith("a") or word.endswith("e") or word.endswith("o"):
            return "N"
        elif word.endswith("y") or word.endswith("i"):
            return "N"
        elif word.endswith("t"):
            return "V"
        elif word.endswith("l"):
            return "V"
        elif word.endswith("me") or word.endswith("te"):
            return "V"
        elif word.endswith("ý") or word.endswith("á") or word.endswith("é"):
            return "N"
        elif word.endswith("ě") or word.endswith("e"):
            return "R"
        elif word.isdigit():
            return "C"
        elif word in [".", ",", "!", "?"]:
            return "Z"
        elif word.lower() in ["já", "ty", "on", "my", "vy", "oni"]:
            return "P"
        else:
            return most_frequent_tag

def evaluate_tagging(test_file, word_tag_dict, most_frequent_tag):
    correct = 0
    total = 0
    
    with open(test_file, 'r', encoding='iso-8859-2') as f:
        for line in f:
            line = line.strip()
            if line:
                word, true_tag = line.split('\t')
                predicted_tag = predict_pos_tag(word_tag_dict, most_frequent_tag, word)
                if predicted_tag == true_tag:
                    correct += 1
                total += 1
    
    return round(100 * correct / total, 2)

def predict_tagging(test_file, word_tag_dict, most_frequent_tag):
    with open(test_file, 'r', encoding='iso-8859-2') as f:
        for line in f:
            word = line.strip()
            if word:
                predicted_tag = predict_pos_tag(word_tag_dict, most_frequent_tag, word)
                print(predicted_tag)
            else:
                print('')

def main():
    if len(sys.argv) != 4:
        print("Usage: python tagger.py <trainingfile> <testfile> <PREDICT|EVAL>")
        sys.exit(1)
    
    training_file = sys.argv[1]
    test_file = sys.argv[2]
    mode = sys.argv[3]

    word_tag_dict, most_frequent_tag = read_training_data(training_file)
    
    if mode == "EVAL":
        accuracy = evaluate_tagging(test_file, word_tag_dict, most_frequent_tag)
        print(accuracy)
    elif mode == "PREDICT":
        predict_tagging(test_file, word_tag_dict, most_frequent_tag)
    else:
        print("Invalid mode. Use PREDICT or EVAL.")
        sys.exit(1)

if __name__ == "__main__":
    main()
