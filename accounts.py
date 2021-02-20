import investpy


class Account:
    def __init__(self, balance, ticker, instrument_type, service):
        self.balance = balance
        self.ticker = ticker
        self.instrument_type = instrument_type
        self.service = service

    def add(self, amount):
        self.balance = self.balance + amount

    def subtract(self, amount):
        self.balance = self.balance - amount


class Stock(Account):
    def __init__(self, balance, ticker, instrument_type, country, service):
        self.country = country
        super().__init__(balance, ticker, instrument_type, service)

    def get_current_close(self):
        if self.instrument_type == 'stock':
            return investpy.get_stock_recent_data(stock=self.ticker, country=self.country).tail(1).iloc[0]['Close']

    def get_current_value(self, currency):
        value_in_usd = self.get_current_close() * self.balance
        cross = investpy.get_currency_cross_recent_data(f'USD/{currency}').tail(1).iloc[0]['Close']
        return value_in_usd * cross

    def print_account(self, currency):
        print(f'{self.ticker}: {self.balance} ({self.get_current_value(currency)} {currency})')
