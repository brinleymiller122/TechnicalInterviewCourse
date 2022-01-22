# Say you have an array for which the ith element is the price of a given stock on day i
# If you were only permitted to complete at most one transaction (i.e, buy one and 
# sell one share of the stock) design an algorithm to find the maximum profit
# This problem came from leetcode.com

input_array = [7, 1, 5, 3, 6, 4]
# Output = 5

#brute force

def buyStock(n):
    max_profit= 0
    

    for first_price in range(len(n)):
        for second_price in range(first_price +1, len(n)):
           
            if max_profit < n[second_price] - n[first_price]:
                max_profit=n[second_price] - n[first_price]

    return max_profit

print(buyStock(input_array))

#better

def buyStocks(n):
    max_profit=0
    min_num= n[0]

    for num in n:
        if num < min_num:
            min_num=num
        max_profit=max(max_profit, num - min_num)
    return max_profit

print(buyStocks(input_array))