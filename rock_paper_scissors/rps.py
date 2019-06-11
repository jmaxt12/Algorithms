#!/usr/bin/python
"""
1) Understanding the Problem
2) Devise a Plan
3) Carry out Plan
4) Review
"""
import sys

def rock_paper_scissors(n):
  pass 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')