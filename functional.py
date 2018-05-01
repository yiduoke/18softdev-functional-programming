import re

fd = open("grimm", "r") #opens the grimm story file
all = fd.read().lower() #converts every word into lowercase only
all = re.sub(r'[^\w\s]','',all) #gets rid of punctuation

word_list =  all.split()
#dictionary of words and their frequencies
freqs = {x: word_list.count(x) for x in set(word_list)}
print freqs #{'has': 201, 'all': 980}

#frequency of a single word
def single_freq(word):
	if word in freqs:
		return freqs[word]
	else:
		return 0

print 'frequency of the word "prominently": ' + str(single_freq('prominently'))

#frequency of multiple words
def group_frequency(listy):
	return reduce(lambda a, b: single_freq(a)+single_freq(b), listy)

print 'frequency of "persuaded" and "will": ' + str(group_frequency(['persuaded', 'will']))

#most frequently-occuring word
def most_freq():
	return reduce(lambda a, b: a if freqs[a]>freqs[b] else b, freqs)

print "most frequent word: " + str(most_freq())