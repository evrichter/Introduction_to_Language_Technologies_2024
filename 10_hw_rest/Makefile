# Print the readme for the program usage
readme:
	@echo "============================================="
	@echo "English-to-Czech Translation and POS Tagging"
	@echo "============================================="
	@echo "This program translates English text to Czech and performs part-of-speech tagging on the translated text." | fold -s -w 80
	@echo "The program uses the UDPipe API for POS tagging and a Czech-English Transformer model for translation." | fold -s -w 80
	@echo ""
	@echo "For more information about the services used, visit:"
	@echo "   - UDPipe: https://ufal.mff.cuni.cz/udpipe"
	@echo "   - Transformer: https://lindat.mff.cuni.cz/services/transformer/"
	@echo ""
	@echo "Usage:"
	@echo "1. To run the translation and POS tagging program, use the following command:"
	@echo "   'make run'"
	@echo ""
	@echo "   You will be prompted to input English text, which will be translated to Czech" 
	@echo "   and tagged with part-of-speech labels." 
	@echo ""
	@echo "2. To see this README again, use:"
	@echo "   'make readme'"
	@echo ""
	@echo "Make sure you have Python 3 and the required dependency installed."
	@echo "Install dependency using pip with the following command:"
	@echo "   pip install requests"
	@echo ""


# Run the Python program
run:
	python3 translate_and_tag.py
	

# Help command to show available targets
help:
	@echo "Available targets:"
	@echo " readme - Display README information"
	@echo " run    - Run the translation and POS tagging program"

