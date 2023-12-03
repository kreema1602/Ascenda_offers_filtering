from datetime import datetime


def validate_date(date_string):
	try:
		# Attempt to parse the input date string
		datetime.strptime(date_string, '%Y-%m-%d')
		return True
	except ValueError:
		# If parsing fails, the input is not a valid date
		return False
