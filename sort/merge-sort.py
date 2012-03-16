# Merge sort implementation

import math
import sys

def merge(lst,p,q,r):
  """ Merge the two lists l:left and r:right """
    
  end = 99999
  # some key that is guaranteed to be larger than any possible data in the list.
  # Here i have assumed that the list contains integer less than, say 99999
  # It is required the if-else condition in the for loop
  
  # make 2 lists
  lt=lst[p:(q+1)]
  rt=lst[(q+1):r]
  
  print p, q, r, lt, rt

  # append end to both the list. This helps in an easy check for end in list
  lt.append(end)
  rt.append(end)

  i=0
  j=0

  for k in range(p,r):
    # compare competing elements of both left and right lists
    if lt[i]<rt[j]:
      lst[k] = lt[i]
      i = i+1
    else:
      lst[k]= rt[j]
      j = j+1


  
def mergesort(lst, start, end):
  """ Split the list and call merge recursively """
  if start<end:
    split = int(math.floor((start+end)/2)) 
    mergesort(lst, start, split)
    mergesort(lst, split+1, end)
    merge(lst, start, split, end+1)

def main():
  lst = [5,2,4,7,1,3,2,6,-1]
  print lst
  mergesort(lst, 0, len(lst)-1)
  print lst

if __name__ == "__main__":
  main()

