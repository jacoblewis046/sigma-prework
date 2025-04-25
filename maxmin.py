
def str_to_list(str):
    str_list = str[1:-1].split(",")
    return [int(x) for x in str_list]


ints = input("Enter your ints: ")
ints_list = str_to_list(ints)
# print(ints_list)

min = 10000000000000
max = 0

for num in ints_list:
    if num > max:
        max = num
    if num < min:
        min = num

print([min,max])