import spacy

def main():
    # Load the trained model
    try:
        nlp = spacy.load("models/model-best")
    except Exception as e:
        print("Error loading model. Ensure the model is trained and the path is correct.")
        print(str(e))
        return

    # sample sentences
    sentences = [
        "Das ist ein Beispiel.",
        "Ich liebe es, neue Modelle zu trainieren.",
        "SpaCy ist ein großartiges Tool für NLP."
    ]

    # Process and display results
    for sentence in sentences:
        doc = nlp(sentence)
        print(f"Sentence: {sentence}")
        print("Tokens and Predictions:")
        for token in doc:
            print(f"  {token.text:15} AG: {token.tag_}")
        print("-" * 40)


if __name__ == "__main__":
    main()
