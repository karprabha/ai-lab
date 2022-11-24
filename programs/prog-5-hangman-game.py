import time

name = input("Enter you name : ")
print(f"Hello {name}, Let's play Hangman")

time.sleep(1)
print("Start guessing word")
time.sleep(0.5)

word = ("Seceret")
word = word.lower()

guesses = ""
turns = 12

while turns > 0 :
	failed = 0
	print("\nWord : ",end="")
	for char in word:
		if char in guesses:
			print(char,end="")
		else:
			print("_",end="")
			failed += 1
	if failed == 0:
		print(f"\nYou Won!!, word was {word}")
		break
	guess = input("\nGuess a character : ")
	guesses += guess

	if guess not in word:
		turns -= 1
		print("Wrong guess !!")
		print(f"{turns} guesses remaining")

	if turns == 0:
		print(f"You lose!!, word was {word}")