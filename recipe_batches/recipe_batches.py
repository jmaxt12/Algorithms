#!/usr/bin/python
"""
1) Understanding the Problem
  recipe needs to have values
  ingredients need to have values
  if ingredients values >= recipe then you can make recipe
2) Devise a Plan
  the "//" in math gives me the ammount of times a number goes into another number
3) Carry out Plan
4) Review
"""

import math

def recipe_batches(recipe, ingredients):
  batches = []
  if len(recipe) == len(ingredients):
    for key in recipe:
      batches.append(ingredients[key]//recipe[key])
    return min(batches)
  else:
      return 0


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 232, 'butter': 103, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))