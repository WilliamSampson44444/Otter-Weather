"""
	filename: pyconverter.py

	author: Joseph Villegas

	abstract: a python file holding functions 
	          to perform temperature conversions
	          and time conversions
"""
import time

def fahrenheit_to_celsius(temperature):
	"""Covert from Fahrenheit to Celsius

	:param temperature: degree understood to be in Fahrenheit

	NOTE:

		Fahrenheit to Celsius formula: °C = (°F - 32) x 5/9 

		First subtract 32, then multiply by 5, then divide by 9.

	"""
	
	return (temperature - 32) * 5.0 / 9.0

def celsius_to_fahrenheit(temperature):
	"""Convert from Celsius to Fahrenheit

	:param temperature: degree understood to be in Celsius

	NOTE:
		Celsius to Fahrenheit formula: °F = (°C × 9/5) + 32 

		Multiply by 9, then divide by 5, then add 32.

	"""
	
	return 9.0 / 5.0 * temperature + 32

def kelvin_to_fahrenheit(temperature):
	"""Convert from Kelvin to Fahrenheit

	:param temperature: degree understood to be in Kelvin

	NOTE:
		Kelvin to Fahrenheit formula: °F = 9/5(K - 273.15) + 32

		Subtract 273.15, multiply by 9/5, then add 32.

	"""

	return (9.0 / 5.0) * (temperature - 273.15) + 32

def fahrenheit_to_kelvin(temperature):
	"""Convert from Fahrenheit to Kelvin

	:param temperature: degree understood to be in Fahrenheit

	NOTE:
		Fahrenheit to Kelvin formula: K = 5/9(°F - 32) + 273.15

		Subtract by 32, multiply by 5/9, then add 273.15.

	"""

	return (5.0 / 9.0) * (temperature - 32) + 273.15

def celsius_to_kelvin(temperature):
	"""Convert from Celsius to Kelvin

	:param temperature: degree understood to be in Celsius

	NOTE:
		Celsius to Kelvin formula: K = °C + 273.15

		Add 273.15.

	"""

	return temperature + 273.15

def kelvin_to_celsius(temperature):
	"""Convert from Kelvin to Celsius

	:param temperature: degree understood to be in Kelvin

	NOTE:
		Kelvin to Celsius formula: °C = K - 273.15

		Subtract 273.15.

	"""

	return temperature - 273.15

def epoch_to_human_readable_date(epoch):
	"""The Unix epoch/Unix time/POSIX time/Unix timestamp is the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT), 
	not counting leap seconds (in ISO 8601: 1970-01-01T00:00:00Z). Literally speaking the epoch is Unix time 0 (midnight 1/1/1970), 
	but 'epoch' is often used as a synonym for Unix time. The converter on this page converts timestamps in seconds (10-digit), milliseconds (13-digit) 
	and microseconds (16-digit) to readable dates.
	"""

	return time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(epoch))

