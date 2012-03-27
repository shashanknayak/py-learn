import sys

def main():
  inp = [5,4,2,8,-1,3,11,9,-4]
  print inp
  sort(inp)
  
def sort(inp):
  count = len(inp)
  for i in range(1,count):
    key = inp[i]
    j = i - 1
    while j>=0 and inp[j]>key:
      inp[j+1] = inp[j]
      j = j - 1
    inp[j+1] = key
  print inp

if __name__ == "__main__":
  main()
