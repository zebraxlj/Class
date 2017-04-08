IMPORTANT:
	run Makefile before run part1 part2 code
	If Make file cannot run correctly because of counting.c or counting_prime.c,
	manually compile the right one, then run the following makefile option:
		> make clean
		> g++ <correct counting C file>
		> make word_occurrence
		> make letter_occurrence
		> mkdir output
	
	python version: 2.7


./books ----------------- all book files, pre- and postfix removed
./e_coli ---------------- E-coli genome sequence file

./letter_occurrence ----- count of letter occurrence in different books
------------------------- output from running counting's a.out -min 1 -max 1 [books]

./output ---------------- output files of part1 and part2 models
------------------------- explained in the report

./word_occurrence ------- count of the word occurrence in different books
------------------------- output from running counting's ./a.out -min 3 -max 10 [books]

./counting.c
./counting_prime.c ------ counting program provided by Dr. Drews
------------------------- both are modified to ignore numerical characters

./Markov.py ------------- Markov model class

./part1.py
./part2.py -------------- part 1 and part 2 implementation

./util.py --------------- utility functions that are used in both part 1 and part 2