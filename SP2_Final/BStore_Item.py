class Item():
    def __init__(self, num, name, year, genre, price, availb):
        self.name = name
        self.year = year
        self.genre = genre
        self.price = price
        self.availb = availb  

        self.tuple = (num, name, year, genre, price, availb)

# all "0" states refer to the ideal state:
    # price at 0 means no price/free
    # state at 0 means no discount
    # availb at 0 means unavailable