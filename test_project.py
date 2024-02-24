import wallet

def test_add_stock():
    player = wallet.Wallet()
    player.add_stock("ARM", 100.00)
    assert player.balance == 900


def test_sell_stock():
    player = wallet.Wallet()
    player.add_stock("ARM", 100.00)
    player.sell_stock("ARM", 100.00)
    assert player.balance == 1000


def test_exit_position():
    player = wallet.Wallet()
    player.add_stock("ARM", 100.00)
    player.add_stock("ARM", 100.00)
    player.add_stock("ARM", 100.00)
    player.exit_position("ARM")
    assert player.stocks == {}
