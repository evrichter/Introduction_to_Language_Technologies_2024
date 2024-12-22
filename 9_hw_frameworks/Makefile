data_dir = data
models_dir = models

conllu_train = $(data_dir)/train.conllu
conllu_dev = $(data_dir)/dev.conllu
conllu_test = $(data_dir)/test.conllu

spacy_train = $(data_dir)/train.spacy
spacy_dev = $(data_dir)/dev.spacy
spacy_test = $(data_dir)/test.spacy

# truncated files
#conllu_train_head = $(data_dir)/train_head.conllu
#conllu_dev_head = $(data_dir)/dev_head.conllu

base_config = base_config.cfg
full_config = config.cfg

model_best = $(models_dir)/model-best

.PHONY: readme download train eval show

readme:
	@echo "I used SpaCy to train a POS tagger for the German language. The training data comes from a Universal Dependencies treebank. The model achieved 95.47% accuracy on the test set. Since training takes a considerable amount of time, I modified the config file to set the number of epochs to 1, which was sufficient to achieve 95% accuracy. With longer training, this accuracy could likely improve further. Additionally, I used the head command to truncate the training data (see the commented code in the Makefile) in an attempt to speed up the training process. However, for some reason, this did not result in a faster training time."

readme_order:
	@echo "1. Download the data"
	@echo "2. Download the German SpaCy model"
	@echo "3. Convert the data to SpaCy format"
	@echo "4. Create a full config file (from the base config file)"
	@echo "5. Train the model (change e.g. number of epochs in the config file to reduce training duration)"
	@echo "6. Evaluate the model on the test set"
	@echo "7. Show the model on three example sentences"


download:
	mkdir -p $(data_dir)
	wget -O $(conllu_train) https://raw.githubusercontent.com/UniversalDependencies/UD_German-HDT/refs/heads/master/de_hdt-ud-train-a-1.conllu
	wget -O $(conllu_dev) https://raw.githubusercontent.com/UniversalDependencies/UD_German-HDT/refs/heads/master/de_hdt-ud-dev.conllu
	wget -O $(conllu_test) https://raw.githubusercontent.com/UniversalDependencies/UD_German-HDT/refs/heads/master/de_hdt-ud-test.conllu


download_model:
	python3 -m spacy download de_core_news_lg


#truncate_train_dev_set:
#	head -n 20037 $(conllu_train) > $(conllu_train_head)
#	head -n 2526 $(conllu_dev) > $(conllu_dev_head)

#convert: truncate_train_dev_set
#	python3 -m spacy convert $(conllu_train_head) $(data_dir) --n-sents 10
#	python3 -m spacy convert $(conllu_dev_head) $(data_dir) --n-sents 10
#	python3 -m spacy convert $(conllu_test) $(data_dir) --n-sents 10


convert: 
	python3 -m spacy convert $(conllu_train) $(data_dir) --n-sents 10
	python3 -m spacy convert $(conllu_dev) $(data_dir) --n-sents 10
	python3 -m spacy convert $(conllu_test) $(data_dir) --n-sents 10
	
	

create_full_config: $(base_config)
	python3 -m spacy init fill-config $(base_config) $(full_config)
	

train:
	mkdir -p $(models_dir)
	python3 -m spacy train $(full_config) \
		--output $(models_dir) \
		--paths.train $(spacy_train) \
		--paths.dev $(spacy_dev)
		

eval: $(model_best) $(spacy_test)
	python3 -m spacy evaluate $(model_best) $(spacy_test)


show:
	python3 show_model.py
