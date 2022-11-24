from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag

stop_words = set(stopwords.words("English"))
message = input("Enter message : ")
tokens = sent_tokenize(message)

print("POS tags for each word are : ")
for token in tokens:
	word = word_tokenize(token)
	word = [w for w in word if not w in stop_words]
	tag = pos_tag(word)
	print(tag)