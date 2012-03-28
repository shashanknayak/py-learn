import sys

def main():
  n = int(sys.argv[1])
  init_str = ""
  for i in range(1,n+1):
    init_str += str(i)
  print init_str  
  ret = permute(init_str, n)
  ret_int = []
  for key in ret:
    ret_int.append(int(key))

  ret_int.sort()
  print "Sorted List of Permutations: ", ret_int
  print "Number of permutations: ", len(ret_int)

def permute(init_str,n):
  perm_list = []
  if n == 1:
    perm_list.append(init_str)
    print "Run #1: ", perm_list
    return perm_list
  ret_list = permute(init_str[1:],n-1)
  for key in ret_list:
    for j in range(0,n):
      perm_list.append(key[:j] + init_str[0] + key[j:])
  print "Run #" + str(n) + ": ", perm_list 
  return perm_list

if __name__ == "__main__":
  main()
