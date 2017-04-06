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
		
	# def __init__(self, occurrence):
	#	self.occurrence = None
	#	self.order = None
	#	self.wl_min = None
	#	self.wl_max = None
		
	#	if type(occurrence) is dict:
	#		self.occurrence = occurrence
	#	else:
	#		print 'input must be dictionary type, given', type(occurrence)
		
	#	self.max_order = 0
	#	self.compute_max_order()
		
	def compute_max_order(self):
		for key in self.occurrence.keys():
			if len(key) > self.max_order + 1:
				self.max_order = len(key) - 1
		
	def set_markov_order(self, order):
		if order < 0:
			print 'markov order < 0'
		if order > self.max_order:
			print 'markov order too large, max_order:', self.max_order 
		self.order = order

	def set_word_length_range(self, l, r):
		if l > r:
			print 'min length:',l,'> max length:', r
			return
		if l <= self.order:
			print 'min length:',l,'<= markov order:', self.order
			return
		self.wl_min = l
		self.wl_max = r

	def get_expected_value(self, word):
		# print word
		# print word[:self.order]
		ret = float(self.occurrence[word[:self.order]]) / (self.seq_len-self.order)
		for l in range(len(word)-self.order):
			r = l + self.order+1
			ret *= float(self.occurrence[word[l:r]]) / self.occurrence[word[l:r-1]]
			# print word[l:r]
		return (self.seq_len - len(word)) * ret
	
	def get_OE_score(self, word):
		O = self.occurrence[word]
		E = get_expected_value(word)
		return float(O)/E
	
	def get_variance(self, word):
		pass

	def print_probability_table(self):
		for key in self.occurrence.keys():
			print key, '\t\t', self.occurrence[key]
