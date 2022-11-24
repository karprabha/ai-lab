from nltk.stem import WordNetLemmatizer
import string

lemmatizer = WordNetLemmatizer()

message = input("Enter a message : ")
punctuations = string.punctuation

for word in message:
	if word in punctuations:
		message.remove(word)

message = message.split()
print("word\t\tlemma")
for word in message:
	print(f"{word}\t\t{lemmatizer.lemmatize(word)}")
