from pty import spawn


def online_stock_span(price: int, days: int):
    """
    span: days for which the price of stock was less than today's
    Algo:
    1. just store the current price and remove all prices lesser than this price
    2. the number of removed prices is the span
    :param stock:
    :return:
    """
    days += 1  # days the stock was higher
    stock_span = [] # contains the stock span and its day of the format (price, days)


    while stock_span and stock_span[-1][0] < price:
        stock_span.pop()

    if stock_span: # check if there are elements, if the price could be the largest then the stack is empty
        span = days - stock_span[-1][1]
    else:
        span = days

    stock_span.append((price, days))
    return span



