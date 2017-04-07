class Markov:
	def __init__(self,occurrence,seq_len,order,wl_min,wl_max):
		self.occurrence = None
		self.seq_len = seq_len
		self.max_order = 0
		self.order = None
		self.wl_min = None
		self.wl_max = None

		if type(occurrence) is dict:
			self.occurrence = occurrence
		else:
			print 'input must be dictionary type, given', type(occurrence)

		self.compute_max_order()
		self.set_markov_order(order)
		self.set_word_length_range(wl_min, wl_max)
		
	def compute_max_order(self):
		for key in self.occurrence.keys():
			if self.max_order < len(key) - 1:
				self.max_order = len(key) - 1
		
	def set_markov_order(self, order):
		assert (order >= 0),'morkov order: '+str(order)+' < 0'
                assert (order <= self.max_order),'markov order: '+str(order)+'> max_order:'+str(self.max_order)
		self.order = order

	def set_word_length_range(self, l, r):
                assert (l<r),'min len: '+str(l)+' > max length: '+str(r)
                assert (l>self.order), 'min length: '+str(l)+' <= markov order:'+str(self.order)
		self.wl_min = l
		self.wl_max = r

	def get_expected_value(self, word):
		# print word
		# print word[:self.order]
                assert (len(word)>self.order),'word length: '+str(len(word))+' < order: '+str(self.order)
		ret = float(self.occurrence[word[:self.order]]) / (self.seq_len-self.order)
		for l in range(len(word)-self.order):
			r = l + self.order+1
			ret *= float(self.occurrence[word[l:r]]) / self.occurrence[word[l:r-1]]
			# print word[l:r]
		return (self.seq_len - len(word)) * ret
	
	def get_OE_score(self, word):
                assert (len(word)>self.order),'word length: '+str(len(word))+' < order: '+str(self.order)
		O = self.occurrence[word]
		E = get_expected_value(word)
		return float(O)/E
	
	def get_variance(self, word):
		pass

	def print_probability_table(self):
		for key in self.occurrence.keys():
			print key, '\t\t', self.occurrence[key]

if __name__ == '__main__':
        occ = dict()
        occ['A'] = 50
        occ['AA'] = 10
        occ['AB'] = 20
        occ['AC'] = 5
        occ['AD'] = 15
        occ['AAA'] = 2
        occ['AAB'] = 8
        occ['ABA'] = 10
        occ['ABB'] = 4
        occ['ABC'] = 6
        occ['ACC'] = 5

        seq_len = 3
        order = 1
        wl_min = order + 1
        wl_max = seq_len
        
        M = Markov(occ, seq_len, order, wl_min, wl_max)
        pass
