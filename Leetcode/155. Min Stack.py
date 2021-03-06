

class MinStack:

    def __init__(self):
        self._stack = []

    def push(self, x: int) -> None:
        if not self._stack:
            self._stack.append((x, x))
        else:
            if x < self._stack[-1][1]:
                self._stack.append((x, x))
            else:
                self._stack.append((x, self._stack[-1][1]))

    def pop(self) -> None:
        return self._stack.pop()[0]

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(5)
obj.push(3)
obj.push(10)
obj.push(2)

print(obj.top())
print(obj.getMin())
obj.pop()
print(obj.getMin())
