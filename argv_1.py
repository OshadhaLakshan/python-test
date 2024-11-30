import sys

try:
    print("Hellow, My name is", sys.argv[1])
except IndexError:
    print("Ex: python argv_1.py [YOUR_NAME]")
