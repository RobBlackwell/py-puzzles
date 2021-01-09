.PHONY: shell
shell :
	nix-shell

.PHONY: format
format:
	black *.py

.PHONY: test
test:
	./maths-romance.py
	./luminescent-being.py
	./mission.py
	./exclusionary-squares.py
