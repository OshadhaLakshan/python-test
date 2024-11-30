import cowsay
import sys

if len(sys.argv) < 2:
    sys.exit("Too few Arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many Arguments")

cowsay.cow("Hellow, " + sys.argv[1])