"""

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


We are going to utilize sliding window method for efficiency

Approach:
track the min number: This will be the best buying opportunity. if you find a number lower, that will
be the new minimum

track the max profit so far and update it accordingly in case:



"""
def best_buy(stocks):
    if not stocks:
        return 'Nil'
    maxProfit = 0
    minPrice = stocks[0]

    for prices in stocks:
        if prices < minPrice:
            minPrice = prices
        max_profit = prices - minPrice
        maxProfit = max(maxProfit, max_profit)
    return maxProfit if maxProfit > 0 else None
print(best_buy([7,1,5,3,6,4]))















# def best_buy(stocks:list):
#     if not stocks:
#         return "Empty"
#     elif len(stocks) < 2:
#         return stocks
#     buy_stock_at_lowest_price = min(stocks)
#     max_profit = 0
#
#     for price in stocks:
#         get_profit = price - buy_stock_at_lowest_price
#         new_max_profit = max(max_profit, get_profit)
#         return f"This is the max: {new_max_profit}"
#
# res = best_buy([7,1,5,3,6,4])
# print(res)


"""correct approach"""

# def stock_price(stocks:list)->int or float:
#     if not stocks:
#         return "empty"
#     elif len(stocks) < 2:
#         return 'Xero'
#
#     min_price = stocks[0]
#     max_profit = 0
#
#     for i in stocks[1:]:
#         current_price = i
#         if current_price < min_price:
#             min_price = current_price
#         get_price = current_price - min_price
#         if get_price > max_profit:
#             max_profit = get_price
#     return max_profit
#
# print(stock_price([7,1,5,3,6,4]))



# def stock_market(stock_price:list)->int or float:
#     """base case"""
#     if len(stock_price) < 2:
#         return 'nil'
#     minimum_price = stock_price[0]
#     maximum_profit = 0
#
#     for i in stock_price[1:]:
#         current_price = i
#         if current_price < minimum_price:
#             minimum_price = current_price
#         get_max_profit = current_price - minimum_price
#         if get_max_profit > maximum_profit:
#             maximum_profit = get_max_profit
#     return maximum_profit
#
#
# result = stock_market([7,1,5,3,6,4])
# print(result)





