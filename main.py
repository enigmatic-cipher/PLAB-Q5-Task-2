"""
Given a List of numbers as input where each element is less than 1000. Print the
number which is nearest to 1000.
Input-> [179,256,9]
Output-> 256
"""

lst = [179,256,9]
ln = len(lst)
index = 0
for i in range(0,ln):
  e = lst[i]
  index = index + 1
  