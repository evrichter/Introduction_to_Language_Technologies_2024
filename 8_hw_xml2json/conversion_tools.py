import xml.etree.ElementTree as ET
import json
import csv

file_name = "sample"


def convert_xml_to_json(file_name_to_convert):
    json_name = file_name + ".json"

    tree = ET.parse(file_name_to_convert)
    root = tree.getroot()

    sentences = []

    for sentence in root.findall("sentence"):
        sentence_text = sentence.get("text")
        words = []

        for word in sentence.findall("word"):
            word_id = word.get("id")
            word_form = word.get("form")
            word_lemma = word.get("lemma")
            word_upos = word.get("upos")
            word_head = word.get("head")

            word_dict = {}

            word_dict["id"] = word_id
            word_dict["form"] = word_form
            word_dict["lemma"] = word_lemma
            word_dict["upos"] = word_upos
            word_dict["head"] = word_head

            words.append(word_dict)

        sentences.append({
                "text": sentence_text,
                "words": words
        })

    with open(json_name, "w", encoding="utf-8") as json_out:
        json.dump({"sentences": sentences}, json_out, indent=4, ensure_ascii=False)




def convert_json_to_tsv(file_name_to_convert):
    final_tsv_name = file_name + ".tsv"

    with open(file_name_to_convert, "r", encoding="utf-8") as json_in:
        data = json.load(json_in)

    lines = []

    for sentence in data["sentences"]:
        lines.append(f"# sentence-text: {sentence['text']}")

        for word in sentence["words"]:
            lines.append("\t".join([
                word["id"], word["form"], word["lemma"], word["upos"], word["head"]
            ]))
        
        lines += " "

    with open(final_tsv_name, "w", encoding="utf-8") as tsv_out:
        tsv_out.write("\n".join(lines) + "\n")




def convert_tsv_to_xml(file_name_to_convert):
    with open(file_name_to_convert, "r", encoding="utf-8") as tsv:
        lines = tsv.readlines()

    root = ET.Element("sentences")

    sentence_element = None

    for line in lines:
        line = line.strip()

        if line.startswith("# sentence-text:"):
            sentence_text = line.replace("# sentence-text: ", "")
            sentence_element = ET.SubElement(root, "sentence", text=sentence_text)
        elif line != "":
            cols = line.split("\t")
            word_id, form, lemma, upos, head = cols

            ET.SubElement(
                sentence_element,
                "word",
                id=word_id,
                form=form,
                lemma=lemma,
                upos=upos,
                head=head
            )

    tree = ET.ElementTree(root)
    tree.write(file_name + ".xml", encoding="utf-8", xml_declaration=True)





def present_report():
    print("""
        The Python script was implemented using xml.etree.ElementTree for XML processing and the json module for JSON handling.
        The conversions were implemented in three main functions: convert_tsv_to_xml, convert_xml_to_json, and convert_json_to_tsv. 
        TSV sentences were parsed line-by-line. Sentence headers (sentence-text) became <sentence> elements with a text attribute, 
        and word rows were nested <word> elements with attributes like id, form, lemma, upos, and head. The XML elements were parsed into 
        a Python dictionary with sentences containing text and words. The JSON data was converted back to TSV, writing sentence texts as 
        comments and word attributes as tab-separated rows.
        """)
    




def check(file_to_compare):
    with open(file_to_compare, 'r', encoding='utf-8') as f1, open(file_name + ".tsv", 'r', encoding='utf-8') as f2:
        reader1 = csv.reader(f1, delimiter='\t')
        reader2 = csv.reader(f2, delimiter='\t')

        for line_num, (row1, row2) in enumerate(zip(reader1, reader2), start=1):
            if row1 != row2 and row2[0] != " ":
                print("ERROR")
                return False
        
        if any(reader1) or any(reader2):
            print("ERROR")
            return False

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert between TSV, XML, and JSON formats.")
    parser.add_argument("operation", choices=["tsv2xml", "xml2json", "json2tsv", "check", "report"])
    parser.add_argument("input", nargs="?", help="Input file", default=None)

    args = parser.parse_args()

    if args.operation == "tsv2xml":
        convert_tsv_to_xml(args.input)
    elif args.operation == "xml2json":
        convert_xml_to_json(args.input)
    elif args.operation == "json2tsv":
        convert_json_to_tsv(args.input)
    elif args.operation == "check":
        check(args.input)
    elif args.operation == "report":
        present_report()