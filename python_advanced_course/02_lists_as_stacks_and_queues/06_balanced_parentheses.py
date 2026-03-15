parentheses_line = input()
parentheses = {"(": ")", "[": "]", "{": "}"}
opening_parentheses_stack = []

for par in parentheses_line:
    if par in parentheses:
        opening_parentheses_stack.append(par)
    elif par in parentheses.values():
        if not opening_parentheses_stack:
            print("NO")
            break
        last_opening = opening_parentheses_stack.pop()

        if parentheses[last_opening] != par:
            print("NO")
            break
else:
    if opening_parentheses_stack:
        print("NO")
    else:
        print("YES")
