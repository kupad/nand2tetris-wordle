.PHONY: dictionary run kill clean
TOOLS = ../tools
PYTHON  = python3
DICT = '/usr/share/dict/american-english'
#DICT = '/usr/share/dict/spanish'


.DEFAULT_GOAL := build

build: Dictionary.jack
	$(TOOLS)/JackCompiler.sh .

Dictionary.jack: gendict.py
	$(PYTHON) gendict.py $(DICT)

dictionary: Dictionary.jack

run: build
	$(TOOLS)/VMEmulator.sh

kill:
	pkill -f 'java.*VMEmulatorMain'

clean:
	rm -rf *.vm Dictionary.jack
