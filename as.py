import pyfiglet
import sys
import time

result = pyfiglet.figlet_format("[  A  S  ]", font="big")

for c in result:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.01)


