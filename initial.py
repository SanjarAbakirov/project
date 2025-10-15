# test
# def new_fn(name):
#     print(f"Hello, {name}")
# new_fn("Sam")



import sys
# Define a main() - the function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
  if len(sys.argv) >= 2:
    name = sys.argv[1]
  else:
    name = 'Alice'
  print('Hello', name)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()


def my_function():
    print("Hellow from My fn")

def some_fn_from_me():
    print("Smbody called my fn")

# some_fn_from_me()
# my_function()

# arguments
# pattern
# def my_fn_args(username, greetings):
    # print("Hello, %s , from my Fn! with you %s"%(username, greetings))
# my_fn_args("Sam", "we do many things and projects")

