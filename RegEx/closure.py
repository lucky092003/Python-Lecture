# def outer_function(message):
#     def inner_function():
#         print(message)

#     return inner_function

# closure = outer_function("hey")
# closure()


# def counter():
#     count =0
#     def increment():
#         nonlocal count 
#         count += 1
#         print(count)

#     return increment
# c1 = counter()
# c1()
# c1()
# c2 = counter()
# c2()
# c1()

import time
start = time.time
print(start)