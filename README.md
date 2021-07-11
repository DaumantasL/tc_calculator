# tc_calculator
A simple memory-based calculator - a packaging exercise for Turing College.

## Installation

To install: `pip install git+https://github.com/DaumantasL/tc_calculator`

Import as: `from calculator.operations import calculator`

## Methods

Calculator stores a single float value in memory, all other operations are performed on it and update it.

Initialize with `calculator(value)`. Default value of 0.

### Memory

```
memory
Returns number in memory
 ```
 
 ```memory = number
 Sets calculator memory to number value provided
 ```
 
 ```reset()
 Resets calculator memory to 0
 ```
 ### Operations

```add(number)
 Adds number to number in calculator memory
 ```
 
 ```subtract(number)
 Subtracts number from number in calculator memory
 ```
 
  ```multiply(number)
 Multiplies number in calculator memory by number
 ```
 
  ```divide(number)
 Divides number in calculator memory by number
 ```
 
   ```power(number)
 Raises number in calculator memory to n-th power
 ```
 
   ```root(number)
 Takes n-th root of number in calculator memory
 ```
