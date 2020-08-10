# FUZZY TRADER

This is a trader simulator where the user can inform a given amount of money to invest (USD) and the app will show 4 options of investments: 2 stocks (Apple and Microsoft) and 2 cryptocurrencies (Bitcoin and Ethereum). The user will pick one of the offers and add that to its investments. The app will store the investment data for a given user and it will show its current investment state.


### PROJECT TECH SPECS

These are the main technologies used in this project:
+ Runtime: Python 3.7.2
+ Framework: Django 3.1
+ Host: Heroku


### USAGE
To use the Fuzzy Trader, using the web browser of your preference, access [paste Heroku link here]


### DEVELOPMENT SETUP

To get setup for development in this project, follow the steps bellow:
1. Clone the repo
2. Install Python 3.7.2
3. Create a Python 3.7.2 virtualenv
4. Install the dependencies (requirements.txt)
5. Run `python manage.py runserver`
6. Add the following env variables (you may need to create a free account in the external apis used): SECRET_KEY (value=django secret key), ALPHA_VANTAGE_KEY (value=alpha vantage api key),  COIN_API_KEY (value=coin api key), MARKET_STACK_KEY (value=market stack api key), PYTHONPATH (value=root directory of this project, aka same level as manage.py file)
7. Access the app at localhost:8000 using your browser
8. To run the automated tests do:`python manage.py test`


### KNOWN LIMITATIONS AND IMPROVEMENTS:
+ As this project uses free keys for the external api access, they may be limited. Some of them have a limit of 100 uses per day.

+ User interface can be improved with more styling.


### EXTERNAL RESOURCES

This web application uses the following external resources:
+ https://www.coinapi.io/
+ https://www.alphavantage.co/
+ https://marketstack.com/
