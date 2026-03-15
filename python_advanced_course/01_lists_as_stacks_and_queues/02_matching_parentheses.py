line = input()
stack = []
for i in range(len(line)):
    if line[i] == "(":
        stack.append(i)
    elif line[i] == ")":
        start_index = stack.pop()
        end_index = i + 1
        print(line[start_index:end_index])
