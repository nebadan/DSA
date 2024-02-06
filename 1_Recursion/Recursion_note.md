# Recursion Note

- Recursion = a way of solving problem by having a function calling itself

## Properties

- performing thee same operation multiple times with different inputs
- In every step we try smaller inputs to make the problem smaller
- Base condition is needed to stop the recursion, otherwise infinte loop will occur

## Why recursion ?

1.  Recursive thinking is really important in programming and helps you break down big problems into smaller ones and easier to use 

* when to choose recursion ? if the problem starts with this ...
    * If you can divine the problem into similar sub problems
    * Design an algorithm to compute nth...
    * Write the code to list the n...
    * Implement a method to compute all
    * Practice

2. The prominent usage of recurssion in datastructure like tress and graphs

3. Interviews

4. It is used in many algorithms (divide and conquer, greedy and dynamic programming)

## How recursion works ?

1. A method calls it self
2. Exit from infinte loop

```
def recursionMethod(parameters):
    if exit from condition satisfied:
        return some value
    else:
        recursionMethod(modified parameter)
```
Example.py
```
def recursiveMethod(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursiveMethod(n - 1)
        print(n)
```
Output 
```
n is less than 1
1
2
3
4
```

## Recursive vs Iterative Solutions
* Any problem that can be solved using recursion can be solved using iteration

Recursive
```
def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n - 1)
        return power * 2
```
Iterative
```
def powerOfTwo(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + i
        return power
```
* let compare them:
    * Iteration is space efficent (No stack memory require in case of iteration) 
    * Iteration is time efficient (In case of recurssion system needs more time for pop and push elements to stack memory which makes recurssion less time efficient)
    * Recurssion is easy to code (We use recursion especially in the case we know that a problem can be divided into similar sub problems)


## When to Use/Avoid Recursion ?
When to use it ?
* When we can easily breakdown problem into similar subproblem
* When we are fine with extra overhead(both time and space) that comes with it
* When we need a quick working solution instead of efficient one
* When traverse a tree
* When we use memoization in recursion

When to avoid it ?
* If time and space complexity matter for us
* Recursion uses more memory. If we use embedded memory. For example an application that take more memory in the phone is not efficient
* Recursion can be slow if not implemented right!


## Hot to write recursion in 3 steps ?
1. Recursive case - the flow
2. Base case - the stopping criterion
3. Unintentional case - the constraint