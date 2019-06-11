#!/usr/bin/python
"""
1) Understanding the Problem
  [] find largest number (a)
  [] find smallest number (b)
  [] find the difference of a and b
  [] BUT a MUST be before b
2) Devise a Plan
3) Carry out Plan
4) Review
"""



import argparse

def find_max_profit(prices):
  bigMoney = prices[3]
  lilMoney = prices[1]

  profit = (bigMoney - lilMoney)

print(find_max_profit([6, 3, 4, 9, 1])

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))