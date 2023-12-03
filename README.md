# Ascenda Travel Platform - Offer Filterng CLI
## About this app
This is a command line application that filters and selects offers for Ascenda Travel Platform based on certain criteria. The application accepts a customer check-in date and filters offers from an external partner API.

## Criteria
- Only select offers with category that is `Restaurant`, `Retail` or `Activity`. Category ID mapping is 


  ```
  Restaurant: 1 
  Retail: 2
  Hotel: 3
  Activity: 4
  ```
-  Offer needs to be valid till checkin date + 5 days. (valid_to is in `YYYY-MM-DD`)
-  If an offer is available in multiple merchants, only select the closest merchant
-  This class should only return 2 offers even though there are several eligible offers
-  Both final selected offers should be in different categories. If there are multiple offers in the same category give priority to the closest merchant offer.
-  If there are multiple offers with different categories, select the closest merchant offers when selecting 2 offers

## Getting started
1. Replace `test/input.json` with a response from the Ascenda API.
2. Run `main.py`. Example: `python main.py`
3. Retrieve the result offers from `test/output.json`.

## Build environment
- IDE: PyCharm 2023.2.5 (Community Edition)
- Python version: Python 3.12
