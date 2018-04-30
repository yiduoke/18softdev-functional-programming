word_list = ['test', 'grimm', 'word', 'grimm']

def freq_single(word):
	a=0
	reduce(lambda a, b: a +=1 if b==word, word_list)
	return a

def freq_group(words):
	a = 0
	
def most_freq():
	a = ''
	reduce(lambda word_freqs: word_freqs
