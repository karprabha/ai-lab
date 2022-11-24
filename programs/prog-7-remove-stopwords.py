from nltk.corpus import stopwords

f1 = open("input.txt","r")
f2 = open("Output.txt","w")

stop_words = stopwords.words("English")

for line in f1:
	words = line.split()
	for word in words:
		if word not in stop_words:
			f2.write(word)
			f2.write(" ")

f1.close()
f2.close()