import time
import random
import sys

def human_print(string):
    for i in string:
        if random.randint(0,6) == 0:
            print(chr(random.randint(97,122)), end="")
            sys.stdout.flush()
            time.sleep(.7)
            print("\b" + i, end="")
            sys.stdout.flush()
            time.sleep(.7)
        else:
            print(i, end="")
            sys.stdout.flush()
            time.sleep(.3)
    print("\n")

def type_print(string):
    for i in string:
        print(i, end="")
        sys.stdout.flush()
        time.sleep(.1)
    print("\n")

def reverse_print(string):
    for i in range(len(string)-1,-1,-1):
        print(" "*i + string[i], end="")
        sys.stdout.flush()
        time.sleep(.2)
        print("\r", end="")
    print("\n")

def scroll_print(string):
    for i in range(len(string)-1,-1,-1):
        print(string[i:] + "\r", end="")
        sys.stdout.flush()
        time.sleep(.2)
    print("\n")

def overwrite_print(string):
    for i in range(len(string)):
        print("X", end="")
    sys.stdout.flush()
    print("\r", end="")
    for i in string:
        time.sleep(.2)
        print(i, end="")
        sys.stdout.flush()
    print("\n")


# string = input("Enter your string: ")
# human_print(string)
# type_print(string)
# reverse_print(string)
# scroll_print(string)
# overwrite_print(string)

