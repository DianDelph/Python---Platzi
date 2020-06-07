
# las clases usan CamelCase por convención

class LampCLass:
	_LAMPS = ['''
		  .
	 .    |    ,
	  \   '   /
	   ` ,-. '
	--- (   ) ---
		 \ /
		_|=|_
		|_____|
	''',
           '''
		 ,-.
		(   )
		 \ /
		_|=|_
		|_____|
	''']

	def __init__(self, is_turned_on):  # constructor de clase
		self._is_turned_on = is_turned_on  # asigna el valor

	def turn_on(self):  # enciende la lámpara
		self._is_turned_on = True
		self._display_image()

	def turn_off(self):  # apaga la lámpara
		self._is_turned_on = False
		self._display_image()

	def _display_image(self):  # imprime según estado de la lámpara
		if self._is_turned_on:
			print(self._LAMPS[0])
		else:
			print(self._LAMPS[1])
