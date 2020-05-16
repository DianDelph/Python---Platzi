
def factorial(number): # función que calculará el factorial
	if number == 0: # cuando el númrero llegue a cero
		return 1	 # acaba la función recursiva
	return number * factorial( number- 1) #mientras el número no sea 0, la función se llama así misma. 


if __name__ == "__main__":
	
	number = int (input( 'Escribe un número: '))

	result = factorial(number)

	print(result)
	