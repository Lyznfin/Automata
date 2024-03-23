a = [0, 30, 5, 6, 7, 3, 9, 12, 0, 4, 3, 21, 5, 6]
c = [True if s % 3 == 0 else False for s in a] # lmao, how is doing ternary + list comp allowed
print(c)