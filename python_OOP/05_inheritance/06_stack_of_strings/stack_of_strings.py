class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        return self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not any(self.data)

    def __str__(self) -> str:
        return "[" + ", ".join(reversed(self.data)) + "]"


new_stack = Stack()
new_stack.push("a")
new_stack.push("d")
print(new_stack.__str__())
print(new_stack.is_empty())
