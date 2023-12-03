def closestMerchant(merchantList):
	smallest = merchantList[0]
	for i in merchantList:
		if i["distance"] < smallest["distance"]:
			smallest = i
	return smallest
