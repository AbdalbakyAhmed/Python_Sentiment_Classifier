import sys

msecs = 200000
sys.setExecutionLimit(msecs)  #increase the run time 
#############################
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation (strWord):
    for x in punctuation_chars:
        strWord = strWord.replace(x, "")
    return strWord
#list of positive words:

pos_words = list()
with open ("positive_words.txt") as p_file:
    for line in p_file:
        if line[0] != ';' and line[0] != '\n':
            pos_words.append(line.strip())

#list of negative words:
neg_words = list()
with open ("negative_words.txt") as n_file:
	for line in n_file:
		if line != ':' and line[0] != '\n':
			neg_words.append(line.strip())

#get Positive words counts:
def get_pos (strSentence):
	strSentence = strip_punctuation(strSentence.lower()) #to ensure that all sntence is in lower case
	lst_strSentence = strSentence.split()

	count = 0
	for word in lst_strSentence:
		for pos in pos_words:
			if pos == word:
				count += 1
	return count

#get Negative words counts:
def get_neg (strSentence):
	strSentence = strip_punctuation(strSentence.lower()) #to ensure that all sntence is in lower case
	lst_strSentence = strSentence.split()

	count = 0
	for word in lst_strSentence:
		for neg in neg_words:
			if  neg == word:
				count += 1
	return count

def sentiment_classifier (result_file, data_file) :

	result_file = result_file +".csv"
	print(result_file)

	data_file = data_file +".csv"
	print(data_file)
    # Open file project_twitter_data for read
	project_twitter_data = open(data_file,'r')

	# Open file resulting_data to write the output
	resulting_data = open (result_file,'w')

	resulting_data.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
	resulting_data.write("\n")

	linesData = project_twitter_data.readlines()
	linesData.pop(0)
	for i in linesData:
		list_data = i.strip().split(',')
		resulting_data.write("{}, {}, {}, {}, {}".format(list_data[1], list_data[2], get_pos(list_data[0]), get_neg(list_data[0]), (get_pos(list_data[0]) - get_neg(list_data[0]) ) ) )
		resulting_data.write("\n")
		# print("{}, {}, {}, {}, {}".format(list_data[1], list_data[2], get_pos(list_data[0]), get_neg(list_data[0]), (get_pos(list_data[0]) - get_neg(list_data[0]) ) ) )
	#close files
	resulting_data.close()
	project_twitter_data.close()

############################################
sentiment_classifier('resulting_data', 'project_twitter_data')
print(strip_punctuation("today"))
print(get_pos("what a truly Wonderful day it is today! #incredible"))