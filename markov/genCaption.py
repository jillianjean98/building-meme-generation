# from nltk.tokenize import RegexpTokenizer
import nltk
import re
import pprint
import random
import sys
import getopt
import glob
import markov_meme

def checkargs():
	keyLen = 1
	maxWordInSentence = 100
	genNSentences = 5
	fileList = []

	if len(sys.argv) < 1:
		print( "Usage: " + sys.argv[0] + " -n <sentences to generate> ")
		exit(0)
	else:
		arg = {}
		options = getopt.getopt(sys.argv[1:], 'n:')
		for item in options[0]:
			if(item):
				arg[ item[0] ] = item[1]
		# pprint.pprint(arg)

		genNSentences = int(arg[ '-n' ])
		dictFile = "dicts/meme_markov_dict.txt"

	return( maxWordInSentence, genNSentences, dictFile)


def main(maxWordInSentence, dictFile, genNSentences=50):

	#Create new Markov class
	markovObj = markov_meme.Markov(dictFile=dictFile, maxWordInSentence= maxWordInSentence)

	titles = []
	for _ in range( genNSentences ):
		tries = 0
		text = markovObj.genText()
		## try 10 times to generate unique result
		while filterResults(text) == "" and tries < 10:
			tries += 1
			text = markovObj.genText()
		titles.append(text)

	result = []
	for text in titles:
		match = filterResults(text)
		if(not match == ""):
			print(match)

def filterResults(result):
	file = open('data/meme_labels_clean.txt', 'r')
	filelist = file.readlines()
	file.close()
	found = False
	for line in filelist:
		if str(result) in line.lower():
			found = True
			return ""
	return result

if __name__ == "__main__":
	(maxWordInSentence, genNSentences, dictFile) = checkargs()

	main(maxWordInSentence, dictFile, genNSentences)
