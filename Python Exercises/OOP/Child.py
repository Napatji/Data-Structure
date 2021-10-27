from typing import Mapping
from Cal import Calculator
class Child(Calculator):
    def __init__(self,name):
        super.__init__(self,name)
if __name__ == "__main__":
    test = Child()
    test.calculate(52,13,"/")

