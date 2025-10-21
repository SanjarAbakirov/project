# A match_ends

words = ["level", "property", "aza", "kazak", "python", "lesha", "amanda", "kyshtak", "sas"]

def match_ends(words):
  arr = []
  for word in words:
      if word[0] != word[-1]:
        arr.append(word)
  return arr
match_ends(words)
result = match_ends(words)
print(result)

# 







# Ex with the palindrome
# words = ["level", "property", "aza", "kazak", "python", "lesha", "amanda", "kyshtak", "sas"]

# def match_ends(words):
#   arr = []
#   for word in words:
#       if word[0] != word[-1]:
#         arr.append(word)
#   return arr
# match_ends(words)
# result = match_ends(words)
# print(result)




















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