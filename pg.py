while True:
  x = input("welcome, would you like to write your json data? y/n>")
  if x == "y":
    exec(open('main.py').read())
  if x == "n":
    # Your code for handling when x is "n" goes here
    print("ok")