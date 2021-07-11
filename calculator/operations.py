import numbers

class CalculatorError(Exception):
    """For calculator errors"""

class calculator:
    """A memory-based basic calculator."""
    def __init__(self, memory: float = 0) -> None:
        """Initialize calculator with a number to perform operations on. Zero by default."""
        self._check_argument(memory)
        self.__memory = memory

    @property
    def memory(self) -> float:
        """Returns number in memory"""
        return self.__memory

    @memory.setter
    def memory(self, new_memory: float):
        """Sets calculator memory to number value provided"""
        self._check_argument(new_memory)
        self.__memory = new_memory

    @memory.deleter
    def memory(self) -> None:
        """If calculator memory deleted, sets it to 0"""
        self.__memory = 0
        print(f"Calculator memory set to {self.__memory}")

    def reset(self):
        """Resets calculator memory to 0"""
        self.__memory = 0
        return self.__memory

    def add(self, argument:float):
        """Adds number to number in calculator memory"""
        self._check_argument(argument)
        self.__memory = self.__memory + argument
        return self.__memory
    
    def subtract(self, argument:float):
        """Subtracts number from number in calculator memory"""
        self._check_argument(argument)
        self.__memory = self.__memory - argument
        return self.__memory

    def multiply(self, argument:float):
        """Multiplies number in calculator memory by number"""
        self._check_argument(argument)
        self.__memory = self.__memory * argument
        return self.__memory

    def divide(self, argument:float):
        """Divides number in calculator memory by number"""
        self._check_argument(argument)
        try:
            self.__memory = self.__memory / argument
            return self.__memory
        except ZeroDivisionError as ex:
            raise CalculatorError("You can't divide by zero.") from ex

    def root(self, argument:float):
        """Takes n-th root of number in calculator memory"""
        self._check_argument(argument)
        try:
            self.__memory = self.__memory ** 1/argument
            return self.__memory
        except ZeroDivisionError as ex:
            raise CalculatorError("You can not take a 0th root.") from ex
    
    def power(self, argument:float):
        """Raises number in calculator memory to n-th power"""
        self._check_argument(argument)
        self.__memory = self.__memory ** argument
        return self.__memory

    def _check_argument(self, argument):
        """Checks whether argument is a number."""
        if not isinstance(argument, numbers.Number):
            raise CalculatorError(f'"{argument}" is not a number.')
