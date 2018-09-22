#this one is like your scripts
def print_two(*args):
  arg1, arg2 = args
  print(f"arg1: {arg1}, arg2: {arg2}")


#ok, the *args are actually pointless, we can do just this
def print_two_again(arg1, arg2):
   print(f"arg1: {arg1}, arg2: {arg2}")


#this just takes one argument
def print_one(arg1):
  print(f"arg1: {arg1}")


#this one takes no argument
def print_none():
  print("I got nothin'.")


print_two("Joy","Dalud")
print_two_again("Joy","Dalud")
print_one("Majoy")
print_none()
