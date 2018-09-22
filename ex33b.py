def while_loop(x,y):
  i = 0
  numbers = []

  while i < x:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + y
    print("Numbers now:", numbers)
    print(f"At the bottom i is {i}")


def for_loop(x,y):
  i = 0
  numbers = []

  for i in range(0,x):
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + y
    print("Numbers now:", numbers)
    print(f"At the bottom i is {i}")    


#while_loop(10,2)
for_loop(10,2)
