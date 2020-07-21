# Takes the first name from the user and compares it to yours,
# Then if the name the user entered is the same as yours, print out such as : 
# "Hello, Joseph! The password is : W@12",
# If the name the user entered is not the same as yours, print out such as : 
# "Hello, Amina! See you later."

name = input('please enter a your first name :')
my_name = 'Mehmet'
if name.strip().casefold() == my_name.casefold() :
    print('Hello, Mehmet! The password is : W@12')
else :
    print("Hello, Amina! See you later.")