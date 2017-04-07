len_min = 1
len_max = 10
all: a.out word_occurrence letter_occurrence
	if [ ! -d "./output" ]; then mkdir output; fi

word_occurrence:
	if [ ! -d "./word_occurrence" ]; then mkdir word_occurrence; fi
	./a.out -min $(len_min) -max $(len_max) -asclength ./books/* > ./word_occurrence/all
	./a.out -min $(len_min) -max $(len_max) -asclength ./books/alice_in_wonderland_nows > ./word_occurrence/alice_in_wonderland_nows
	./a.out -min $(len_min) -max $(len_max) -asclength ./books/einstein_relativity_nows > ./word_occurrence/einstein_relativity_nows
	./a.out -min $(len_min) -max $(len_max) -asclength ./books/big_dummys_guide_to_internet_nows > ./word_occurrence/big_dummys_guide_to_internet_nows
	./a.out -min $(len_min) -max $(len_max) -asclength ./books/hamlet_prince_of_denmark_nows > ./word_occurrence/hamlet_prince_of_denmark_nows
	./a.out -min $(len_min) -max $(len_max) -asclength ./books/california_mexican_spanish_cook_book_nows > ./word_occurrence/california_mexican_spanish_cook_book_nows
	./a.out -min $(len_min) -max $(len_max) -asclength ./books/hound_of_baskervilles_nows > ./word_occurrence/hound_of_baskervilles_nows
	./a.out -min $(len_min) -max $(len_max) -asclength ./books/complete_book_of_cheese_nows > ./word_occurrence/complete_book_of_cheese_nows
	./a.out -min $(len_min) -max $(len_max) -asclength ./books/wood_carving_nows > ./word_occurrence/wood_carving_nows

letter_occurrence:
	if [ ! -d "./letter_occurrence" ]; then mkdir letter_occurrence; fi
	./a.out -min 1 -max 1 ./books/* > ./letter_occurrence/all
	./a.out -min 1 -max 1 ./books/alice_in_wonderland_nows > ./letter_occurrence/alice_in_wonderland_nows
	./a.out -min 1 -max 1 ./books/einstein_relativity_nows > ./letter_occurrence/einstein_relativity_nows
	./a.out -min 1 -max 1 ./books/big_dummys_guide_to_internet_nows > ./letter_occurrence/big_dummys_guide_to_internet_nows
	./a.out -min 1 -max 1 ./books/hamlet_prince_of_denmark_nows > ./letter_occurrence/hamlet_prince_of_denmark_nows
	./a.out -min 1 -max 1 ./books/california_mexican_spanish_cook_book_nows > ./letter_occurrence/california_mexican_spanish_cook_book_nows
	./a.out -min 1 -max 1 ./books/hound_of_baskervilles_nows > ./letter_occurrence/hound_of_baskervilles_nows
	./a.out -min 1 -max 1 ./books/complete_book_of_cheese_nows > ./letter_occurrence/complete_book_of_cheese_nows
	./a.out -min 1 -max 1 ./books/wood_carving_nows > ./letter_occurrence/wood_carving_nows

a.out: counting_prime.c counting.c
	-gcc counting.c
	-gcc counting_prime.c


clean:
	rm -f ./a.out
	rm -rf word_occurrence
	rm -rf letter_occurrence
	rm -rf output
