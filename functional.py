word_list = ['test', 'grimm', 'meow', 'grimm']
freqs = {x: word_list.count(x) for x in set(word_list)}
print freqs

# print(reduce(lambda a, b: a+b if b=='grimm' else b, word_list))

# print(freq_single('test'))

# def freq_group(words):
# 	a = 0
	
# def most_freq():
# 	a = ''
# 	reduce(lambda word_freqs: word_freqs
