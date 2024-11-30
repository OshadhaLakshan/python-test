import sys

while True:
    try:
        print("Hellow, My name is", sys.argv[1])
        break
    except IndexError:
        print("Ex: python argv_1.py [YOUR_NAME]")
        break
