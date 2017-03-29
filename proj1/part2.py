import csv
import numpy as np
import re
from util import *

# observation: number of books that contain W (word)
# expectation: 

# Define:
#         l = len(seq_i)
#         k = len(W)
#         y_i ------------- # of occurrence of W in seq_i
#         z_i ------------- if seq_i contains W
#         Z = sum(z_i) ---- number of books that contain W
# Then:
#         p(z_i) = p(y_i >= 0) = 1 - p(y_i == 0) = 1 - (1 - p(W))^(l-k+1)
#         E(Z) = E[sum(z_i)] = sum[E(z_i)] = sum[p(z_i)]
#         p(W) = product(p(w_i))

P = dict()
# (word, O/E score, O, E) 
word_tuples = []
word_tuples_by_length = []
total_char_count = 0
total_word_count = 0

books = ['alice_in_wonderland_nows', 'big_dummys_guide_to_internet_nows',\
		'california_mexican_spanish_cook_book_nows', 'complete_book_of_cheese_nows',\
		'einstein_relativity_nows', 'hamlet_prince_of_denmark_nows',\
		'complete_book_of_cheese_nows', 'wood_carving_nows']
		
l = []
for book in books:
	with open('books/' + book) as file:
		content = file.read()
		l.append(len(content))
print l

# E = num_books * (1)
def get_expected(word):
	p_W = np.float64(1)
	for letter in word:
		p_W *= P[letter]

	E_Z = 0
	for i in xrange(len(books)):
		p_z = 1 - (1 - p_W) ** (l[i] - len(word) + 1)
		E_Z += p_z
	
	return E_Z

def save_part2():
	header = ['word', 'O/E', 'obs', 'E']
	with open('output/part2_result_full.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerows(word_tuples)
	with open('output/part2_result_top_bott_50OE.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(['top 50'])
		writer.writerow(header)
		writer.writerows(word_tuples[1:51])
		writer.writerow(['bottom 50'])
		writer.writerow(header)
		writer.writerows(word_tuples[-51:-1])
	with open('output/part2_result_top_bott_50OE_by_length.csv', 'wb') as f:
		writer = csv.writer(f)
		for tuples in word_tuples_by_length:
			if not tuples: continue
			writer.writerow(['word length ' + str(len(tuples[0][0]))])
			writer.writerow(['top 50 O/E'])
			writer.writerow(header)
			writer.writerows(tuples[1:51])
			writer.writerow(['bottom 50 O/E'])
			writer.writerow(header)
			writer.writerows(tuples[-51:-1])
			writer.writerow([])
	with open('output/part2_result_top_bott_50O_by_length.csv', 'wb') as f:
		writer = csv.writer(f)
		for tuples in word_tuples_by_length:
			if not tuples: continue
			temp = sorted(tuples, key = lambda obs : obs[2], reverse = True)
			writer.writerow(['word length ' + str(len(temp[0][0]))])
			writer.writerow(['top 50 Observation'])
			writer.writerow(header)
			writer.writerows(temp[1:51])
			writer.writerow(['bottom 50 Observation'])
			writer.writerow(header)
			writer.writerows(temp[-51:-1])
			writer.writerow([])



if __name__ == '__main__':
	total_char_count, P = load_probability_table('letter_occurrence/all')
	#test_probability_table(P)

	with open('word_occurrence/all', 'r') as file:
		_ = file.readline()
		for line in file:
			tokens = re.split('[\t| ]+', line)
			O = int(tokens[2])
			E = get_expected(tokens[0])
			if E == 0:
				word_tuples.append((tokens[0], float('inf'), O, E))
			else:
				word_tuples.append((tokens[0], O/E, O, E))

	for i in xrange(11):
		word_tuples_by_length.append([])
	for elem in word_tuples:
		word_tuples_by_length[len(elem[0]) - len(word_tuples[0][0]) + 1].append(elem)

	for i in xrange(len(word_tuples_by_length)):
		word_tuples_by_length[i] = sorted(word_tuples_by_length[i], \
										key = lambda word : word[1], reverse = True)

	word_tuples = sorted(word_tuples, key = lambda word : word[1], reverse = True)

	save_part2()
