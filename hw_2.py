import sys

def main():
  



  if len(sys.argv) >= 2:
    name = sys.argv[1]
  else:
    name = 'World'
  print('Greetings', name)

if __name__ == '__main__':
  main()



# def sum_num(a, b):
#    return a + b