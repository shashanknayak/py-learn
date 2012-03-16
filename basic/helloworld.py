import sys

def hello(name):
  """The universal first program everyone writes before embarking on a
     programming journey """
  print "Hello",name

def main():
  if not sys.argv[1]:
    name = "???"
  else:
    name = sys.argv[1]
  hello(name)

#Boilerplate

if __name__ == "__main__":
  main()
