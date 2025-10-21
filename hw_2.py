words = ["level", "property", "aza", "kazak", "python", "lesha", "amanda"]
result = 0

def check_fn(words):
  count = 0
  for word in words:
      if word[0] == word[-1]:
        count += 1
  return count
check_fn(words)
result = check_fn(words)
print(result)


 





















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