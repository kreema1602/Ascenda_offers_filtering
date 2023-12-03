import datetime


def filterCate_ValidDate(i, input_date):
	validDate = datetime.datetime.strptime(i["valid_to"], '%Y-%m-%d').date()
	if validDate < (input_date + datetime.timedelta(days=5)).date():
		return False
	if i["category"] == 3:
		return False
	return True