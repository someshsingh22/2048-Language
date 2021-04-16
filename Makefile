errfile:
	pip install sly==0.4
	python3 test.py 2>error.txt

console:
	pip install sly==0.4
	python3 test.py

clean:
	rm error.txt 
	rm -r ./__pycache__