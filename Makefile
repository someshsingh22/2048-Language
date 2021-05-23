errfile:
	pip install sly==0.4
	python3 test.py 2>error.txt

console:
	pip install sly==0.4
	python3 test.py

clean:
	bash clean.sh 1> /dev/null 2> /dev/null