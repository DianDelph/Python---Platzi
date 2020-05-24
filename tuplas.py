
def first_not_repeating_char(char_sequence):
	seen_letters = {} # declaro un diccionario

	for idx, letter in enumerate(char_sequence): # recorro la secuencia de caracteres
		if letter not in seen_letters: # pregunto si el caracter no se encuentra en las letas ya vistas
			seen_letters[letter] = (idx, 1) #  guardo la letra (key) en el diccionario, y creo una tupla con el índice (value) y cuántas veces hemos visto la letra (1)
		else: # si ya la vimos 
			seen_letters[letter] = ( seen_letters[letter][0],seen_letters[letter][1] + 1) # si ya la vimos, entonces cambio la tupla que corresponde a la letra. Accedo al primer índice de la tupla (0), luego al segundo valor (1) y le incremento su valor en uno 
	
	final_letters = []
	for key, value in seen_letters.items(): # voy a limpiar el diccionario y me voy a quedar con las letras que sólo vimos una vez
		if value[1] == 1: # En el segundo valor (1) de la tupla dentro del diccionario es donde tengo almacenado cuántas veces vi la letra
			final_letters.append( (key, value[0])) # creo una nueva tupla donde mando la letra y índice donde se encuentra la letra.

	not_repeated_letters = sorted(final_letters, key=lambda value: value[1] ) # ordena la lista conforme al índice y regresa el primer elemento

	if not_repeated_letters: #si hay leatras reptidas
		return not_repeated_letters[0][0] #accedo a la primera tupla y al primer elemento de la tupla.
	else:
		return '_'




if __name__ == "__main__":
	char_sequence = input ('Escribe una secuencia de caracteres: ')

	result = first_not_repeating_char(char_sequence)

	if result == '_':
		print('Todos los caracteres se repiten')
	else:
		print(f'El primer caracter no repetido es {result}')