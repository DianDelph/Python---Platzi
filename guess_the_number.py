
import random # modulo para generar números aleatorios

def run():
	number_found= False
	random_number = random.randint(0, 20)  # genera un número entero aleatorio entre 0 y 20

	while not number_found: 
		number = int (input('Intenta un número '))

		if number == random_number:
			print(' Felicidades. Encontraste el número')
			number_found= True
		elif number > random_number:
			print('El número misterioso es más pequeño')
		else:
			print('El número mistarioso es más grande')

if __name__ == "__main__":
	run()