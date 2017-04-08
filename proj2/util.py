import csv
import re

''' able to load multiple file and merge the occurrence table '''
def load_occurrence_file(file_pathes, num_word=True, num_file=False):
	assert isinstance(file_pathes, (list, tuple)), 'file_pathes must be a list or tuple'
	occurrence = dict()
	for file_path in file_pathes:
		with open(file_path, 'r') as file:
			_ = file.readline()
			for line in file:
				tokens = re.split('[\t|\n| ]+', line)
				if num_word:
					if tokens[0] in occurrence:
						#print tokens[0], occurrence[tokens[0]], occurrence[tokens[0]]+float(tokens[1])
						occurrence[tokens[0]] += float(tokens[1])
					else:
						occurrence[tokens[0]] = float(tokens[1])
				elif num_file:
					if tokens[0] in occurrence:
						#print tokens[0], occurrence[tokens[0]], occurrence[tokens[0]]+float(tokens[1])
						occurrence[tokens[0]] += float(tokens[2])
					else:
						occurrence[tokens[0]] = float(tokens[2])
	return occurrence

def get_total_char_count(char_occurrence_files):
	total_char_count = 0
	for char_occurrence_file in char_occurrence_files:
                print char_occurrence_file
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


if __name__ == '__main__':
	single = 'word_occurrence/einstein_relativity_nows'
	multiple = ['word_occurrence/einstein_relativity_nows', 'word_occurrence/california_mexican_spanish_cook_book_nows']
	print single
	#temp1 = load_occurrence_file([single])
	temp2 = load_occurrence_file(multiple)
	pass
