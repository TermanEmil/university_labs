# Run make fclean everywhere it's possible
find . -name Makefile | sed 's/M.*$//' | xargs -L1 make fclean -sC

# Remove python residues.
find . -name *.pyc | xargs rm -f
find . -name __pycache__ | xargs rm -rf

# Remove latex residues.
find . \( -name "*.fls" -or -name "*.aux" -or -name "*.fdb_latexmk" -or -name \
	'*.log' -or -name "*.out" -or -name "*.synctex.gz" \) | xargs rm -rf