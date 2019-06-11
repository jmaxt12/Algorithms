#!/usr/bin/python
"""
1) Understanding the Problem
  4 ways to eat cookies
  0 cookies once
  1 cookie 1 way
  2 cookies 2 ways - 1 at a time or 2 at a time
  3 cookes 4 ways - 1 at a time, 1 then two, 2 then 1, 3 at a time
2) Devise a Plan
  If I find out how many multiples of 3 there are, then I could multiply that by 4? Thinking aloud....
3) Carry out Plan
4) Review
"""
import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n < 0:
    return 0
  elif n == 0:
    return 1

  else:
    return (eating_cookies(n - 1)) + (eating_cookies(n - 2)) + (eating_cookies(n - 3))

print (eating_cookies(5))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')