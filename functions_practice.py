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