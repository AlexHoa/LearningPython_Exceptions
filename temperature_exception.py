#!usr/local/bin/python3.6
'''Module "temperature which converts from Celcius to Farenheit and Kelvin an vice versa
Celcius = (Farenheit -32)* 5/9
Farenheit = Celcius * 9/5 +32
Kelvin = Celcius + 273.15
Celcius = Kelvin - 273.15
'''

def conv_C_k(tempC):
	''' Conversion Celcius-Kelvin '''
	try:	
		assert tempC > -273.15
		tempK = tempC + 273.15
	except 	AssertionError:
		print('error: enter a value > - 273.15')
		tempK = None
	return tempK

def conv_K_C(tempK):
	''' Conversion Kelvin-Celcius '''
	try:
		assert tempK > 0
		tempC = tempK - 273.15
	except 	AssertionError:
		print('error: enter a value > 0')
		tempC = None
	return tempC


def conv_C_F(tempC):
	''' Conversion Celcius Farenheit '''
	try:
		assert tempC > -273.15
		tempF = tempC *9/5 + 32
	except 	AssertionError:
		print('error: enter a value > -273.15')
		tempF = None
	return tempF

def conv_F_C(tempF):
	''' Conversion Farenheit-Celcius '''
	try:
		assert tempF > -459.67
		tempC = (tempF - 32)*5/9
	except 	AssertionError:
		print('error: enter a value > -459.67')
		tempC = None
	return tempC

def conv_K_F(tempK):
	''' Conversion Kelvin-Farenheit'''
	try:	
		assert tempK > 0	
		tempF = tempK * 9/5 -459.67
	except 	AssertionError:
		raise 'error: enter a value > 0'
	return tempF

def conv_F_K(tempF):
	''' Conversion Farenheit-Kelvin '''
	try:
		assert tempF > -459.67
		tempK = (tempF + 459.67)*5/9
	except 	AssertionError:
		print('error: enter a value > -459.67')
		tempK = None
	return tempK


