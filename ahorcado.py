
import random


# los "gráficos" del juego. Una lista "constante" con arte ASCII
IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

# constante con las palabras que usaremos en el juego


WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

def display_board(hidden_word, tries):
	print(IMAGES[tries]) #imprime la imagen según el número de erroes
	print(' ')
	print(hidden_word)
	print('-----------------')

def random_word():
	index = random.randint(0, len(WORDS)- 1) # elige una palabra de mi lista
	return WORDS[index]

def run():
	word = random_word ()
	# genera un tablero, su largo es el mismo que la palabra escondida
	hidden_word = ['_'] * len(word)
	# genera un tablero, su largo es el mismo que la palabra escondida
	hidden_word = ['_'] * len(word)
	tries = 0 #guarda el número de errores

	while True:  #loop infinito
		display_board(hidden_word, tries) # va a manejar la interfaz
		current_letter = input('Escoge una letra: ')

		letter_indexes = [] 
		for index in range(len(word)): # veremos si la letra ingresada corresponde
			if word[index] == current_letter:
				letter_indexes.append(index) # si la letra corresponde, la inserta donde le toca

		if len(letter_indexes) == 0 :# si la lista está vacía, el usuario no le atinó
			tries += 1

			if tries == 7:
				display_board(hidden_word, tries)
				print('')
				print(' ¡Perdiste! La palabra correcta era {}'.format(word))
				break
		else:
			for index in letter_indexes:
				hidden_word[index] = current_letter #se muestran las letras que ya llevo
				
			letter_indexes = [] # comienzo de nuevo
		try:
			hidden_word.index('_')  #busca si quedan letras por adivinar
		except ValueError:
			print(' ')
			print('¡Felicidades! Ganaste. La palabra es {}'.format(word))
			break
				

if __name__ == "__main__":
	print (' B I E N V E N I D O S   A  A H O R C A D O')
	run()
