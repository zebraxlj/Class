./books ----------------- all book files, pre- and postfix removed


./letter_occurrence ----- count of letter occurrence in different books
------------------------- output from running counting's a.out -min 1 -max 1 [books]
------------------------- Note: run the following commands before run part1.py and part2.py
./a.out -min 1 -max 1 ./books/* > ./letter_occurrence/all
./a.out -min 1 -max 1 ./books/alice_in_wonderland_nows > ./letter_occurrence/alice_in_wonderland_nows
./a.out -min 1 -max 1 ./books/einstein_relativity_nows > ./letter_occurrence/einstein_relativity_nows
./a.out -min 1 -max 1 ./books/big_dummys_guide_to_internet_nows > ./letter_occurrence/big_dummys_guide_to_internet_nows
./a.out -min 1 -max 1 ./books/hamlet_prince_of_denmark_nows > ./letter_occurrence/hamlet_prince_of_denmark_nows
./a.out -min 1 -max 1 ./books/california_mexican_spanish_cook_book_nows > ./letter_occurrence/california_mexican_spanish_cook_book_nows
./a.out -min 1 -max 1 ./books/hound_of_baskervilles_nows > ./letter_occurrence/hound_of_baskervilles_nows
./a.out -min 1 -max 1 ./books/complete_book_of_cheese_nows > ./letter_occurrence/complete_book_of_cheese_nows
./a.out -min 1 -max 1 ./books/wood_carving_nows > ./letter_occurrence/wood_carving_nows


./output ---------------- output files of part1 and part2 models
------------------------- explained in the report


./word_occurrence ------- count of the word occurrence in different books
------------------------- output from running counting's ./a.out -min 3 -max 10 [books]
------------------------- Note: run the following commands before run part1.py and part2.py
./a.out -min 3 -max 10 ./books/* > ./word_occurrence/all
./a.out -min 3 -max 10 ./books/alice_in_wonderland_nows > ./word_occurrence/alice_in_wonderland_nows
./a.out -min 3 -max 10 ./books/einstein_relativity_nows > ./word_occurrence/einstein_relativity_nows
./a.out -min 3 -max 10 ./books/big_dummys_guide_to_internet_nows > ./word_occurrence/big_dummys_guide_to_internet_nows
./a.out -min 3 -max 10 ./books/hamlet_prince_of_denmark_nows > ./word_occurrence/hamlet_prince_of_denmark_nows
./a.out -min 3 -max 10 ./books/california_mexican_spanish_cook_book_nows > ./word_occurrence/california_mexican_spanish_cook_book_nows
./a.out -min 3 -max 10 ./books/hound_of_baskervilles_nows > ./word_occurrence/hound_of_baskervilles_nows
./a.out -min 3 -max 10 ./books/complete_book_of_cheese_nows > ./word_occurrence/complete_book_of_cheese_nows
./a.out -min 3 -max 10 ./books/wood_carving_nows > ./word_occurrence/wood_carving_nows


./counting.c
./counting_prime.c ------ counting program provided by Dr. Drews
------------------------- both are modified to not count numerical characters


./part1.py
./part2.py -------------- part 1 and part 2 implementation


./util.py --------------- utility functions that are used in both part 1 and part 2