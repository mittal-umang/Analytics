# Chapter 12 Question 16
class Stack(list):
    def __init__(self):
        super().__init__()

    def push(self, value):
        self.append(value)

    def isEmpty(self):
        return len(self) == 0

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self[0]

    def getSize(self):
        return len(self)


def main():
    stack = Stack()
    print("Enter value in list:")
    while stack.getSize() < 5:
        stack.push(input())
    print("String in reverse is:")
    while not stack.isEmpty():
        print(stack.pop(), end="\t")


if __name__ == '__main__':
    main()
