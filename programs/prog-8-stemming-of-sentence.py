from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
message = input("Enter message for stemming : ")
words = word_tokenize(message)

print("Root words are : ")
for word in words:
	print(f"{word} : {ps.stem(word)}")