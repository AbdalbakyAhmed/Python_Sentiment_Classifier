# Python_Sentiment_Classifier
Final Project of the course Python Functions, Files, and Dictionaries. 
This course is part of the "Python 3 Programming Specialization" by University of Michigan.
more information: https://www.coursera.org/learn/python-functions-files-dictionaries/

## Tasks:
1. Building a sentiment classifier, which will detect how positive or negative each tweet is. 
2. create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. 
3. produce a graph of the Net Score vs Number of Retweets.
--
## Function
#### 1. def strip_punctuation (word):
takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word.
#### 2. def get_pos (strSentence):
takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words, The function should return a positive integer how many occurrences there are of positive words in the text.
using a list of "positive_words" to determine what words will count as positive. 
#### 3. def get_neg (strSentence):
takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. 
The function should return a positive integer - how many occurrences there are of negative words in the text.
using a list of "negative_words" to determine what words will count as negative.
### 4. def sentiment_classifier (result_file, data_file) :
sentiment_classifier will detect how positive or negative each tweet is. 
Takes two string parameters, 
data_file which represents the name of CSV file which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet).
result_file which represents the name of CSV file which we will write the ouput which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. 
