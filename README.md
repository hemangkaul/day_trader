# DAY TRADER
#### Video Demo:
https://youtu.be/r6IiQ7VrJok
#### Description:
My project is an implementation of a game I call Day Trader. The basic game tenent of the game is to buy low and sell high. The game uses real stocks as the basis of the game and gathers real-time stock prices scraped from Yahoo Finance. This game needs to be played during high volatility trading hours to really enjoy the ups and downs of the market.

My project is built with three main functionalities. The first and most important functionality is scraping the web for financial data. This was done using two external libraries, requests and Beautiful Soup. Using the requests library we make a GET request for the yahoo finance web page for the stock given, and then using the beautiful soup html parser we are able to extract the exact price of the stock.

The next most important class, or arguably the most important, is the Wallet. I have decided to represent the "player" as a Wallet of stocks and money. I have decided to represent the player as a Wallet because the main functionalities of the wallet are to add_stock, sell_stock, exit_position. The add_stock functionality simply adds 1 stock to the players wallet, represented as a dict, if the player can afford it, which executes a check to the balance of the player. The sell_stock functionality simply sells 1 stock from the players wallet if the player owns that stock, and adds the funds from the resulting sale to the player's balance. The exit_position functionality allows a player to sell every stock of a specific stock in order to exit a position quickly, and does nothing if the player doesn't own any of that stock. There is also the quit() function which allows the player to exit all positions and end the game.

My main function basically executes the main logic of the game which is to continuously ask the player what stock they want to buy sell or exit from. This is done with a while loop and prompting input from the user. Since the game is built around stocks the stock question is asked repeatedly. There is some functionality that catches invalid input, if the value of the input is not one of the approved options.

The game is run simply, by executing python project.py in your terminal. It requires pyfiglet, bs4, and requests.

In order to test the project we basically test the Wallets ability to add, sell, and retain stocks/state. There are three functions in test_project.py which test the ability of the wallet to add a stock, in test_add_stock. In test_sell_stock, the same concept but this time to sell stock and maintain the correct state of the wallet. And then finally there is test_exit_position, which tests the ability of the user to sell all of one stock.

That is the basic functionality of my project.
