import datetime
import json
from Ascenda_offers.date_validator import validate_date
from Ascenda_offers.offerFilterCategoryAndValidDate import filterCate_ValidDate
from Ascenda_offers.ClosestMerchant import closestMerchant


def main():
	# Read user input
	input_date = input("Enter a date (yyyy-mm-dd): ")
	while not validate_date(input_date):
		input_date = input("Your input was not follow the (yyyy-mm-dd) format, please input again: ")
	input_date = datetime.datetime.strptime(input_date, '%Y-%m-%d')
	
	# read JSON file
	f = open("input.json")
	data = json.load(f)
	
	# Create 2 empty offer
	offer1, offer2 = {}, {}
	
	input_date = datetime.datetime(2019, 12, 25)
	
	for i in data["offers"]:
		if filterCate_ValidDate(i, input_date):
			i["merchants"] = closestMerchant(i["merchants"])
			# Create offer1 if offer1 not exist
			if not offer1:
				offer1 = i
				continue
			# Create offer2 if offer1 not exist
			if offer1 and not offer2:
				offer2 = i
				# This line ensure offer2.distance > offer1.distance
				if offer1["merchants"]["distance"] > offer2["merchants"]["distance"]:
					offer1, offer2 = offer2, offer1
				continue
			# Replace second offer with current offer if offer1 = offer 2
			if i["category"] != offer1["category"] and offer1["category"] == offer2["category"]:
				offer2 = i
			
			if i["category"] != offer1["category"] and offer1["category"] != offer2["category"]:
				# Replace current offer with offer1 if its distance better
				if i["merchants"]["distance"] < offer1["merchants"]["distance"]:
					offer1 = i
				# Replace current offer with offer2 if its distance better
				elif i["merchants"]["distance"] < offer2["merchants"]["distance"]:
					offer2 = i
	
	# Write 2 offer into JSON file
	resultDict = {"offers": [offer1, offer2]}
	with open("output.json", "w") as outfile:
		outfile.write(json.dumps(resultDict))


if __name__ == "__main__":
	main()
