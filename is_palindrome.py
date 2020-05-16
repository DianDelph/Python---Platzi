#busca si una palabra es palíndromo

# usando pre establecido de python
def palindrome2(word):
	reversed_word = word [::-1]

	if reversed_word == word:
		return True
	else:
		return False


# haciendo algoritmo propio
def palindrome(word):
	reversed_letters = [] #lista que me ayudará a comprobar si es palíndromo

	for letter in word:
		reversed_letters.insert(0, letter) #inserto la letra en el índice 0

		reversed_word = ''.join(reversed_letters) #genero string vacía y le agrego la letra según el índice de reversed_letters
		print(reversed_word)

	if reversed_word == word:
		return True

	return False

if __name__ == "__main__":
	word = str(input('Escribe una palabra '))

	result = palindrome(word)

	if result is True:
		print('{} sí es un palíndromo'.format(word))
	else:
		print('{} no es un palíndromo'.format(word))