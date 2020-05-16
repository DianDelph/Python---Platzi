#convierte mxn to col
def foreing_exchange_calculator(ammount):2
	mex_to_col_rate= 165.23 # tipo de cambio actual

	return mex_to_col_rate * ammount 

def run():
	print('C U R R E N C Y   C O N V E R T E R')
	print(' Mexican pesos to Colombian pesos.')
	print(' ')

	ammount = float(input('Enter the ammount of Mexican pesos to convert '))  # voy a pedir cuánto MXN a convertir

	result = foreing_exchange_calculator (ammount)

	print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount, result)) # aqui imprimo el resultado
	print(' ')

if __name__ == "__main__":
	run()
	print('Final {}'.format(ammount))
