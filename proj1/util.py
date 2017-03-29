import csv
import re

def load_probability_table(file_path):
	P = dict()
	total_char_count = 0
	with open(file_path, 'r') as file:
		_ = file.readline()
		for line in file:
			tokens = re.split('[\t| ]+', line)
			P[tokens[0]] = float(tokens[1])
			total_char_count += float(tokens[1])
		for key in P.keys():
			P[key] /= total_char_count
	return total_char_count, P

def test_probability_table(table):
	for k, v in table.items():
		print k, '\t', v
	sum = 0
	for v in table.values():
		sum += v
	print 'sum of p: ', sum

