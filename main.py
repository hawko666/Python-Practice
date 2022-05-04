#print("hello world")
#this is comment
#print("hello\nworld")

#this is multiline string
#print("""hello
      
#      jasjhl
#      fahsdkj;k""")
#concadinating
#print("hello" + " World")

#multiple string
#print("hello" * 10)

#***************************************************lesson 2

#to get user input   input("What is your name")
#this will print the responce
#print(input("What is your name\t"))

#***************************************************

name = input("Whats your name \t")

#use exit to end the code
if name == "ben":
  print("Get lost!!!")
  exit
else:
  print("Hello " + name + ", I am beta\n\n\n")

  menu = "black coffee, Espresso, Latte, Cappucino"

  print(name + ", What is your order\n" + menu)

  order = input()

  price = 8

  qty = int(input("how many cups do you want?\n"))

 #can also do int(qty) here
  total = price * qty

#converting to string
  print("your total price is " + str(total))

  print(str(qty) + " coffee of " + order + ", comeing-up quick !!")


#if 2 > 3:
  print("it's true")
#else:
  print("not true")




#***************************************************lesson 3
#age = 22
#print(age)
#print(type(age))
#python follow bodams rules
