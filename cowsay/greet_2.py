import cowsay
import sys
import io
from contextlib import redirect_stdout

if len(sys.argv) != 3:
    sys.exit("Usage: python greet_2.py [name] [output_file]")

name = sys.argv[1]
output_file = sys.argv[2]

# Capture the output of cowsay.cow
f = io.StringIO()
with redirect_stdout(f):
    cowsay.trex(f"Hello, {name}")
message = f.getvalue()

# Write the captured message to a file
with open(output_file, "w") as file:
    file.write(message)

print(f"Message written to {output_file}")
