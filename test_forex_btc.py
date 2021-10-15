#Program to test functions in the forex-btc program
print("This program tests functions in the  forex-btc program using pytest")
print()

from forex_btc import get_currency_name
from forex_btc import get_currency_symbol
from forex_btc import get_historical_exchange_rates_for_one_currency
from forex_btc import display_historical_exchange_rates_for_one_currency
from forex_btc import enter_valid_date
from forex_btc import enter_valid_bitcoin_date
from forex_btc import display_goodbye_message
from forex_btc import display_main_menu_options
from forex_btc import display_help_menu
from forex_btc import display_invalid_input_message
from forex_btc import display_currency_menu_options
from forex_btc import display_returning_to_main_menu_message
from forex_btc import display_bitcoin_menu_options
from forex_btc import display_list_of_supported_currencies
from forex_btc import get_historical_bitcoin_exchange_rate_for_a_currency
from forex_btc import display_historical_bitcoin_price_for_one_currency
from forex_btc import display_flag_of_country
from forex_btc import display_currency_information
from forex_btc import convert_currency_to_bitcoin
from forex_btc import calculate_amount_of_one_currency_in_another
from forex_btc import get_historical_exchange_rate_between_two_currencies
from unittest.mock import patch
import datetime

#Tests for getting currency and country information 

def test_get_currency_name():
    assert get_currency_name('USD') == "United States dollar"
    assert get_currency_name('EUR') == "European Euro"
    
def test_get_currency_symbol():
    assert get_currency_symbol('USD') == "US$"
    assert get_currency_symbol('EUR') == "€"
    assert get_currency_symbol('ILS') == "₪"
    
def test_display_flag_of_country(capfd):
    currency = "EUR"
    display_flag_of_country(currency)
    out, err = capfd.readouterr()
    output = out.strip()
    assert output == ('''Image unavailable for Europe''').strip()
    currency_2 = "USD"
    display_flag_of_country(currency_2)
    out, err = capfd.readouterr()
    output = out.strip()
    assert output == ('''Image of flag will display for The United States''').strip()
    
def test_display_currency_information(capfd):
    currency = "EUR"
    display_currency_information(currency)
    out, err = capfd.readouterr()
    output = out.strip()
    assert output == ('''Information about EUR:
-----------------------
Currency Code: EUR
Currency Name: European Euro
Currency Symbol: €
Image unavailable for Europe''').strip()
    
    currency = "ZAR"
    display_currency_information(currency)
    out, err = capfd.readouterr()
    output = out.strip()
    assert output == ('''Information about ZAR:
-----------------------
Currency Code: ZAR
Currency Name: South African rand
Currency Symbol: R
Country: South Africa
Capital Pretoria
Region: Africa
Sub-Region: Southern Africa
Population: 54002000 people
Demonym: South African
Wikipedia Link: http://en.wikipedia.org/wiki/south_africa
Image of flag will display for South Africa''').strip()

def test_convert_currency_to_bitcoin(capfd):
    currency = "MAD"
    amount = 45
    convert_currency_to_bitcoin(currency, amount)
    out, err = capfd.readouterr()
    output = out.strip()
    assert output == ('''ERROR: Please ensure the currency entered is in the list of supported currencies''').strip()
    
def test_get_historical_exchange_rate_between_two_currencies(capfd):
    currency_1 = "EUR"
    currency_2 = "MAD"
    amount = 50
    get_historical_exchange_rate_between_two_currencies(currency_1, currency_2, amount)
    out, err = capfd.readouterr()
    output = out.strip()
    assert output == ('''ERROR: Please ensure both currency codes entered are in the list of supported currencies''').strip()
    
    currency_1 = "EUR"
    currency_2 = "EUR"
    amount = 50
    calculate_amount_of_one_currency_in_another(currency_1, currency_2, amount)
    out, err = capfd.readouterr()
    output = out.strip()
    assert output == ('''ERROR: The currency codes entered are the same as each other, please enter two different currency codes''').strip()
 
    
def test_calculate_amount_of_one_currency_in_another(capfd):
    currency_1 = "EUR"
    currency_2 = "EUR"
    amount = 50
    calculate_amount_of_one_currency_in_another(currency_1, currency_2, amount)
    out, err = capfd.readouterr()
    output = out.strip()
    assert output == ('''ERROR: The currency codes entered are the same as each other, please enter two different currency codes''').strip()
    
    currency_1 = "MAD"
    currency_2 = "EUR"
    amount = 50
    calculate_amount_of_one_currency_in_another(currency_1, currency_2, amount)
    out, err = capfd.readouterr()
    output = out.strip()
    assert output == ('''ERROR: Please ensure both currency codes entered are in the list of supported currencies''').strip()
    
@patch("builtins.input")
def test_enter_valid_date(mock_input):
    input_values = [2015, 6, 5]
    mock_input.side_effect = input_values
    expected_value = enter_valid_date()
    assert expected_value == datetime.datetime(2015, 6, 5, 18, 36, 28, 151012)
    
@patch("builtins.input")
def test_enter_valid_bitcoin_date(mock_input):
    input_values = [2017, 6, 5]
    mock_input.side_effect = input_values
    expected_value = enter_valid_bitcoin_date()
    assert expected_value == datetime.datetime(2017, 6, 5, 18, 36, 28, 151012)

@patch("builtins.input")
def test_get_historical_exchange_rates_for_one_currency(mock_input):
    input_values = [2015, 5, 5]
    mock_input.side_effect = input_values
    historical_rate, date = get_historical_exchange_rates_for_one_currency('USD')
    assert date == datetime.datetime(2015, 5, 5, 18, 36, 28, 151012)
    assert historical_rate == {'GBP': 0.6611495907, 'HKD': 7.751101916, 'IDR': 13066.9425204642, 'ILS': 3.8834217865, 'DKK': 6.7146712243, 'INR': 63.4291625439, 'CHF': 0.933345327, 'MXN': 15.4404965368, 'CZK': 24.6127552397, 'SGD': 1.3368714581, 'THB': 33.4001978951, 'HRK': 6.8254025367, 'EUR': 0.8995232527, 'MYR': 3.6130250967, 'NOK': 7.598722677, 'CNY': 6.2022128272, 'BGN': 1.7592875776, 'PHP': 44.6370423675, 'PLN': 3.6144643339, 'ZAR': 12.0480345417, 'CAD': 1.2089592516, 'BRL': 3.0869838985, 'RON': 3.985607628, 'NZD': 1.3332733651, 'TRY': 2.713771701, 'JPY': 120.4641539984, 'RUB': 51.416749123, 'KRW': 1083.6736529639, 'USD': 1.0, 'AUD': 1.2700368805, 'HUF': 271.3861653324, 'SEK': 8.3911127103}

@patch("builtins.input")
def test_get_historical_bitcoin_exchange_rate_for_a_currency(mock_input):
    input_values = [2014, 10, 22]
    mock_input.side_effect = input_values
    historical_rate, date = get_historical_bitcoin_exchange_rate_for_a_currency('EUR')
    assert date == datetime.datetime(2014, 10, 22, 18, 36, 28, 151012)
    assert historical_rate == 299.8197

def test_display_historical_bitcoin_price_for_one_currency(capfd):
    currency = "EUR"
    date = datetime.datetime(2014, 10, 22, 18, 36, 28, 151012)
    historical_btc_rate = 299.8197
    display_historical_bitcoin_price_for_one_currency(currency, historical_btc_rate, date)
    out, err = capfd.readouterr()
    output = out.strip()
    assert output == ('''Historical Bitcoin Price:
========================

฿1 Bitcoin cost €299.82 European Euro on 22-10-2014 (DD-MM-YYYY)''').strip()
    
def test_display_historical_exchange_rates_for_one_currency(capfd):
    currency = "USD"
    date = datetime.datetime(2015, 5, 5, 18, 36, 28, 151012)
    historical_rate = {'GBP': 0.6611495907, 'HKD': 7.751101916, 'IDR': 13066.9425204642, 'ILS': 3.8834217865, 'DKK': 6.7146712243, 'INR': 63.4291625439, 'CHF': 0.933345327, 'MXN': 15.4404965368, 'CZK': 24.6127552397, 'SGD': 1.3368714581, 'THB': 33.4001978951, 'HRK': 6.8254025367, 'EUR': 0.8995232527, 'MYR': 3.6130250967, 'NOK': 7.598722677, 'CNY': 6.2022128272, 'BGN': 1.7592875776, 'PHP': 44.6370423675, 'PLN': 3.6144643339, 'ZAR': 12.0480345417, 'CAD': 1.2089592516, 'BRL': 3.0869838985, 'RON': 3.985607628, 'NZD': 1.3332733651, 'TRY': 2.713771701, 'JPY': 120.4641539984, 'RUB': 51.416749123, 'KRW': 1083.6736529639, 'USD': 1.0, 'AUD': 1.2700368805, 'HUF': 271.3861653324, 'SEK': 8.3911127103}
    display_historical_exchange_rates_for_one_currency(currency, historical_rate, date)
    out, err = capfd.readouterr()
    output = out.strip()
    assert output == ('''Historical Rates for: United States dollar on 5-5-2015 (DD-MM-YYYY):
=====================

Code | Rate
---- | ----
 GBP | 0.6611495907
 HKD | 7.751101916
 IDR | 13066.9425204642
 ILS | 3.8834217865
 DKK | 6.7146712243
 INR | 63.4291625439
 CHF | 0.933345327
 MXN | 15.4404965368
 CZK | 24.6127552397
 SGD | 1.3368714581
 THB | 33.4001978951
 HRK | 6.8254025367
 EUR | 0.8995232527
 MYR | 3.6130250967
 NOK | 7.598722677
 CNY | 6.2022128272
 BGN | 1.7592875776
 PHP | 44.6370423675
 PLN | 3.6144643339
 ZAR | 12.0480345417
 CAD | 1.2089592516
 BRL | 3.0869838985
 RON | 3.985607628
 NZD | 1.3332733651
 TRY | 2.713771701
 JPY | 120.4641539984
 RUB | 51.416749123
 KRW | 1083.6736529639
 USD | 1.0
 AUD | 1.2700368805
 HUF | 271.3861653324
 SEK | 8.3911127103''').strip()
    
#Tests for menu items displayed in program

def test_display_main_menu_options(capfd):
    display_main_menu_options()
    out, err = capfd.readouterr()
    output = out.strip()
    assert output == ('''Forex Program Main Menu
=======================

Please select one of the options below:

C - Currency Menu: display a list of currency menu options
B - Bitcoin Menu: display a list of Bitcoin menu options
H - Help: display the Help Menu
Q - Quit: close the program''').strip()

def test_display_help_menu(capfd):
    display_help_menu()
    out, err = capfd.readouterr()
    output = out.strip()
    assert output == ('''Help Menu
=========

Forex Program
-------------

- This program displays currency information for most of the world's major currencies
- The currency information is both current and historical
- Curent and historical information is also available for Bitcoin prices

You can choose to conduct currency conversion calculations or find out more information on each currency by entering "C" on the Main Menu

You can choose to conduct Bitcoin conversion calculations by entering "B" on the Main Menu

Further Information
-------------------

 1. The program is written using the forex-python library which can be found here:
    - https://forex-python.readthedocs.io/en/latest/index.html

 2. The exchange rates in the library are taken from the RatesAPI publised by the European Central Bank
    - https://ratesapi.io/

 3. The Bitcoin information in the program is taken from the CoinDesk API
    - https://www.coindesk.com/coindesk-api

 4. The program also uses the flagpy library to display the flags of supported countries
    - https://pypi.org/project/flagpy/''').strip()
    
def test_display_goodbye_message(capfd):
    display_goodbye_message()
    out, err = capfd.readouterr()
    output = out.strip()
    assert output == ("Closing application, goodbye!")
    
def test_display_returning_to_main_menu_message(capfd):
    display_returning_to_main_menu_message()
    out, err = capfd.readouterr()
    output = out.strip()
    assert output == ("***Returning to Main Menu...***")
    
def test_display_invalid_input_message(capfd):
    display_invalid_input_message()
    out, err = capfd.readouterr()
    output = out.strip()
    assert output == ("ERROR: Invalid selection\nPlease try again...").strip()
    
def test_display_bitcoin_menu_options(capfd):
    display_bitcoin_menu_options()
    out, err = capfd.readouterr()
    output = out.strip()
    assert output == ('''Bitcoin Options
================

Please enter one of the options below:

P - Price: see the value of a currency in the current price of Bitcoin
C - Conversion: convert a specific amount of a currency to Bitcoin
H - Historical: see the historical Bitcoin exchange rates for a currency on a specific date in the past
M - Menu: return to the Main Menu''').strip()

def test_display_currency_menu_options(capfd):
    display_currency_menu_options()
    out, err = capfd.readouterr()
    output = out.strip()
    assert output == ('''Currency Options
================

Please select one of the options below:

L - List: see a list of all the supported currencies in the program
R - Rates: see a list of todays exchange rates for a specific currency
T - Today: see todays exchange rates between two specific currency codes
E - Exchange: see the value of one currency in another currency at todays exchange rates
H - Historical: see the historical exchange rates for a currency on a specific date in the past
P - Past Conversion: convert an amount between two currency on a specific date in the past
I - Information: see further information related to a specific currency code and the country it is from
M - Menu: To return to the Main Menu''').strip()
    
def test_display_list_of_supported_currencies(capfd):
    display_list_of_supported_currencies()
    out, err = capfd.readouterr()
    currency_list = out
    assert currency_list.strip() == ('''
    Supported Currencies:
====================

Code | Currency
---- | --------
 AUD | Australian dollar
 BGN | Bulgarian lev
 BRL | Brazilian real
 CAD | Canadian dollar
 CHF | Swiss franc
 CNY | Chinese/Yuan renminbi
 CZK | Czech koruna
 DKK | Danish krone
 EUR | European Euro
 GBP | British pound
 HKD | Hong Kong dollar
 HRK | Croatian kuna
 HUF | Hungarian forint
 IDR | Indonesian rupiah
 ILS | Israeli new sheqel
 INR | Indian rupee
 ISK | Icelandic króna
 JPY | Japanese yen
 KRW | South Korean won
 MXN | Mexican peso
 MYR | Malaysian ringgit
 NOK | Norwegian krone
 NZD | New Zealand dollar
 PHP | Philippine peso
 PLN | Polish zloty
 RON | Romanian leu
 RUB | Russian ruble
 SEK | Swedish krona
 SGD | Singapore dollar
 THB | Thai baht
 TRY | Turkish new lira
 USD | United States dollar
 ZAR | South African rand''').strip()


    
    
    
