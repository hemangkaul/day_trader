from stock_data import get_price

class Wallet:
    def __init__(self):
        self.stocks = {}
        self.balance = 1000

    def add_stock(self, stock: str, price: float) -> None:
        if (self.balance - price) < 0:
            print("You can't afford that!")
        elif stock in self.stocks.keys():
            self.stocks[stock] = self.stocks[stock] + 1
            self.balance = self.balance - price
        else:
            self.stocks[stock] = 1
            self.balance = self.balance - price


    def sell_stock(self, stock: str, price: float) -> None:
        if stock not in self.stocks.keys():
            print("You don't own that stonk!")
        else:
            if self.stocks[stock] == 1:
                self.stocks.pop(stock)
                self.balance = self.balance + price
            else:
                self.stocks[stock] = self.stocks[stock] - 1
                self.balance = self.balance + price

    def exit_position(self, stock: str) -> None:
        if stock not in self.stocks.keys():
            print("You don't own that stonk!")
        else:
            self.balance = (float(self.stocks[stock]) * float(get_price(stock))) + self.balance
            del self.stocks[stock]

    def quit(self) -> None:
        sale = 0
        for stock in self.stocks.keys():
            sale = sale + float(get_price(stock)) * float(self.stocks[stock])
        self.balance = self.balance + sale
        self.stocks = {}

    def __str__(self):
        stock_list = ""
        for stock in self.stocks:
            stock_list = stock_list + stock + ": " + str(self.stocks[stock]) + "\n"
        return stock_list + "Balance: " + "$" + str(self.balance)

