class Portfolio:
    def __init__(self, starting_cash):
        self.cash = starting_cash
        self.shares = 0
        self.history = []

    def buy(self, price):
        self.shares = self.shares + (self.cash / price)
        self.cash = 0

    def record_value(self, price):
        self.history.append(self.cash + self.shares * price)

    def get_history(self):
        return self.history
