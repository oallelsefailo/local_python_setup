def hello():
    print("Hello! Welcome!")

def pack(item1, item2, item3):
    packed_list = [item1, item2, item3]
    return packed_list

def eat_lunch(lunchbox):
    if lunchbox:
        print("First I eat", lunchbox[0])
        for item in lunchbox[1:]:
            print("Next I eat", item)
    else:
        print("My lunchbox is empty!")

hello()
eat_lunch(pack("Sandwich", "Sour Patch Kids", "Chips"))

## ACTIVITY 11/01 ##

def max_num(a, b, c):
    return max(a, b, c)

def mult_list(numbers_list):
    result = 1
    for numbers in numbers_list:
        result *= numbers
    return result

def rev_string(input_string):
    return input_string[::-1]

print(max_num(5, 12, 245))
print(mult_list([1, 2, 3, 4]))
print(rev_string("SUP DAWG"))

def num_within(number, start, end):
    return start <= number <= end

print(num_within(3, 2, 4))

def pascal(n):
    for i in range(n):
        num = 1
        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)
        print()

pascal(4)

## ACTIVITY 11/4 ##

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

""" 
How does this solution ensure data immutability?

We're not modifying the array 

Is this solution a pure function? Why or why not?

I think so?

Is this solution a higher order function? Why or why not?

No, we're not returning any other functions here

Would it have been easier to solve this problem using a different programming style?

Possibly but it doesn't come to me as to how..

Why in particular is functional programming a helpful paradigm when solving this problem?

I honestly don't know lol, maybe because it's easier to read..
"""

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    
    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def flame_jet(self, other_podracer):
        other_podracer.condition = "trashed"

"""
We're using encaspulation with the podracers from its parent class
abstraction with the methods in the main podracer class
inheritance from creating the new prodracer classes that take in the main podracers properties

I don't think this one would have been easier to use in another style because if we wanted to start using different variables or rename them, we
can just do it at the main podracer level, rather than going through all of them to change.

We were able to structure the data using OOP that allows inheritance through the other podracer classes 
"""