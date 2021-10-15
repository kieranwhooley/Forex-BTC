# Forex-BTC

The purpose of the **forex-btc** program is to allow users to see current and historical currency and bitcoin exchange rate information, and then use these rates to convert various currencies. 

The program also allows users to see extra information related to the currencies and the countries they are used in.

The program is written using the **forex-python** library which can be found here:<br/>
https://forex-python.readthedocs.io/en/latest/index.html
   
The exchange rates in the library are taken from the **Rates API** publised by the European Central Bank:<br/>
https://ratesapi.io/

The Bitcoin information in the program is powered by **CoinDesk**:<br/>
https://old.coindesk.com/price/bitcoin

The program also uses the **flagpy** library to display the flags of supported countries:<br/>
https://pypi.org/project/flagpy/

The program is tested using **pytest**.
