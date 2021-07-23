import sys


# Quadratic n^2 loops
def maxProfit(prices):
    bprice, sprice, mprofit = sys.maxsize, -sys.maxsize + 1, 0
    k, l = 0, 0
    for k in range(len(prices)):
        if prices[k] < bprice:
            bprice = prices[k]
            for l in range(k + 1, len(prices)):
                if prices[l] - bprice > mprofit:
                    sprice = prices[l]
                    mprofit = sprice - bprice
                l += 1
        k += 1
    return mprofit


def maxProfit_1(prices):  # IMPROVEMENT!!! - but not optimal just yet
    bprice, mprofit = 0, 0
    for i in range(len(prices)):
        bprice = prices[i]
        prices_ = prices[i: len(prices)]
        if len(prices_) > 0 and max(prices_) - bprice > mprofit:
            mprofit = max(prices_) - bprice
    return mprofit


def maxProfit_2(prices):
    b_price1, mprofit1 = prices[0], 0
    b_price2, mprofit2 = 0, 0
    switch = False
    for k in range(len(prices)):
        if prices[k] < b_price1 and not switch:
            b_price2 = prices[k]
            switch = True
        if (prices[k] < b_price2 and switch):
            if (mprofit1 > mprofit2):
                b_price2 = prices[k]
                mprofit2 = 0
            elif (mprofit1 <= mprofit2):
                b_price1, mprofit1 = b_price2, mprofit2
                b_price2 = prices[k]
                mprofit2 = 0
        if switch and prices[k] - b_price2 > mprofit2:
            mprofit2 = prices[k] - b_price2
        elif prices[k] - b_price1 > mprofit1:
            mprofit1 = prices[k] - b_price1
    if (mprofit1 >= mprofit2):
        return mprofit1
    else:
        return mprofit2

def maxProfit_Final(prices):
    bprice = prices[0]
    mprofit = 0
    for i in range(1, len(prices)):
        if prices[i] < bprice:
            bprice = prices[i]
        if prices[i] - bprice > mprofit:
            mprofit = prices[i] - bprice
    return mprofit


if __name__ == '__main__':
    a = [4, 2, 1, 7]
    print(maxProfit_Final(a))
