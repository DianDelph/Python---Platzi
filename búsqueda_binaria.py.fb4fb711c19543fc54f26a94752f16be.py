#!/usr/bin/env python3

def binary_search(numbers, number_to_find, low, high):

	if low > high: # si el número bajo es más grande que el alto
		return False   # significa que no lo encontré

	mid = (low + high) // 2  # "//" regresa un entero

	if numbers[mid] == number_to_find: # si el número está a la mitad
		return True 

	elif numbers[mid] > number_to_find:  # si el número de enmedio es más grande
		return binary_search(numbers, number_to_find, low, mid - 1 ) # la función se llama así misma. Mandamos la lista, el número a encontrar, el índice menor y el nuevo límite es la mitad menos 1
	else:
		return binary_search(numbers, number_to_find, mid + 1, high)# la función se llama así misma. Mandamos la lista, el número a encontrar, el nuevo límite menor es la mitad + 1y el mayor se queda como estaba


if __name__ == "__main__":

	numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]

	number_to_find = int(input('Ingresa un número: '))

	result = binary_search(numbers, number_to_find, 0 , len(numbers)- 1)

	if result is True:
		print('El número si está en la lista')
		f'El número {number_to_find} sí está en la lista'
	else:
		print('El número no está en la lista')

