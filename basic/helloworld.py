import sys

def hello(name):
  """The universal first program everyone writes before embarking on a
     programming journey """
  print "Hello",name

def main():
  hello(sys.argv[1])

#Boilerplate

if __name__ == "__main__":
  main()
