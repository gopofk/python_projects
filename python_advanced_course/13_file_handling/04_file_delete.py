import os

try:
    os.remove("python.txt")
except FileNotFoundError:
    print("no such file")
