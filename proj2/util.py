import csv
import re

def load_occurrence_file(file_path, num_word=True, num_file=False):
	occurrence = dict()
	with open(file_path, 'r') as file:
		_ = file.readline()
		for line in file:
			tokens = re.split('[\t|\n| ]+', line)
			if num_word:
				occurrence[tokens[0]] = float(tokens[1])
			elif num_file:
				occurrence[tokens[0]] = float(tokens[2])
	return occurrence

def get_total_char_count(char_occurrence_file):
        total_char_count = 0
	with open(char_occurrence_file, 'r') as file:
		_ = file.readline()
		for line in file:
			tokens = re.split('[\t|\n| ]+', line)
			total_char_count += float(tokens[1])
	return total_char_count

def test_probability_table(table):
	for k, v in table.items():
		print k, '\t', v
	sum = 0
	for v in table.values():
		sum += v
	print 'sum of p: ', sum

