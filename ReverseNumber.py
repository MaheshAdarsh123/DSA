# a simple way in python 

string = str(input("Enter a text"))
reversed = string[::-1]

if(string == reversed):
    print("Palindrome")
else:
    print("Not Palindrome")