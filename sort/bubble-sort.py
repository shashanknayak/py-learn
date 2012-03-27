import sys

def main():
  inp = [5,1,4,2,8]
  print "Unsorted list: ",inp
  sort(inp)

def sort(inp):
  count = len(inp)
  runs = 0
  for i in range(0,count-1):
    k=0
    runs += 1
    swap = 1
    print "Run #"+ str(i+1) +": ",inp
    for j in range(1,count):
      if inp[k]>inp[j]:
        tmp = inp[k]
        inp[k] = inp[j]
        inp[j] = tmp
        swap = 0
      k = k + 1
      print "Run #" + str(i+1) + "." + str(j) + ": ", inp
    if swap:
      break
  print "Number of runs: ", runs
  print "Sorted list: ", inp
  return inp

if __name__ == "__main__":
  main()
