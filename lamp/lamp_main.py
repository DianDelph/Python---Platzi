
from lamp_class import LampClass

def run():
	lamp = LampClass(is_turned_on=False)  # manda la variable al constructor
	while True:

		command = input('''
			¿Qué deseas hacer?

			[p]render
			[a]pagar
			[s]alir
		''')

		if command == 'p':
			lamp.turn_on()
		elif command == 'a':
			lamp.turn_off()
		else:
			break


if __name__ == '__main__':
	run()
