ANTLR=../antlr/antlr-3.1.3.jar

all: antlr

antlr: grammar/SelectExpr.g grammar/SelectScript.g
	cd grammar; java -jar $(ANTLR) SelectExpr.g
	cd grammar; java -jar $(ANTLR) SelectScript.g
	mv grammar/*.py SelectScript/
	mv grammar/*.tokens SelectScript/

clean:
	cd SelectScript; rm SelectExprLexer.py  SelectExprParser.py  SelectExpr.tokens SelectScript.tokens SelectScript.py
	
install:
	python setup.py install
	python setup.py install
