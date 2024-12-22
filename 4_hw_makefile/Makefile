# download the skakalpes-il2.txt file

skakalpes-il2.txt:


	@wget -q https://ufal.mff.cuni.cz/~zabokrtsky/courses/npfl125/data/skakalpes-il2.txt

convert: 
	@iconv -f ISO-8859-2 -t UTF-8 skakalpes-il2.txt -o skakalpes-il2-utf8.txt

# Target t1: Prints "Hello world"

t1:
	@echo "Hello world"

# Target t2: view file using cat

t2: 

	@cat skakalpes-il2.txt

# Target t3: convert the skakalpes-il2.txt file from iso-8859-2 to utf-8

t3: 
	@iconv -f ISO-8859-2 -t UTF-8 skakalpes-il2.txt

# Target t4: count the number of lines

t4:
	@wc -l < skakalpes-il2.txt 

# Target t5: count the number of words

t5: convert
	@wc -w < skakalpes-il2-utf8.txt 

# Target t6: print the first 15 lines  

t6: convert
	@head -n 15 skakalpes-il2-utf8.txt

# Target t7: print the last 15 lines

t7: convert

	@tail -n 15 skakalpes-il2-utf8.txt 

# Target t8: print lines 10-20

t8: convert

	@sed -n '10,20p' skakalpes-il2-utf8.txt

# Target t9: print the first two words on each line

t9: convert

	@cut -d' ' -f1-2 skakalpes-il2-utf8.txt

# Target t10: print all lines containing a digit

t10: convert

	@grep -a '[0-9]' skakalpes-il2-utf8.txt

# Target t11: substitute each space and punctuation mark with a new line symbol

t11: convert

	@sed 's/[[:space:][:punct:]]/\n/g' skakalpes-il2-utf8.txt

# Target t12: print a list of words avoiding empty lines

t12: convert

	@sed 's/[[:space:][:punct:]]/\n/g' skakalpes-il2-utf8.txt | grep -v '^$$'

# Target t13: print word list sorted alphabetically

t13: convert

	@sed 's/[[:space:][:punct:]]/\n/g' skakalpes-il2-utf8.txt | grep -v '^$$' | sort

# Target t14: count number of words in text where each line corresponds to one word

t14: convert

	@sed 's/[[:space:][:punct:]]/\n/g' skakalpes-il2-utf8.txt | grep -v '^$$' | wc -l

# Target t15: count number of distinct words in the text

t15: convert

	@sed 's/[[:space:][:punct:]]/\n/g' skakalpes-il2-utf8.txt | grep -v '^$$' | sort | uniq | wc -l

# Target t16: create a frequency list of words
	
t16: convert

	@sed 's/[[:space:][:punct:]]/\n/g' skakalpes-il2-utf8.txt | grep -v '^$$' | sort | uniq -c | sort -nr

# Target t17: create a frequency list of alphabetic letters

t17: convert
	
	#@tr -cd '[:alpha:]' < skakalpes-il2-utf8.txt | tr '[:upper:]' '[:lower:]' | fold -w1 | sort | uniq -c | sort -nr

	@grep -o '[[:alpha:]]' skakalpes-il2-utf8.txt | sed 's/.*/\L&/' | sort | uniq -c | sort -nr


# Target t18: create frequency list of bigrams

t18: convert

	@tr -sc "[A-Z][a-z]" "\n" < skakalpes-il2-utf8.txt > skakalpes-il2-utf8.words
	@tail -n +2 skakalpes-il2-utf8.words > skakalpes-il2-utf8.nextwords

	@paste skakalpes-il2-utf8.words skakalpes-il2-utf8.nextwords | sort | uniq -c | sort -nr > skakalpes-il2-utf8.bigrams
	@cat skakalpes-il2-utf8.bigrams


# Download the html file

example.html:
	@wget -O example.html https://ufal.mff.cuni.cz


# Target 19: find capitalized word bigrams in example.html

t19:

	@grep -oP '\b[A-Z]+\b' example.html > capitalized.words
	@tail -n +2 capitalized.words > capitalized.nextwords
	
	@paste capitalized.words capitalized.nextwords | grep -P '\t' > capitalized.bigrams
	@cat capitalized.bigrams


# Target t20: create target that generates frequency list of HTML element names

t20:

	@grep -oP '<\s*([a-zA-Z0-9]+)' example.html | sed 's/<\s*//' | sort | uniq -c | sort -nr > html_element_frequency.txt
	@cat html_element_frequency.txt






