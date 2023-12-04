import datetime
import json
from utilities.ClosestMerchant import closestMerchant
from utilities.date_validator import validate_date
from utilities.offerFilterCategoryAndValidDate import filterCate_ValidDate


def main():
	# Read user input
	print("========================================")
	print("Asenda Travel Platform - Offer Filtering")
	input_date = input("Enter check-in date (yyyy-mm-dd): ")
	while not validate_date(input_date):
		input_date = input("Your input was not follow the (yyyy-mm-dd) format, please input again: ")
	input_date = datetime.datetime.strptime(input_date, '%Y-%m-%d')
	
	# input_date = datetime.datetime(2019, 12, 25)
	
	# read JSON file
	inputFile = open("test/input.json")
	data = json.load(inputFile)
	
	# Create 2 empty offer
	offer1, offer2 = {}, {}
	
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
			
			# Case 3 offers in the same category
			if i["category"] == offer1["category"] == offer2["category"]:
				if i["merchants"]["distance"] < offer1["merchants"]["distance"]:
					offer1 = i
				elif i["merchants"]["distance"] < offer2["merchants"]["distance"]:
					offer2 = i
				
			# Replace second offer with current offer if offer1 = offer 2
			if i["category"] != offer1["category"] and offer1["category"] == offer2["category"]:
				offer2 = i
			
			# Check if current offer is better than offer1 (same category)
			elif i["category"] == offer1["category"] and i["merchants"]["distance"] < offer1["merchants"]["distance"]:
				offer1 = i
			# Check if current offer is better than offer1 (same category)
			elif i["category"] == offer2["category"] and i["merchants"]["distance"] < offer2["merchants"]["distance"]:
				offer2 = i
			
			elif i["category"] != offer1["category"] and offer1["category"] != offer2["category"]:
				# Replace current offer with offer1 if its distance better
				if i["merchants"]["distance"] < offer1["merchants"]["distance"]:
					offer1 = i
					
				# Replace current offer with offer2 if its distance better
				elif i["merchants"]["distance"] < offer2["merchants"]["distance"]:
					offer2 = i
	
	# Write 2 offer into JSON file
	resultDict = {"offers": [offer1, offer2]}
	with open("output.json", "w") as outputFile:
		outputFile.write(json.dumps(resultDict))
	
	print("Best offer available:")
	if not offer1:
		print("There is no offers available :(")
	else:
		print(offer1)
		print(offer2)
	
	print("Your offers have been save to output.json file !")
	
	inputFile.close()
	outputFile.close()


if __name__ == "__main__":
	main()
