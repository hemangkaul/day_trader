from stock_data import get_price
from pyfiglet import Figlet
import wallet

def main():
    game()

def game() -> None:
    figlet = Figlet()
    fonts = figlet.getFonts()
    print(figlet.renderText("DAY TRADER!!!"))
    player = wallet.Wallet()
    while True:
        print(player)
        while True:
            stonk = input("Stonk?\n").upper()
            if stonk == "QUIT":
                player.quit()
                action = "quit"
                break
            try:
                price = get_price(stonk)
                print(f"Price: {price}")
                action = input("What would you like to do? Buy, sell, or exit your position?\n").lower()
                break
            except ValueError:
                print("Not a stonk")
        if action == "buy":
            player.add_stock(stonk, float(price))
        elif action == "sell":
            player.sell_stock(stonk, float(price))
        elif action == "exit":
            player.exit_position(stonk)
        elif action == "quit":
            player.quit()
            print(player)
            break
        else:
            print("Not a valid action!")


if __name__ == "__main__":
    main()
