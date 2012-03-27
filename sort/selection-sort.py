def main():
  inp = [4,3,1,-1,9,16,7]
  print "Unsorted List: ", inp
  sort(inp)

def sort(inp):
  count = len(inp)
  for i in range(0,count-1):
    min_ele = inp[i]
    min_ind = i
    for j in range(i+1, count):
      if min_ele>inp[j]:
        min_ele = inp[j]
        min_ind = j
    tmp = inp[i]
    inp[i] = inp[min_ind]
    inp[min_ind] = tmp
    print "run #"+str(i+1)+": ", inp  
  print "Sorted List: ", inp

if __name__ == "__main__":
  main()

