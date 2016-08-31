#!/usr/bin/python

import math
import sys
import numpy


def main():
  '''Main call. Parses, runs, and saves problem specific data'''
  with open('data/rosalind_ini2.txt') as input_data:
    numbers = input_data.read().split()

    input_data.close()



    #Get the hypotenuse for the input data
    hyp = hypotenuse(numbers)

    with open('output/ini2_hyp.txt', 'w') as output_data:
      output_data.write('{}' .format(hyp))
      output_data.close()
 

def hypotenuse(data):
  '''Calculates the hypotenuse and Returns the values'''
  a = float(data[0])
  b = float(data[1])
  a_square = math.pow(a, 2)
  print a_square
  b_square = math.pow(b, 2)
  print b_square
  ab_sum = a_square + b_square
  print ab_sum
  result = math.sqrt(ab_sum)
  return ab_sum


if __name__ == '__main__':
  main()




  



