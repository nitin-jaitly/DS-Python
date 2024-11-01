
"""
Hello world
Problem Statement: Design a MinStack class that supports pushing, popping, retrieving the top element, and retrieving the minimum element in constant time O(1).
Requirements:
1.	push(x): Pushes element x onto the stack.
2.	pop(): Removes the element on top of the stack.
3.	top(): Gets the top element of the stack.
4.	getMin(): Retrieves the minimum element in the stack.
5.	The MinStack should be efficient in terms of space and time, ensuring all operations are performed in O(1) time complexity.

Constraints:
•	Assume all operations are valid (e.g., a pop or top operation will only be called if there is at least one element in the stack).
•	All stack operations (push, pop, top, getMin) should operate in O(1) time.
Example Operations and Results:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()   // Returns -3.
minStack.pop()
minStack.top()      // Returns 0.
minStack.getMin()   // Returns -2.

"""
#from collections import List
class MinStack:
    def __init__(self):
        self.my_stack = []
        self.min_stack = []

    def push(self,x:int ) -> None:
        self.my_stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    def print(self):
        print(self.my_stack)
        print(self.min_stack)

    def pop(self) -> None:
        if self.my_stack:
            if self.my_stack[-1]  == self.min_stack[-1]:
                self.min_stack.pop()
        return self.my_stack.pop()

    def top(self):
        if self.my_stack:
            return self.my_stack[-1]
        return None

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return -1

def main():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.print()
    print("min_value = " , minStack.getMin()) # Returns - 3.
    assert minStack.getMin() == -3

    minStack.print()
    #
    minStack.pop()
    #
    print(minStack.top()) # Returns 0.
    assert minStack.top() == 0
    #
    assert minStack.getMin() == -2

if __name__ == "__main__":
    main()




