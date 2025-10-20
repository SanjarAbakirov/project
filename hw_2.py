# import sys

# this is the task for donuts
def main():
  num_don = int(input('How many donuts?'))
  if num_don <= 9:
    # num_don = sys.argv[1]
    print("Number of donuts:", + num_don),
  else:
    print("You eat too many of them")

if __name__ == '__main__':
# Код, который выполняется только при прямом запуске (например, main()),
# и код (функции, классы), который можно использовать при импорте, не вызывая побочных эффектов.
# «Если этот файл запущен напрямую (а не импортирован), то вызови функцию main()».
  main()

# --------------------

def match_ends(words):
  words = int(input('How many donuts?'))


 
match_ends("Sammy", "Tonny", "Johny")

def main():
  if len(sys.argv) >= 2:
    name = sys.argv[1]
  else:
    name = 'World'
  print('Hello', name)





# def sum_num(a, b):
#    return a + b


# practice

# num_don = int(input("How many donuts?"))
# # print(type(num_don))
# if num_don >10:
#     print("A lot. Eat less")
# elif num_don == 0: 
#     print("find more donuts")
# else:
#     print("You have enough")