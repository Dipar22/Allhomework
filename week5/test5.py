import sys
import math
user=sys.argv[1:]
if bool(user)==True:
    temperature = []
    for x in user:
        temp=int(x)
        temperature.append(temp)
    print ("Maximum =", max(temperature))
    print("Minimum=", min(temperature))
    print("Mean=", sum(temperature)/6)
else:
    print("error")