import csv

#reading cvc and returns dicts

def getDataInput(filename):
    with open(filename) as file:
        reader = csv.DictReader(file)
        return [row for row in reader]
#getting median
    
def getMedian(price_list):
    n = len(price_list)
    if n % 2 == 1:
        return float(price_list[n // 2])
    else:
        return (float(price_list[n // 2 - 1]) + float(price_list[n // 2])) / 2
#defining the csv 
def main():
    filename = "RealEstateData.csv" 
    records = getDataInput(filename)
    #searching for the column names for data
    city_key = next((key for key in records[0] if "city" in key.lower()), None)
    type_key = next((key for key in records[0] if "type" in key.lower()), None)
    price_key = next((key for key in records[0] if "price" in key.lower()), None)

    #dictionary storing all these
    prices = []
    city_totals = {}
    type_totals = {}
    
    for record in records:
        city = record[city_key]
        property_type = record[type_key]
        
        try:
            price = float(record[price_key].replace(',', ''))
        except ValueError:
            price = 0  #error handle
        
        prices.append(price)
        city_totals[city] = city_totals.get(city, 0) + price
        type_totals[property_type] = type_totals.get(property_type, 0) + price
    
    prices.sort()
    #outputs
    print(f"Minimum:      ${min(prices):,.2f}")
    print(f"Maximum:      ${max(prices):,.2f}")
    print(f"Total:        ${sum(prices):,.2f}")
    print(f"Average:      ${sum(prices)/len(prices):,.2f}")
    print(f"Median:       ${getMedian(prices):,.2f}")
    
    print("\nSummary by Property Type")
    for property_type, total in type_totals.items():
        print(f"{property_type:<20} ${total:,.2f}")
    
    print("\nSummary by City")
    for city, total in sorted(city_totals.items()):
        print(f"{city:<20} ${total:,.2f}")

if __name__ == "__main__":
    main()

#spent countless hours on this one im sure there alot of errors here and i would greatly appreciate any tips. i  was a little confused on the regards to zip codes, did you want a seperate output for zip codes?  The city type is alphabetical order im not sure how to order it like the way you did honestly other than making a custom order
