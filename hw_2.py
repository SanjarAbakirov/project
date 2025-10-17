import sys

def main():
  
  if len(sys.argv) >= 2:
    name = sys.argv[1]
  else:
    name = 'World'
  print('Greetings', name)

if __name__ == '__main__':
  main()
# Код, который выполняется только при прямом запуске (например, main()),
# и код (функции, классы), который можно использовать при импорте, не вызывая побочных эффектов.
# «Если этот файл запущен напрямую (а не импортирован), то вызови функцию main()».

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