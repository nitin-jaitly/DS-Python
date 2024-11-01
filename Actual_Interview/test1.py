
"""
num = 0

val = 1

num + val / 2

num + val / 3

Given a series of integer values, implement a RunningAverage class to calculate the running average of the values added.
The class should support adding new values and retrieving the current running average.
You may assume that the class will be used in a multi-threaded environment, and you need to ensure thread safety.
Example 1:
ra = RunningAverage()
ra.add(1)
ra.add(2)
ra.add(3)
print(ra.get_average())  # Output: 2.0
Output: 2.0
Explanation: The running average after adding 1, 2, and 3 is (1 + 2 + 3) / 3 = 2.0.
Example 2:
ra = RunningAverage()
ra.add(5)
ra.add(10)
print(ra.get_average())  # Output: 7.5
ra.add(15)
print(ra.get_average())  # Output: 10.0
Output: 7.5, 10.0
Explanation: The running average after adding 5 and 10 is (5 + 10) / 2 = 7.5. After adding 15, it is (5 + 10 + 15) / 3 = 10.0.
Example 3:
ra = RunningAverage()
print(ra.get_average())  # Output: 0.0
Output: 0.0
Explanation: The initial running average is 0.0 before any values are added.
Constraints:
The add method should be thread-safe.
The get_average method should return a float representing the running average.
The class should handle a large number of additions efficiently.
Instructions:
Implement the RunningAverage class according to the specifications.
Ensure thread safety in a multi-threaded environment.
Optimize the class to handle a large number of additions efficiently.
has context menu


has context menu
"""
import threading

class runningAverage:

    def __init__(self):
        self.count = 0
        self.avg = 0
        self.lock = threading.Lock()

    def add(self, new_val):
        with self.lock:
            self.count += 1
            self.avg = self.avg +  ( new_val - self.avg) / self.count
            print("avg ", self.avg)

    def get_average(self):
        with self.lock:
            return self.avg

def main():
    print("---------------")
    print("EXAMPLE 1")
    ra = runningAverage()
    ra.add(1)
    print(ra.get_average())
    ra.add(2)
    print(ra.get_average())
    ra.add(3)
    ra.get_average()

    ##
    print("---------------")
    print("EXAMPLE 2")
    ra_ex2 = runningAverage()
    ra_ex2.add(5)
    ra_ex2.get_average()
    ra_ex2.add(10)
    ra.get_average()
    ra_ex2.add(15)
    ra.get_average()
    print(ra.get_average())

    print("---------------")
    print("EXAMPLE 3")
    ra_ex3 = runningAverage()
    ra_ex3.add(0)
    ra_ex3.get_average()

if __name__ == "__main__":
    main()
