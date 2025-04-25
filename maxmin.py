
def str_to_list(str):
    str_list = str[1:-1].split(",")
    return [int(x) for x in str_list]

def maxmin(ints_list):
    min = float("inf")
    max = float("-inf")

    for num in ints_list:
        if num > max:
            max = num
        if num < min:
            min = num

    return [min,max]


ints = input("Enter your ints: ")
ints_list = str_to_list(ints)
print(maxmin(ints_list))


