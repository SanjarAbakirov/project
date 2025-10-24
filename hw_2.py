# A match_ends

# words = ["level", "property", "aza", "kazak", "python", "lesha", "amanda", "asa", "sas", "s", "de"]

# def match_ends(words):
#   arr = []
#   count = 0
#   for word in words:
#       if len(word) >= 2:
#          count += 1 
#   return count
# match_ends(words)
# result = match_ends(words)
# print(result)

# training
# words = ["xylophone", "apple", "axe", "extra", "berry", "xenon"]
# result = 0
# def gpt_fn(words):
#     arr = []
#     for word in words:
#       if word[0] == "x" or len(word) < 5:
#          arr.append(word)
#     return arr
# gpt_fn(words)
# result = gpt_fn(words)
# print(result)

# Task - the palindrome
# words = ["level", "property", "aza", "kazak", "python", "lesha", "amanda", "kyshtak", "sas", "xex"]

# def match_ends(words):
#   arr = []
#   for word in words:
#       if word[0] == word[-1]:
#         arr.append(word)
#   return arr
# match_ends(words)
# result = match_ends(words)
# print(result)

# task front_x
# words = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark', 'java', 'xawier', 'avitchi', 'xpara']
# result = 0

# def front_x(words):
#   arr = []
#   arr2 = []
#   joined = 0
#   for word in words:
#       if word[0] == 'x':
#         arr.append(word)
#       else:
#          arr2.append(word)
#       joined = arr + arr2
#   return joined
# front_x(words)       
# result = front_x(words)
# print(result)


# sort_last
# list = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
# element = lambda element:element[1]
# list.sort(key=element)
# print(list)

# test fn

def main(n):
    return n ** 3
import unittest

class MyTest(unittest.TestCase):

  def test(self):
    result = main(3)
    expect = 27
    self.assertEqual(result, expect)
 
    if main(1) == 8:
        prefix = 'Ok'
    else:
        prefix = 'X'
    print('%s got: %s expected: %s' % (prefix, repr(result), repr(expect)))

if __name__ == '__main__':
  unittest.main()




  
 



# def main():
#     def test(got, expected):
#         if got == expected:
#             prefix = 'Ok'
#         else:
#             prefix = 'X'
#         print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))
#     test()
# main()









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