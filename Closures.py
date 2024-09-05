
# function after the parent function has returned.

def parent_function(person):
    #coins = 3

    def play_game():
        nonlocal coins()
        coins -= 1

        if coins > 1:
            print("\n" + person + "has" + str(coins) + "coins left.")
        elif coins == 1:
            print("\n" + person + "has" + str(coins) + "coins left.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game


martin = parent_function("Martin", 3)
pocky = parent_function("Pockey", 5)

martin()
martin()

pocky()

martin()