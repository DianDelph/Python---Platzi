

# diciconario con las letras y su clave
KEYS = {
	'a': 'w',
	'b': 'E',
	'c': 'x',
	'd': '1',
 	'e': 'a',
	'f': 't',
	'g': '0',
	'h': 'C',
	'i': 'b',
	'j': '!',
	'k': 'z',
	'l': '8',
	'm': 'M',
	'n': 'I',
	'o': 'd',
	'p': '.',
	'q': 'U',
	'r': 'Y',
	's': 'i',
	't': '3',
	'u': ',',
	'v': 'J',
	'w': 'N',
	'x': 'f',
	'y': 'm',
	'z': 'W',
	'A': 'G',
	'B': 'S',
	'C': 'j',
	'D': 'n',
	'E': 's',
	'F': 'Q',
	'G': 'o',
	'H': 'e',
	'I': 'u',
	'J': 'g',
	'K': '2',
	'L': '9',
	'M': 'A',
	'N': '5',
	'O': '4',
	'P': '?',
	'Q': 'c',
	'R': 'r',
	'S': 'O',
	'T': 'P',
	'U': 'h',
	'V': '6',
	'W': 'q',
	'X': 'H',
	'Y': 'R',
	'Z': 'l',
	'0': 'k',
	'1': '7',
	'2': 'X',
	'3': 'L',
	'4': 'p',
	'5': 'v',
	'6': 'T',
	'7': 'V',
	'8': 'y',
	'9': 'K',
	'.': 'Z',
	',': 'D',
	'?': 'F',
	'!': 'B',
}


def encrypt(message):
	words = message.split(' ') # separa el string por palabra (cada que hay espacio) y lo guarda en una lista
	encrypted_message = []

	for word in words: # por cada palabra en la lista
		encrypted_word = ''
		for letter in word: #por cada letra de la palabra
			encrypted_word += KEYS[letter] # accesdo a la llave usando la letra y guardo el valor
		encrypted_message.append(encrypted_word)  # agrego la palabra al cifrado
	
	return ' '.join(encrypted_message) # reconstruyo el string y lo regreso


def decrypt(message):
	words = message.split(' ')
	decrypted_message = []

	for word in words:
		decrypted_word = ''

		for letter in word:
			for key, value in KEYS.items():  # no podemos saber que value corresponde a qué key, entonces se recorren ambos
				if value == letter:
					decrypted_word += key
					
		decrypted_message.append(decrypted_word)

	return ' '.join(decrypted_message)  # reconstruyo el string y lo regreso


def run():

	while True:

		command = input('''--- * --- * --- * --- * --- * --- * --- * ---

			Bienvenido a criptografía. ¿Qué deseas hacer?

			 [c]ifrar mensaje
			[d]ecifrar mensaje
			[s]alir
		''')

		if command == 'c':
			message = input('Escribe tu mensaje: ')
			encrypted_message = encrypt(message)
			print(encrypted_message)
		elif command == 'd':
			encrypted_message = input('Escribe tu mensaje cifrado: ')
			decrypted_message = decrypt(encrypted_message)
			print(decrypted_message)
		elif command == 's':
			print('salir')
		else:
			print('¡Comando no encontrado!')


if __name__ == '__main__':
	print('M E N S A J E S  C I F R A D O S')
	run()
