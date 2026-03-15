with open("text.txt") as f:
    for index, line in enumerate(f):
        if index % 2 == 0:
            for ch in "-,.!?":
                line = line.replace(ch, "@")
            print(" ".join(reversed(line.split())))
