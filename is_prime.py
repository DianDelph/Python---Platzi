


# función para definir si un numero es primo
def is_prime(number):
	if number < 2:  # ningún numero menor a 2 es primo
		return False
	elif number == 2: #si el número es 2, es primo
		return True
	elif number > 2 and number  % 2 == 0: #si el número es mayor a 2 y divisible entre 2, no es primo
		return False
	else: 
		for i in range(3, number): # evalúo cada entero entre 3 y el número
			if number % i == 0: #si el entero lo divide, no es primo
				return False
		
		return True # si ningún entero lo divide, entonces es primo

def run():
	number = int(input('Escribe un número: '))
	result = is_prime(number)

	if result is True:
		print('Tu número es primo')
	else:
		print('Tu número no es primo')



if __name__ == "__main__":
	run()