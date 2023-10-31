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
pack()
eat_lunch()