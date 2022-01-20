TOOLS = ../tools
SRC = .
PYTHON  = python3

.DEFAULT_GOAL := build

.PHONY: dict
Dictionary.jack:
	$(PYTHON) gendict.py > Dictionary.jack

.PHONY: build
build: Dictionary.jack
	$(TOOLS)/JackCompiler.sh .

.PHONY: run
run: 
	$(TOOLS)/VMEmulator.sh

.PHONY: clean
clean:
	rm -rf *.vm Dictionary.jack
