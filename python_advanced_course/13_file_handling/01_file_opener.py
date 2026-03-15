try:
    file = open("text.txt")
except FileNotFoundError:
    print("Sorry, file not found")
finally:
    print("exit")
