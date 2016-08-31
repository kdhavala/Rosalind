#!/usr/bin/python

'''
A solution to a ROSALIND problem from the Python location.  
Problem Title: Strings and Lists
Rosalind Python ID: INI3
Rosalind Python #: 003
URL: http://rosalind.info/problems/ini3/
'''

import sys

with open('data/rosalind_ini3.txt') as input_data:
  string, indices = [line.strip() for line in input_data.readlines()]
  a,b,c,d = map(int, indices.split())


  

slices = [string[a:b+1], string[c:d+1]]

with open('output/ini3.txt', 'w') as output_data:
  output_data.write(' '.join(slices))




