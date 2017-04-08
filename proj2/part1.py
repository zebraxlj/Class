import csv
import re
from util import *
from Markov import Markov

import sys

P = dict()
trans_matrix = []
degree = 1
row = dict()
col = dict()
# (word, O/E score, O, E) 
word_tuples = []
word_tuples_by_length = []
total_char_count = 0
total_word_count = 0

def save_part1():
	header = ['word', 'O/E', 'obs', 'E']
	# with open('output/part1_letter_probability.csv', 'wb') as f:
	#	writer = csv.writer(f)
	#	writer.writerow(['letter', 'P'])
	#	keys = P.keys()
	#	keys = sorted(keys)
	#	for key in keys:
	#		writer.writerow([key, P[key]])
	with open('output/part1_M'+str(order)+'_result_full.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerows(word_tuples)
	with open('output/part1_M'+str(order)+'_result_top_bott_50OE.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(['top 50'])
		writer.writerow(header)
		writer.writerows(word_tuples[1:51])
		writer.writerow(['bottom 50'])
		writer.writerow(header)
		writer.writerows(word_tuples[-51:-1])
	with open('output/part1_M'+str(order)+'_result_top_bott_50OE_by_length.csv', 'wb') as f:
		writer = csv.writer(f)
		for tuples in word_tuples_by_length:
			if not tuples: continue
			temp = sorted(tuples, key = lambda score: score[1], reverse = True)
			writer.writerow(['word length ' + str(len(tuples[0][0]))])
			writer.writerow(['top 50 O/E'])
			writer.writerow(header)
			writer.writerows(tuples[1:51])
			writer.writerow(['bottom 50 O/E'])
			writer.writerow(header)
			writer.writerows(tuples[-51:-1])
			writer.writerow([])
	with open('output/part1_M'+str(order)+'_result_top_bott_50O_by_length.csv', 'wb') as f:
		writer = csv.writer(f)
		for tuples in word_tuples_by_length:
			if not tuples: continue
			temp = sorted(tuples, key = lambda obs : obs[2], reverse = True)
			writer.writerow(['word length ' + str(len(temp[0][0]))])
			writer.writerow(['top 50 Observation'])
			writer.writerow(header)
			writer.writerows(temp[:51])
			writer.writerow(['bottom 50 Observation'])
			writer.writerow(header)
			writer.writerows(temp[-51:])
			writer.writerow([])

order = 4

word_len_min = order+1
word_len_max = 8

books = ['alice_in_wonderland_nows', 'big_dummys_guide_to_internet_nows', 'california_mexican_spanish_cook_book_nows', 'complete_book_of_cheese_nows', 'einstein_relativity_nows', 'hamlet_prince_of_denmark_nows', 'complete_book_of_cheese_nows', 'wood_carving_nows']

import math

if __name__ == '__main__':
	file_pathes = []
#	for book_name in books:
#	     file_pathes.append('letter_occurrence/'+book_name)
	total_char_count = get_total_char_count(file_pathes)

	file_pathes = []
	for book_name in books:
	     file_pathes.append('word_occurrence/'+book_name)
	occurrence = load_occurrence_file(file_pathes)

	word_dict = dict()
	for order in xrange(1, 6):
		print 'order',order

		word_len_min = order + 1
		word_len_max = 8
		markov_model = Markov(occurrence, total_char_count, order, word_len_min, word_len_max)

		word_tuples = []
		word_tuples_by_length = []
		for word in occurrence:
			if len(word) < word_len_min or \
			   len(word) > word_len_max:
				continue
			O = occurrence[word]
			E = markov_model.get_expected_value(word)
			word_tuples.append((word, float(math.pow(O,2))/(math.sqrt(float(E)/2+2)-1), int(O), E))
#			 word_tuples.append((word, float(O)/E, int(O), E))


		
		for i in xrange(word_len_max+1):
			word_tuples_by_length.append([])
		for elem in word_tuples:
			#word_tuples_by_length[len(elem[0]) - len(word_tuples[0][0]) + 1].append(elem)
			word_tuples_by_length[len(elem[0])].append(elem)
		for i in xrange(len(word_tuples_by_length)):
			word_tuples_by_length[i] = sorted(word_tuples_by_length[i], \
							  key = lambda word : word[1], reverse = True)

		word_tuples = sorted(word_tuples, key = lambda word:word[1], reverse = True)
		save_part1()
		
				
	sys.exit(0)
	
	''' load all file instead of each book at once '''
	file_name = 'all'
	#file_name = 'complete_book_of_cheese_nows'
	occurrence = load_occurrence_file('word_occurrence/'+file_name)
	total_char_count = get_total_char_count('letter_occurrence/'+file_name)

	# for key in occurrence.keys():
	#	print key, '\t\t', occurrence[key]
	for order in xrange(1,6):
		print order
		word_len_min = order + 1
		
		M1 = Markov(occurrence, total_char_count, order, word_len_min, word_len_max)

		with open('word_occurrence/'+file_name, 'r') as file:
			_ = file.readline()
			for line in file:
				tokens = re.split('[\t| ]+', line)
				if len(tokens[0]) < word_len_min: continue
				if len(tokens[0]) > word_len_max: continue
				O = tokens[1]
				E = M1.get_expected_value(tokens[0])
				word_tuples.append((tokens[0], float(O)/E, int(O), E))

		for i in xrange(word_len_max+1):
			word_tuples_by_length.append([])
		for elem in word_tuples:
			word_tuples_by_length[len(elem[0]) - len(word_tuples[0][0]) + 1].append(elem)
		for i in xrange(len(word_tuples_by_length)):
			word_tuples_by_length[i] = sorted(word_tuples_by_length[i], \
							  key = lambda word : word[1], reverse = True)
		word_tuples = sorted(word_tuples, key = lambda word:word[1], reverse = True)
		save_part1()
		
