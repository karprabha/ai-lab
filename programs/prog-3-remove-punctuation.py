import string

message  = input("Enter a message : ")
print(f"Original message : {message}")

punctuation = string.punctuation

for word in message:
    if word in punctuation:
        message = message.replace(word,"")
print(f"Message after punctuation removal : {message}")