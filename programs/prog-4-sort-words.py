message = input("Enter message : ")
words = message.split()
words.sort()

sortedMessage = ""
for w in words:
	sortedMessage = sortedMessage + w + " "

print(f"Sorted message : {sortedMessage}")