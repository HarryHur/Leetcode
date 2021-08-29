"""
Codeup problem
Input 1 character and print the next character

Note : chr() and ord()
        chr() => unicode change to character
        ord() => character change to unicode
""" 
a = input()
a = ord(a)
b = a+1
print(chr(b))