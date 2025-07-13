# Problem: Create a class MyStack with push(), pop(), and peek() methods.

class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        return

    def pop(self):
        return self.stack.pop()

    def show(self):
        return self.stack

stack = MyStack()
stack.push(5)
stack.push(10)
stack.push(89)
print(stack.show())
print(stack.pop())
print(stack.pop())
print(stack.pop())