.PHONY: all pdf check test

all: pdf

# Rebuild committed PDFs and their source/hash manifest.
pdf:
	python3 scripts/build.py

# Validate links, hashes, LaTeX logs, and committed-vs-rebuilt PDF text.
check:
	python3 scripts/build.py --check

test:
	python3 -m unittest discover -s tests -v
