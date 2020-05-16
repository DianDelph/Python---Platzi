
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
	hidden_word = ['_'] * len(word) # genera un tablero, su largo es el mismo que la palabra escondida
	tries = 0 #guarda el número de errores

	while True:  #loop infinito
		display_board(hidden_word, tries) # va a manejar la interfaz
		current_letter = str(input('Escoge una letra: '))

if __name__ == "__main__":
	print (' B I E N V E N I D O S   A  A H O R C A D O')
	run()