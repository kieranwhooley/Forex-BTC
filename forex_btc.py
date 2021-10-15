#This program uses the forex-python, flagpy and countryinfo libraries which can be found here:
#https://forex-python.readthedocs.io/en/latest/index.html
#https://pypi.org/project/countryinfo/
#https://pypi.org/project/flagpy/
print("This program displays forex currency information")
print("This program uses the forex-python library which can be found here:")
print("https://forex-python.readthedocs.io/en/latest/index.html")
print("https://pypi.org/project/countryinfo/")
print("https://pypi.org/project/flagpy/")
print()

from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
from forex_python.bitcoin import BtcConverter
from countryinfo import CountryInfo
import flagpy as fp
import datetime

supported_currencies = ('AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK',
                        'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR')

supported_countries = {'AUD': "Australia", 'BGN': "Bulgaria", 'BRL': "Brazil", 'CAD': "Canada", 'CHF':"Switzerland", 'CNY':"China", 'CZK':"The Czech Republic", 'DKK':"Denmark", 'EUR':"Europe", 'GBP':"The United Kingdom", 'HKD':"Hong Kong", 'HRK':"Croatia", 'HUF':"Hungary", 'IDR':"Indonesia", 'ILS':"Israel", 'INR':"India", 'ISK':"Iceland",
                        'JPY':"Japan", 'KRW':"South Korea", 'MXN': "Mexico", 'MYR':"Malaysia", 'NOK':"Norway", 'NZD':"New Zealand", 'PHP':"The Philippines", 'PLN':"Poland", 'RON':"Romania", 'RUB':"Russia", 'SEK':"Sweden", 'SGD':"Singapore", 'THB':"Thailand", 'TRY':"Turkey", 'USD':"The United States", 'ZAR':"South Africa"}

def enter_valid_date():
    """
    A function that verifies that a date entered by a user is supported by the historical exchange rate data

    Returns
    -------
    date : datetime object
        A datetime object with the year, month, day, hour, minute, second, millisecond required for use in the historical exchange rate conversion calculations.

    """
    while True:
        try:
            #Ask the user for the year, month and date they want to check
            year = int(input("Enter a valid year between 1999 and 2020: "))
            month = int(input("Enter a numerical value for the month from 1 to 12: "))
            day = int(input("Enter a valid day for the month entered: "))
            try:
                #convert the input to a datetime object for use in the forex-python library
                date = datetime.datetime(year, month, day, 18, 36, 28, 151012)
                #only allow years that are supported by the forex-python library
                if year >= 1999 and year <= 2020:
                    break
                else:
                    print()
                    print("ERROR: Only years between 1999 and 2020 are supported")
            except:
                print()
                print("ERROR: Please only enter valid dates")
        except ValueError:
            print()
            print("ERROR: Please only enter valid numerical values for the year, month and day")
    
    return date

def enter_valid_bitcoin_date():
    """
    A function that verifies that a date entered by a user is supported by the historical Bitcoin data

    Returns
    -------
    date : datetime object
        A datetime object with the year, month, day, hour, minute, second, millisecond required for use in the historical exchange rate conversion calculations.

    """
    while True:
        try:
            #Ask the user for the year, month and date they want to check
            print()
            print("NOTE: For historical Bitcoin rates, only dates between August 2010 and today are supported")
            year = int(input("Enter a valid year between 2010 and 2020: "))
            month = int(input("Enter a numerical value for the month from 1 to 12: "))
            day = int(input("Enter a valid day for the month entered: "))
            try:
                #convert the input to a datetime object for use in the forex-python library
                date = datetime.datetime(year, month, day, 18, 36, 28, 151012)
                #only allow years that are supported by the forex-python library
                if (year < 2010 or year >= 2020):
                    print()
                    print("ERROR: Only dates between August 2010 and today are supported")
                elif (year == 2010 and month < 8):
                    print()
                    print("ERROR: Only dates between August 2010 and today are supported")
                else:
                    break
            except ValueError:
                print()
                print("ERROR: Please only enter valid dates")
        except ValueError:
            print()
            print("ERROR: Please only enter valid numerical values for the year, month and day")
    
    return date

def get_historical_exchange_rate_between_two_currencies(currency_one, currency_two, amount):
    """
    A function that takes two currency codes and an amount and display the value of each based on the value on a historical date in the past

    Parameters
    ----------
    currency_one : string
        A three letter currency code.
    currency_two : string
        A three letter currency code.
    amount : float
        An amount to convert.

    Returns
    -------
    None.

    """
    c = CurrencyRates()
    #Check to ensure the two currencies being compared are in the supported list
    if (currency_one not in supported_currencies) or (currency_two not in supported_currencies):
        print()
        print("ERROR: Please ensure both currency codes entered are in the list of supported currencies")
    #Output an error message if the two currencies being compared are the same as each other
    elif (currency_one == currency_two):
        print()
        print("ERROR: The currency codes entered are the same as each other, please enter two different currency codes")
    else:
        #Call function verify the date entered is valid
        date = enter_valid_date()
        
        #Get the year, month and day from the valid date to use in the output
        year = date.year
        month = date.month
        day = date.day
        
        #Get the historical exchange rates between the two currencies
        historical_rate_1 = c.get_rate(currency_one, currency_two, date)
        historical_rate_2 = c.get_rate(currency_two, currency_one, date)
        
        #Print out the historical exchange rates on the specified date
        print()
        print("Historical Exchange Rates:")
        print("---------------------------")
        print()
        print(f"Historical exchange rate of {get_currency_name(currency_one)} to {get_currency_name(currency_two)} on {day}-{month}-{year} (DD-MM-YYYY) was:\n{historical_rate_1}")
        print(f"Historical exchange rate of {get_currency_name(currency_two)} to {get_currency_name(currency_one)} on {day}-{month}-{year} (DD-MM-YYYY) was:\n{historical_rate_2}")
        print()
        
        #Convert the amount entered at the historical rate on the date specified
        converted_at_historical_rate_1 = c.convert(currency_one, currency_two, amount, date)
        converted_at_historical_rate_2 = c.convert(currency_two, currency_one, amount, date)
        
        #Display the symbol of the currency in the output
        symbol_of_currency_1 = get_currency_symbol(currency_one)
        symbol_of_currency_2 = get_currency_symbol(currency_two)
        
        #Display the output of the conversion at historical rates
        print("Conversion at Historical Exchange Rates:")
        print("-----------------------------------------")
        print()
        print(f"Values of exchange on {day}-{month}-{year} (DD-MM-YYYY) were:")
        print()
        print(f"{symbol_of_currency_1}{amount:.2f} {get_currency_name(currency_one)} in {get_currency_name(currency_two)} was {symbol_of_currency_2}{converted_at_historical_rate_1:.2f}")
        print(f"{symbol_of_currency_2}{amount:.2f} {get_currency_name(currency_two)} in {get_currency_name(currency_one)} was {symbol_of_currency_1}{converted_at_historical_rate_2:.2f}")

def get_historical_exchange_rates_for_one_currency(currency):
    """
    A function to get the exchange rates of a currency on a historical date

    Parameters
    ----------
    currency : currency
        A three letter currency code. 

    Returns
    -------
    None.

    """
    c = CurrencyRates()
    #Ensure the date entered is valid
    date = enter_valid_date()
    
    #Store the historical rates in a variable to be looped through
    historical_rates = c.get_rates(currency, date)
    
    return historical_rates, date

def display_historical_exchange_rates_for_one_currency(currency, historical_rates, date):
    """
    A function to display the exchange rates for a currency on a historical date 

    Parameters
    ----------
    currency : string
        A three letter currency code.
    historical_rates : dict
        A dictionary of currency codes and historical exchange rates in key-value pairs.
    date : datetime object
        A datetime object with the year, month, day, hour, minute, second, millisecond.

    Returns
    -------
    None.

    """
    #Get the year, month and day from the date for use in the output
    year = date.year
    month = date.month
    day = date.day
    
    print()
    print(f"Historical Rates for: {get_currency_name(currency)} on {day}-{month}-{year} (DD-MM-YYYY):")
    print("=====================")
    print()
    print("Code", "|", "Rate")
    print("----", "|", "----")
    #Print out the historical rates for the currency entered
    for k, v in historical_rates.items():
        print("", k,"|", v)

def get_historical_bitcoin_exchange_rate_for_a_currency(currency):
    """
    A function to get the value of a currency in Bitcoin at todays exchange rate

    Parameters
    ----------
    currency : string
        A three letter currency code.

    Returns
    -------
    None.

    """
    b = BtcConverter()
    #Ensure the date entered is valid
    date = enter_valid_bitcoin_date()
    
    #Get the Bitcoin rate for the currency on the specified date
    historical_btc_rate = b.get_previous_price(currency, date)
    
    return historical_btc_rate, date

def display_historical_bitcoin_price_for_one_currency(currency, historical_btc_rate, date):
    """
    A function to display the value of a currency in Bitcoin at todays exchange rate

    Parameters
    ----------
    currency : string
        A three letter currency code.
    historical_btc_rate : float
        The Bitcoin rate for the currency on the specified date.
    date : datetime object
        A datetime object with the year, month, day, hour, minute, second, millisecond..

    Returns
    -------
    None.

    """
    b = BtcConverter()
    
    #Get the year, month and day from the date for use in the output
    year = date.year
    month = date.month
    day = date.day
    
    #Display the price in Bitcoin on the specified date
    print()
    print("Historical Bitcoin Price:")
    print("========================")
    print()
    print(f"{b.get_symbol()}1 Bitcoin cost {get_currency_symbol(currency)}{historical_btc_rate:.2f} {get_currency_name(currency)} on {day}-{month}-{year} (DD-MM-YYYY)")
    print()
    
def display_current_exchange_rates(currency_code):
    """
    A function to display the exchange rates for all supported currencies for the currency code entered

    Parameters
    ----------
    currency_code : string
        A three letter currency code.

    Returns
    -------
    None.

    """
    c = CurrencyRates() 
    currency_rates = c.get_rates(currency_code)
    print("Current Exchange Rates for:", get_currency_name(currency_code))
    print("===========================")
    print()
    print("Code", "|", "Rate")
    print("----", "|", "----")
    for k, v in currency_rates.items():
        print("", k,"|", v)
        
def display_list_of_supported_currencies():
    """
    A function to display a list of the supported currencies to the user

    Returns
    -------
    None.

    """
    print()
    print("Supported Currencies:")
    print("====================")
    print()
    print("Code", "|", "Currency")
    print("----", "|", "--------")
    for k, v in supported_countries.items():
        #Get the name of the currency from the code and display both
        currency = get_currency_name(k)
        print("", k,"|", currency)

def get_currency_name(currency_code):
    """
    A function to display the name of currency from a currency code

    Parameters
    ----------
    currency_code : string
        A three letter currency code.

    Returns
    -------
    currency_name : string
        The name of the currency

    """
    c = CurrencyCodes()
    currency_name = c.get_currency_name(currency_code)
    return currency_name

def get_currency_symbol(currency_code):
    """
    A function to display the symbol of a currency code

    Parameters
    ----------
    currency_code : string
        A three letter currency code.

    Returns
    -------
    currency_symbol : string
        The symbol for the currency
    

    """
    c = CurrencyCodes()
    currency_symbol = c.get_symbol(currency_code)
    return currency_symbol
    
def display_flag_of_country(currency_code):
    """
    A function to display an image of the flag of the country associated with the currency code entered

    Parameters
    ----------
    currency_code : string
        A three letter currency code.

    Returns
    -------
    None.

    """
    #Europe and Hong Kong flags are not supported by flagpy so present a message to the user advising them no flag will display
    if currency_code in ('EUR', 'HKD'):
        country_name = supported_countries.get(currency_code)
        print("Image unavailable for", country_name)
    else:
        if currency_code in supported_countries.keys():
            country_name = supported_countries.get(currency_code)
            fp.display(country_name)
            print("Image of flag will display for", country_name)
            
def display_currency_information(currency_code):
    """
    A function to display information related to the currency code entered

    Parameters
    ----------
    currency_code : string
        A three letter currency code.

    Returns
    -------
    None.

    """
    #Change the country name to match how it is stored in the countryinfo library for the following countries
    if currency_code == "USD":
        country_name = "USA"
    elif currency_code == "GBP":
        country_name = "UK"
    elif currency_code == "CZK":
        country_name = "Czech Republic"
    elif currency_code == "PHP":
        country_name = "Philippines"
    else:
        country_name = supported_countries.get(currency_code)
    
    #Europe is not a country so it is not available in the countryinfo library
    if currency_code == "EUR":
        print()
        print("Information about", currency_code + ":")
        print("-----------------------")
        print("Currency Code:", currency_code)
        print("Currency Name:", get_currency_name(currency_code))
        print("Currency Symbol:", get_currency_symbol(currency_code))
        display_flag_of_country(currency_code)
    #Get country information for valid countries in supported list
    if (currency_code in supported_currencies) and currency_code != "EUR":
        #Get the country information using the countryinfo library
        country = CountryInfo(country_name)
        capital = country.capital()
        region = country.region()
        subregion = country.subregion()
        population = country.population()
        demonym = country.demonym()
        wikipedia_page = country.wiki()
        #Display the country information
        print()
        print("Information about", currency_code + ":")
        print("-----------------------")
        print("Currency Code:", currency_code)
        print("Currency Name:", get_currency_name(currency_code))
        print("Currency Symbol:", get_currency_symbol(currency_code))
        print("Country:", supported_countries.get(currency_code))
        print("Capital", capital)
        print("Region:", region)
        print("Sub-Region:", subregion)
        print("Population:", str(population) + " people")
        print("Demonym:", demonym)
        print("Wikipedia Link:", wikipedia_page)
        display_flag_of_country(currency_code)
    elif currency_code not in supported_currencies:
        print()
        print("ERROR: That currency is not supported")
    
def display_exchange_rates_between_two_currency_codes(currency_one, currency_two):
    """
    A function that takes in two currency codes and displays the exchange rate between them

    Parameters
    ----------
    currency_one : string
        A three letter currency code.
    currency_two : string
        A three letter currency code.

    Returns
    -------
    None.
    """
    c = CurrencyRates()
    #Check to ensure the two currencies being compared are in the supported list
    if (currency_one not in supported_currencies) or (currency_two not in supported_currencies):
        print()
        print("ERROR: Please ensure both currency codes entered are in the list of supported currencies")
    #Output an error message if the two currencies being compared are the same as each other
    elif (currency_one == currency_two):
        print()
        print("ERROR: The currency codes entered are the same as each other, please enter two different currency codes")
    #Get the exchange rates of both currencies to each other
    else:
        rate_1 = c.get_rate(currency_one, currency_two)
        rate_2 = c.get_rate(currency_two, currency_one)
        
        #Display the name of the currency in the output rather than the currency code
        name_of_currency_1 = get_currency_name(currency_one)
        name_of_currency_2 = get_currency_name(currency_two)
        
        print()
        print("Current Exchange Rates:")
        print("-----------------------")
        print()
        print("Current exchange rate of", name_of_currency_1, "to", name_of_currency_2, "is:", rate_1)
        print("Current exchange rate of", name_of_currency_2, "to", name_of_currency_1, "is:", rate_2)

def calculate_amount_of_one_currency_in_another(currency_one, currency_two, amount):
    """
    A function to display the specific value of one currency in another currency

    Parameters
    ----------
    currency_one : string
        A three letter currency code.
    currency_two : string
        A three letter currency code.
    amount : float
        The amount to convert between the currencies.

    Returns
    -------
    None.

    """
    c = CurrencyRates()
    #Check to ensure the two currencies being compared are in the supported list
    if (currency_one not in supported_currencies) or (currency_two not in supported_currencies):
        print()
        print("ERROR: Please ensure both currency codes entered are in the list of supported currencies")
    #Ouput an error message if the two currencies being compared are the same as each other
    elif (currency_one == currency_two):
        print()
        print("ERROR: The currency codes entered are the same as each other, please enter two different currency codes")
    #Get the exchange rates of both currencies to each other
    else:
        exchanged_value_1 = c.convert(currency_one, currency_two, amount)
        exchanged_value_2 = c.convert(currency_two, currency_one, amount)
        
        #Display the name of the currency in the output rather than the currency code
        name_of_currency_1 = get_currency_name(currency_one)
        name_of_currency_2 = get_currency_name(currency_two)
        
        #Display the symbol of the currency in the output
        symbol_of_currency_1 = get_currency_symbol(currency_one)
        symbol_of_currency_2 = get_currency_symbol(currency_two)
        
        print()
        print("Amounts after Exchange:")
        print("-----------------------")
        print(f"{symbol_of_currency_1}{amount:.2f} {name_of_currency_1} in {name_of_currency_2} is {symbol_of_currency_2}{exchanged_value_1:.2f}")
        print(f"{symbol_of_currency_2}{amount:.2f} {name_of_currency_2} in {name_of_currency_1} is {symbol_of_currency_1}{exchanged_value_2:.2f}")

def get_latest_bitcoin_price(currency_code):
    """
    A function to display the value of one unit of a currency in Bitcoin

    Parameters
    ----------
    currency_code : string
        A three letter country code.

    Returns
    -------
    None.

    """
    b = BtcConverter()
    #get the name and symbol of the currency from the code
    name_of_currency = get_currency_name(currency_code)
    symbol_of_currency = get_currency_symbol(currency_code)
    #get the Bitcoin symbol to display in output
    bitcoin_symbol = b.get_symbol()
    #get the value of one bitcoin in the currency entered
    one_bitcoin_in_currency = b.convert_to_btc(1, currency_code)
    
    #Display an error if the currency is not supported
    if currency_code not in supported_currencies:
        print()
        print("That currency is not supported")
    else:
        #Get the latest price of the currency in Bitcoin
        latest_price = b.get_latest_price(currency_code)
        print()
        print("Bitcoin Value")
        print("-------------")
        print()
        print(f"The price of one Bitcoin in {name_of_currency} is {bitcoin_symbol}{latest_price:.2f}")
        print(f"{symbol_of_currency}1 {name_of_currency} would get you {bitcoin_symbol}{one_bitcoin_in_currency:.10f} Bitcoin")
        
def convert_currency_to_bitcoin(currency_code, amount):
    """
    A function to convert a specified amount in a currency to Bitcoin

    Parameters
    ----------
    currency_code : string
        A three letter currency code.
    amount : float
        The amount you want to convert.

    Returns
    -------
    None.

    """
    b = BtcConverter() 
    #get the name and symbol of the currency from the code
    name_of_currency = get_currency_name(currency_code)
    symbol_of_currency = get_currency_symbol(currency_code)
    #get the Bitcoin symbol to display in output
    bitcoin_symbol = b.get_symbol()
    
    if currency_code not in supported_countries:
        print()
        print("ERROR: Please ensure the currency entered is in the list of supported currencies")
    else:
        #Get the value of the amount converted from the currency to Bitcoin
        currency_in_bitcoin = b.convert_to_btc(amount, currency_code)
        #Get the value of amount converted from Bitcoin to the currency
        bitcoin_in_currency = b.convert_btc_to_cur(amount, currency_code)
        print()
        print("Bitcoin Conversion")
        print("------------------")
        print(f"{symbol_of_currency}{amount:.2f} {name_of_currency} converted to Bitcoin is: {bitcoin_symbol}{currency_in_bitcoin:.10f}")
        print(f"{bitcoin_symbol}{amount:.2f} Bitcoin converted to {name_of_currency} is: {symbol_of_currency}{bitcoin_in_currency:.2f}")
                    
def display_main_menu_options():
    """
    A function to display the options available on the Main Menu of the program

    Returns
    -------
    None.

    """
    print("Forex Program Main Menu")
    print("=======================")
    print()
    print("Please select one of the options below:")
    print()
    print("C - Currency Menu: display a list of currency menu options")
    print("B - Bitcoin Menu: display a list of Bitcoin menu options")
    print("H - Help: display the Help Menu")
    print("Q - Quit: close the program")
    print()
    
def display_goodbye_message():
    """
    A function to display a message to the user when they quit the application

    Returns
    -------
    None.

    """
    print()
    print("Closing application, goodbye!")
    
def display_help_menu():
    """
    A function to display a Help menu to the user explaning the options available in the program

    Returns
    -------
    None.

    """
    print()
    print("Help Menu")
    print("=========")
    print()
    print("Forex Program")
    print("-------------")
    print()
    print("- This program displays currency information for most of the world's major currencies")
    print("- The currency information is both current and historical")
    print("- Curent and historical information is also available for Bitcoin prices")
    print()
    print("You can choose to conduct currency conversion calculations or find out more information on each currency by entering \"C\" on the Main Menu")
    print()
    print("You can choose to conduct Bitcoin conversion calculations by entering \"B\" on the Main Menu")
    print()
    print("Further Information")
    print("-------------------")
    print()
    print(" 1. The program is written using the forex-python library which can be found here:")
    print("    - https://forex-python.readthedocs.io/en/latest/index.html")
    print()
    print(" 2. The exchange rates in the library are taken from the RatesAPI publised by the European Central Bank")
    print("    - https://ratesapi.io/")
    print()
    print(" 3. The Bitcoin information in the program is taken from the CoinDesk API")
    print("    - https://www.coindesk.com/coindesk-api")
    print()
    print(" 4. The program also uses the flagpy library to display the flags of supported countries")
    print("    - https://pypi.org/project/flagpy/")
    print()

def display_invalid_input_message():
    """
    A function to display a message to the user if they have entered an invalid selection

    Returns
    -------
    None.

    """
    print()
    print("ERROR: Invalid selection")
    print("Please try again...")
    print()

def display_currency_menu_options():
    """
    A function to display the options available on the Currency Options sub-menu

    Returns
    -------
    None.

    """
    print()
    print("Currency Options")
    print("================")
    print()
    print("Please select one of the options below:")
    print()
    print("L - List: see a list of all the supported currencies in the program")
    print("R - Rates: see a list of todays exchange rates for a specific currency")
    print("T - Today: see todays exchange rates between two specific currency codes")
    print("E - Exchange: see the value of one currency in another currency at todays exchange rates")
    print("H - Historical: see the historical exchange rates for a currency on a specific date in the past")
    print("P - Past Conversion: convert an amount between two currency on a specific date in the past")
    print("I - Information: see further information related to a specific currency code and the country it is from")
    print("M - Menu: To return to the Main Menu")
    
def display_returning_to_main_menu_message():
    """
    A function to display a message to the user when they decide to go back to the Main Menu

    Returns
    -------
    None.

    """
    print()
    print("***Returning to Main Menu...***")
    print()
    
def display_bitcoin_menu_options():
    """
    A function to display the options available on the Bitcoin Options sub-menu

    Returns
    -------
    None.

    """
    print()
    print("Bitcoin Options")    
    print("================")
    print()
    print("Please enter one of the options below:")
    print()
    print("P - Price: see the value of a currency in the current price of Bitcoin")
    print("C - Conversion: convert a specific amount of a currency to Bitcoin")
    print("H - Historical: see the historical Bitcoin exchange rates for a currency on a specific date in the past")
    print("M - Menu: return to the Main Menu")
    
if __name__ == "__main__":
    #Add a Main Menu to the program
    print("Welcome to the Forex Program")
    print()
    while True:
        display_main_menu_options()
        #Let user enter selection on main menu
        selection = input("Please enter selection: ").upper()
        
        #Display error if user enters an invalid option
        if selection not in ("C", "B", "H", "Q"):
            display_invalid_input_message()
        #Close the program if the user enters Q
        elif selection == "Q":
            display_goodbye_message()
            break;
        #Display help menu if the user enters H
        elif selection == "H":
            display_help_menu()
        #Display Bitcoin Options sub-menu is the user enters B
        elif selection == "B":
            while True:
                display_bitcoin_menu_options()
                #Let user enter a selection on the Bitcoin sub-menu
                selection = input("Please enter selection: ").upper()
                #Display an error if the user enters an invalid option
                if selection not in ("P", "C", "H", "M"):
                    display_invalid_input_message()
                #Display the rate of one Bitcoin in a specified currency
                elif selection == "P":
                    currency = input("Enter the currency code you want to see displayed in Bitcoin: ").upper()
                    if currency in supported_currencies:
                        get_latest_bitcoin_price(currency)
                    else:
                        print()
                        print("ERROR: That currency is not supported")
                #Display the rate of one Bitcoin in a specified currency on a historical date in the past  
                elif selection == "H":
                    currency = input("Enter the currency code for which you want to see the historical exchange rate in Bitcoin: ").upper()
                    if currency in supported_currencies:
                        historical_btc_rate, date = get_historical_bitcoin_exchange_rate_for_a_currency(currency)
                        display_historical_bitcoin_price_for_one_currency(currency, historical_btc_rate, date)
                    else:
                        print()
                        print("ERROR: That currency is not supported")
                elif selection == "C":
                    while True:
                        currency_to_convert = input("Please enter the code of the currency you want to convert to Bitcoin: ").upper()
                        try:
                            amount = float(input("Please enter the amount you want to convert: "))
                        except ValueError:
                            print()
                            print("ERROR: Please enter a valid numerical amount")
                        else:
                            convert_currency_to_bitcoin(currency_to_convert, amount)
                            break
                #Return the Main Menu if the user enters M
                elif selection == "M":
                    display_returning_to_main_menu_message()
                    break
        #Display Currency Options sub-menu if the user enters C
        elif selection == "C": 
            while True:
                display_currency_menu_options()
                #Let user enter a selection on the Currency sub-menu
                selection = input("Please enter selection: ").upper()
                #Display an error if the user enters an invalid option
                if selection not in ("L", "R", "T", "E", "H", "P", "I", "M"):
                    display_invalid_input_message()
                #Return the Main Menu if the user enters M
                elif selection == "M":
                    display_returning_to_main_menu_message()
                    break
                #Display a list of supported currencies if the user enter L
                elif selection == "L":
                    display_list_of_supported_currencies()
                #Display a list of exchange rates on a date in the past for a selected currency
                elif selection == "P":
                    print()
                    print("Historical Exchange Rate Conversion:")
                    print("-----------------------------------")
                    currency_one = input("Please enter the code of the first currency: ").upper()
                    currency_two = input("Please enter the code of the second currency: ").upper()
                    try:
                        amount = float(input("Please enter the amount you want to convert: "))
                    except ValueError:
                        print()
                        print("ERROR: Please enter a valid numerical amount")
                    else:
                        get_historical_exchange_rate_between_two_currencies(currency_one, currency_two, amount)
                    #Confirm the currency code entered is supported, display an error if it is not
                elif selection == "H":
                    print()
                    print("Historical Exchange Rates:")
                    print("--------------------------")
                    currency = input("Enter the currency code you want to see historical exchange rates for: ").upper()
                    #Confirm the currency code entered is supported, display an error if it is not
                    if currency in supported_currencies:
                        historical_rates, date = get_historical_exchange_rates_for_one_currency(currency)
                        display_historical_exchange_rates_for_one_currency(currency, historical_rates, date)
                    else:
                        print()
                        print("ERROR: That currency is not supported")
                #Display input field to enter a currency code to check exchange rates if the user enters R
                elif selection == "R":
                    currency = input("Enter the currency code you want to see exchange rates for: ").upper()
                    #Confirm the currency code entered is supported, display an error if it is not
                    if currency in supported_currencies:
                        print()
                        display_current_exchange_rates(currency)
                    else:
                        print()
                        print("ERROR: That currency is not supported")
                #Display input field to enter a currency code to display information about the currency if the user enters I
                elif selection == "I":
                     currency = input("Enter the currency code you want to see further information about: ").upper()
                     display_currency_information(currency)
                #Display the current exchange rates between two currencies
                elif selection == "T":
                    currency_one = input("Please enter the code of the first currency: ").upper()
                    currency_two = input("Please enter the code of the second currency: ").upper()
                    display_exchange_rates_between_two_currency_codes(currency_one, currency_two)
                #Display the value of one currency in another at todays exchange rates
                elif selection == "E":
                    while True:
                        currency_one = input("Please enter the code of the first currency: ").upper()
                        currency_two = input("Please enter the code of the second currency: ").upper()
                        try:
                            amount = float(input("Please enter the amount you want to convert: "))
                        except ValueError:
                            print()
                            print("ERROR: Please enter a valid numerical amount")
                        else:
                            calculate_amount_of_one_currency_in_another(currency_one, currency_two, amount)
                            break