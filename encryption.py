alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newmessage = ''

message = input('Please enter a message: ')

for character in message:
	if character in alphabet:
		position = alphabet.find(character)
		newposition = (position + key) %26
		newcharacter = alphabet[newposition]
		newmessage += newcharacter
	else:
		newmessage += character

print('Your encrypted message is:',newmessage)
