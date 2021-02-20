from portfolio import Portfolio
from transactions import transactions

if __name__ == '__main__':
    portfolio = Portfolio(transactions)
    portfolio.print()
