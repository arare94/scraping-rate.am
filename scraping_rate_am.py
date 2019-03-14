from bs4 import BeautifulSoup
import requests

source = requests.get('https://rate.am/en/').text

soup = BeautifulSoup(source, 'lxml')

# if you want to exit the program, click on
print("Enter 'q' at any time to quit.")
#here is the all currencies name
currencies = ('Usd', 'Eur', 'Rur', 'Gbp')

while True:
    # here I used the title() funtion avoiding from many (ors) 
    asked_currency = input('\nPlease enter the name of currency\nFor example (USD, EUR, RUR, GBP)-> ').title()
    #if our passed currency coincides with the currencies that we have, we continue execution else programm crashes
    if asked_currency in currencies:
        #finding minimum and maximum rates
        content = soup.find_all('tr', {'class':'btm'})[:2]
        minimum = [] # empty list for minimum rate
        maximum = [] # empty list for maximum rate

        #appending all minimum values from site into list
        for min_prices in content[0]:
            minimum.append(min_prices.text)

        #appending all maximum values from site into list
        for max_prices in content[1]:
            maximum.append(max_prices.text)

        #The title () function helps us check the value once for a response.
        if asked_currency == "Usd":
            print("\nThe minimum price for buying USD is {}, and the maximum price for selling USD is {}".\
                  format(minimum[1], maximum[2]))
        elif asked_currency == "Eur":
            print("\nThe minimum price for buying EUR is {}, and the maximum price for selling EUR is {}".\
                  format(minimum[3], maximum[4]))
        elif asked_currency == "Rur":
            print("\nThe minimum price for buying Rur is {}, and the maximum price for selling RUR is {}".\
                  format(minimum[5], maximum[6]))
        elif asked_currency == "Gbp":
            print("\nThe minimum price for buying GBP is {}, and the maximum price for selling GBP is {}".\
                  format(minimum[7], maximum[8]))

    ##if our passed currency coincides with the currencies that we have, we continue execution else programm crashes
    else:
        print("\n--------Invalid Currency! Quitting... Type again!--------")
        break



# print(minimum, maximum)

