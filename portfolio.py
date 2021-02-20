from accounts import Stock


class Portfolio:
    def __init__(self, data):
        self.transactions = data

    def print(self):
        [stock.print_account() for stock in self.get_stocks()]

    def get_stocks(self):
        stocks = []
        for transaction in list(filter(lambda t: t["type"] == "stock", self.transactions)):
            stock = list(filter(lambda a: a.ticker == transaction['buy'], stocks))
            if len(stock) == 1:
                stock[0].add(transaction['amount'])
            else:
                stocks.append(Stock(
                    balance=transaction["amount"],
                    ticker=transaction["buy"],
                    instrument_type=transaction["type"],
                    country=transaction["country"],
                    service=transaction["service"]
                ))

        return stocks
